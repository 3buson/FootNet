__author__ = 'matic'

import time
import pyodbc
import traceback
import networkx as nx
from datetime import date
from collections import deque

import constants


### ---- DATABASE FUNCTIONS ---- ###

def connectToDB():
    connection = None

    while connection is None:
        try:
            connection = pyodbc.connect('DSN=FootNet')

        except Exception, e:
            print "\n[DB connector]  Error connecting to database. Trying again in 1 sec.", e
            traceback.print_exc()

        time.sleep(1)

    return connection


def getCountriesDict(connection):
    cDict = dict()

    try:
        cursor = connection.cursor()

        cursor.execute('''
                        SELECT *
                        FROM countries
                       ''')

        result = cursor.fetchall()

        for resultRow in result:
            cDict[resultRow[1]] = resultRow[0]

    except pyodbc.DatabaseError, e:
        print "\n[Countries mapper]  ERROR - DatabaseError", e
        pass

    finally:
        return cDict


def checkIfPlayerExists(connection, playerId):
    exists = False

    try:
        cursor = connection.cursor()

        cursor.execute('''
                        SELECT *
                        FROM player
                        WHERE idP = ?
                       ''',
                       playerId)

        result = cursor.fetchall()

        exists = (len(result) > 0)

    except pyodbc.DatabaseError, e:
        print "\n[Player existence checker]  ERROR - DatabaseError\n", e
        pass

    finally:
        return exists


### ---- DATABASE SUM FUNCTIONS ---- ###

def calculatePlayersCareerSums(connection):
    cursor = connection.cursor()

    print "\n[Players Career Sum Calculator]  Updating players career stats..."

    cursor.execute('''
                    SELECT idP, SUM(apps), SUM(goals), SUM(assists), SUM(ownGoals), SUM(yellowCards), SUM(redCards), SUM(onSubs), SUM(offSubs), SUM(penaltyGoals), SUM(concededGoals), SUM(cleanSheets), SUM(minutesPerGoal), SUM(minutesPlayed)
                    FROM playerclubseason
                    GROUP BY idP
                   ''')

    playersCareerStats = cursor.fetchall()

    for pcs in playersCareerStats:
        try:
            cursor.execute('''
                            UPDATE player
                            SET apps=?, goals=?, assists=?, ownGoals=?, yellowCards=?, redCards=?, onSubs=?, offSubs=?, penaltyGoals=?, concededGoals=?, cleanSheets=?, minutesPerGoal=?, minutesPlayed=?
                            WHERE idP = ?
                           ''',
                           pcs[1], pcs[2], pcs[3], pcs[4], pcs[5], pcs[6], pcs[7], pcs[8], pcs[9], pcs[10], pcs[11], pcs[12], pcs[13], pcs[0])

        except pyodbc.DatabaseError, e:
            print "[Players Career Sum Calculator]  ERROR - DatabaseError", e
            traceback.print_exc()

            pass

        finally:
            connection.commit()

    print "[Players Career Sum Calculator]  Finished updating players career stats\n"


def calculateClubsSums(connection):
    cursor = connection.cursor()

    print "\n[Clubs Sum Calculator]  Updating clubs stats..."

    cursor.execute('''
                    SELECT idClub, SUM(apps), SUM(goals), SUM(assists), SUM(ownGoals), SUM(yellowCards), SUM(redCards), SUM(onSubs), SUM(offSubs), SUM(penaltyGoals), SUM(concededGoals), SUM(cleanSheets), AVG(minutesPerGoal), SUM(minutesPlayed)
                    FROM playerclubseason
                    GROUP BY idClub
                   ''')

    playersCareerStats = cursor.fetchall()

    for pcs in playersCareerStats:
        try:
            cursor.execute('''
                            UPDATE club
                            SET apps=?, goals=?, assists=?, ownGoals=?, yellowCards=?, redCards=?, onSubs=?, offSubs=?, penaltyGoals=?, concededGoals=?, cleanSheets=?, minutesPerGoal=?, minutesPlayed=?
                            WHERE idClub = ?
                           ''',
                           pcs[1], pcs[2], pcs[3], pcs[4], pcs[5], pcs[6], pcs[7], pcs[8], pcs[9], pcs[10], pcs[11], pcs[12], pcs[13], pcs[0])
        except pyodbc.DatabaseError, e:
            print "[Clubs Sum Calculator]  ERROR - DatabaseError", e
            traceback.print_exc()

            pass
        finally:
            connection.commit()

    print "[Clubs Sum Calculator]  Finished updating players career stats\n"


### ---- WEIGHT FUNCTIONS ---- ###

def calculatePlayersWeight(playerId1, playerId2, playersInfo, withInflation=True):
    weight = 0

    if(withInflation):
        inflationRatio = constants.inflationRatio / 100 # average inflation ratio per year (percent)
    else:
        inflationRatio = 0


    if(len(playersInfo[playerId1]) > len(playersInfo[playerId2])):
        playedMoreSeasons = playerId1
        playedLessSeasons = playerId2
    else:
        playedMoreSeasons = playerId2
        playedLessSeasons = playerId1


    for currentSeason in playersInfo[playedLessSeasons]:
        # players have common season
        if(playersInfo[playedMoreSeasons].has_key(currentSeason)):
            # players have played in the same club in this season
            if(playersInfo[playedMoreSeasons][currentSeason][2] == playersInfo[playedLessSeasons][currentSeason][2]):

                playerValue1 = playersInfo[playedLessSeasons][currentSeason][4]
                playerValue2 = playersInfo[playedMoreSeasons][currentSeason][4]

                inflation = 1 + (inflationRatio * (date.today().year - 2000 - currentSeason))

                if(not playerValue1):
                    playerValue1 = 1
                # take inflation into account
                else:
                    playerValue1 = float(playerValue1) * inflation

                if(not playerValue2):
                    playerValue2 = 1
                # take inflation into account
                else:
                    playerValue2 = float(playerValue2) * inflation

                weight += (playerValue1 + playerValue2) / 100000.0

    return weight


def calculateClubWeight(clubId, clubsInfo, byValue=True):
    if('importance' in clubsInfo[clubId]):
        # weight is defined by club value
        if(byValue):
            destinationClubValue = clubsInfo[clubId]['importance'][0]

            weight = float(destinationClubValue) * 2 / 1000000
        # weight is defined by club ranking
        else:
            destinationClubRanking = clubsInfo[clubId]['importance'][1]
            clubLeague             = clubsInfo[clubId]['league']
            clubLeagueRanking      = constants.leagueRankings[clubLeague]

            if(destinationClubRanking != 0):
                fixedRanking = max((float(destinationClubRanking) / 2), 1)
                weight = (1 / fixedRanking) * clubLeagueRanking * 2
            else:
                weight = (1 / constants.noRankingPenalty) * clubLeagueRanking * 2
    else:
        weight = constants.defaultClubWeight

    return weight


### ---- GRAPH CREATION FUNCTIONS ---- ###

def createGraphFromEdgeList(filename, directed=False):
    print "\n[Graph Creator]  Reading filename %s..." % filename

    nodeData = dict()

    if(directed):
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

    with open(filename) as f:
        skipped = 0
        edges   = 0

        for line in f:
            if(line[0] != '#'):
                edges += 1
                [node1, node2] = line.split()
                graph.add_edge(int(node1), int(node2), weight=0)
            else:
                skipped   += 1
                slicedLine = line.split('"')

                if(len(slicedLine) > 1):
                    [nodeId, nodeName, nodeProperty] = slicedLine

                    if(len(slicedLine) > 2):
                        nodeData[int(nodeId[2:])] = (nodeName, int(nodeProperty))
                    else:
                        nodeData[int(nodeId[2:])] = nodeName

                    graph.add_node(int(nodeId[2:]))

    print "[Graph Creator]  Read filename %s, skipped %d lines" %\
          (filename, skipped)
    print "[Graph Creator]  Graph has %d nodes and %d edges" %\
          (graph.number_of_nodes(), graph.number_of_edges())
    print "[Graph Creator]  Edges in edge list %d\n" % edges

    return graph, nodeData


def createWeightedGraphFromEdgeList(filename, directed=False):
    print "\n[Weighted Graph Creator]  Reading filename %s..." % filename

    nodeData = dict()

    if(directed):
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

    with open(filename) as f:
        skipped = 0
        edges   = 0

        for line in f:
            if(line[0] != '#'):
                edges += 1
                [node1, node2, weight] = line.split()
                graph.add_edge(int(node1), int(node2), weight=float(weight))
            else:
                skipped   += 1
                slicedLine = line.split('"')

                if(len(slicedLine) > 1):
                    [nodeId, nodeName, nodeProperty] = slicedLine

                    if(len(slicedLine) > 2 and nodeProperty != '\n'):
                        nodeData[int(nodeId[2:])] = (nodeName, int(nodeProperty))
                    else:
                        nodeData[int(nodeId[2:])] = nodeName

                    graph.add_node(int(nodeId[2:]))

    print "[Weighted Graph Creator]  Read filename %s, skipped %d lines" %\
          (filename, skipped)
    print "[Weighted Graph Creator]  Graph has %d nodes and %d edges" %\
          (graph.number_of_nodes(), graph.number_of_edges())
    print "[Weighted Graph Creator]  Edges in edge list %d\n" % edges

    return graph, nodeData


### ---- EDGE LIST CREATION FUNCTIONS ---- ###

def createPlayerEdgeListFromDB(filename, seasons='all', leagues='all'):
    print "\n[Exporter]  Exporting player edge list"

    if(seasons != 'all'):
        seasonsString = ','.join(map(str, seasons))
    else:
        seasonsString = constants.allSeasonsString

    if(leagues != 'all'):
        leaguesString = ','.join(map(str, leagues))
    else:
        leaguesString = constants.allLeaguesString

    startTime = time.time()

    connection = connectToDB()

    try:
        file = open(filename, 'w')

        cursor = connection.cursor()

        cursor.execute('''
                        SELECT DISTINCT p.idP, p.idC, p.firstName, p.lastName, p.birthDate FROM player p
                        JOIN playerclubseason pcs USING (idP)
                        JOIN club c USING (idClub)
                        WHERE pcs.idS IN (%s) AND c.idL IN (%s)
                        GROUP BY idP
                       ''' %
                       (seasonsString, leaguesString))

        players       = cursor.fetchall()
        playerIdx     = 1
        numEdges      = 0
        playerList    = list()
        edgeList      = list()
        playerIndices = dict()
        # playerIndices dictionary will be used to map real player ids to consecutive ids for use in the network

        # get all player info
        cursor.execute('''
                        SELECT pcs.idP, pcs.idS, pcs.idClub, p.birthDate, pcs.playerValue, p.birthDate, p.playingPosition
                        FROM playerclubseason pcs
                        JOIN player p USING (idP)
                        JOIN club c USING (idClub)
                        WHERE pcs.idS IN (%s) AND c.idL IN (%s)
                        ORDER BY idP, idS
                       ''' %
                       (seasonsString, leaguesString))

        playersData = cursor.fetchall()
        playersInfo = dict()

        # rearange player info into a dict
        for playerData in playersData:
            seasonId         = int(playerData[1])
            currentPlayerIdx = int(playerData[0])

            if(not playersInfo.has_key(currentPlayerIdx)):
                playersInfo[currentPlayerIdx] = dict()

            playersInfo[currentPlayerIdx][seasonId] = playerData

        # save all the player IDs, their names and age to a list of strings
        for player in players:
            if(player[0] > 0):
                playerIndices[player[0]] = playerIdx
                playerAge                = date.today().year - player[4]

                try:
                    playerName = unicode(" ".join([player[2] , player[3]])).encode('latin-1').replace('"', '')
                except:
                    playerName  = " ".join([player[2] , player[3]]).replace('"', '')

                playerList.append("# %d \"%s\" %d\n" % (playerIdx, playerName, playerAge))

                playerIdx += 1

        # save adjacency list to a list of strings
        for player in players:
            playerId = player[0]

            if(playerId > 0):
                # get all the clubs this player played for in a specific season (playerClubSeason - by playerID)
                cursor.execute('''
                                SELECT pcs.idClub, pcs.idS
                                FROM playerclubseason pcs
                                JOIN club c USING (idClub)
                                WHERE pcs.idP = %s AND pcs.idS IN (%s) AND c.idL IN (%s)
                               ''' %
                               (playerId, seasonsString, leaguesString))

                clubsBySeasons = cursor.fetchall()


                # link all the players from all the clubs to the current player
                linkedPlayerIds = list()
                for clubBySeason in clubsBySeasons:
                    cursor.execute('''
                                    SELECT pcs.idP
                                    FROM playerclubseason pcs
                                    WHERE pcs.idClub = ? AND pcs.idS = ?
                                   ''',
                                   clubBySeason[0], clubBySeason[1])

                    playersInClubInSeason = cursor.fetchall()

                    for playerInClubSeason in playersInClubInSeason:
                        linkedPlayerIds.append(playerInClubSeason[0])

                for linkedPlayer in linkedPlayerIds:
                    if(linkedPlayer > 0):
                        if playerIndices[playerId] < playerIndices[linkedPlayer]:
                            playerId1 = playerIndices[playerId]
                            playerId2 = playerIndices[linkedPlayer]
                            weight    = calculatePlayersWeight(playerId, linkedPlayer, playersInfo)

                            edgeList.append("%s %s %f\n" % (playerId1, playerId2, weight))
                            numEdges += 1

        # output starting comments - number of nodes and edges, format
        # output player list
        # output edge list
        cursor.execute('''
                        SELECT COUNT(DISTINCT p.idP)
                        FROM player p
                        JOIN playerclubseason pcs USING (idP)
                        JOIN club c USING (idClub)
                        WHERE pcs.idS IN (%s) AND c.idL IN (%s)
                       ''' %
                       (seasonsString, leaguesString))

        numNodes = cursor.fetchone()

        file.write("# 'FootNetPlayer' undirected weighted network\n")
        file.write("# %d nodes and %d edges\n" % (numNodes[0], numEdges))
        file.write("# By Matevz Lenic & Matic Tribuson\n")

        for playerEntry in playerList:
            file.write(playerEntry)

        for edgeEntry in edgeList:
            file.write(edgeEntry)

    except Exception, e:
        print "[Exporter]  Exception occurred!", e
        traceback.print_exc()

    finally:
        endTime = time.time()
        print "[Exporter]  Edge list exported, time spent %f s\n" %\
              (endTime - startTime)

        connection.close()
        file.close()

    return playerIndices, playersInfo


def createClubEdgeListFromDB(filename, seasons='all', leagues='all',
                             weightedByClubValue=True, weightedByClubImportance=True):
    print "\n[Exporter]  Exporting club transfer edge list"

    if(seasons != 'all'):
        seasonsString = ','.join(map(str, seasons))
    else:
        seasonsString = constants.allSeasonsString

    if(leagues != 'all'):
        leaguesString = ','.join(map(str, leagues))
    else:
        leaguesString = constants.allLeaguesString

    startTime = time.time()

    connection = connectToDB()

    try:
        file = open(filename, 'w')

        cursor = connection.cursor()

        cursor.execute('''
                        SELECT c.idClub, c.nameClub
                        FROM club c
                        JOIN clubseason cs USING (idClub)
                        WHERE cs.idS IN (%s) AND c.idL IN (%s)
                        GROUP BY idClub
                        ORDER BY idClub
                       ''' %
                       (seasonsString, leaguesString))

        clubs = cursor.fetchall()

        numEdges         = 0
        clubIdx          = 1
        clubList         = list()
        edgeList         = list()
        clubNames        = dict()
        clubsInfo        = dict()
        clubTransfersIn  = dict()
        clubTransfersOut = dict()
        clubIndices      = dict()
        # clubIndices dictionary will be used to map real ids to consecutive ids for use in the network

        for club in clubs:
            clubIndices[club[0]] = clubIdx

            clubsInfo[clubIdx] = dict()

            clubNames[club[0]]        = club[1]
            clubTransfersIn[club[0]]  = dict()
            clubTransfersOut[club[0]] = dict()

            for club2 in clubs:
                clubTransfersIn[club[0]][club2[0]]  = 0
                clubTransfersOut[club[0]][club2[0]] = 0

            clubIdx += 1


        # add club average value to clubsInfo
        cursor.execute('''
                        SELECT cs.idClub, c.idL, AVG(cs.value)
                        FROM clubseason cs
                        JOIN club c USING (idClub)
                        WHERE cs.value != -1 AND cs.idS IN (%s) AND c.idL IN (%s)
                        GROUP BY idClub
                        ORDER BY idClub, idS
                       ''' %
                       (seasonsString, leaguesString))

        clubValues = cursor.fetchall()

        for clubValue in clubValues:
            currentClubIdx = clubIndices[clubValue[0]]
            clubsInfo[currentClubIdx]['league']     = clubValue[1]
            clubsInfo[currentClubIdx]['importance'] = list()

            clubsInfo[currentClubIdx]['importance'].append(clubValue[2])

        # add club average ranking to clubsInfo
        cursor.execute('''
                        SELECT cs.idClub, AVG(cs.ranking)
                        FROM clubseason cs
                        JOIN club c USING (idClub)
                        WHERE cs.ranking != -1 AND cs.idS IN (%s) AND c.idL IN (%s)
                        GROUP BY idClub
                        ORDER BY idClub
                       ''' %
                       (seasonsString, leaguesString))

        clubRankings = cursor.fetchall()

        for clubRanking in clubRankings:
            currentClubIdx = clubIndices[clubRanking[0]]

            if('importance' not in clubsInfo[currentClubIdx]):
                clubsInfo[currentClubIdx]['importance'] = list()

            clubsInfo[currentClubIdx]['importance'].append(clubRanking[1])

        cursor.execute('''
                        SELECT pcs.idP, pcs.idClub, pcs.idS
                        FROM playerclubseason pcs
                        JOIN club c USING (idClub)
                        WHERE pcs.idS IN (%s) AND c.idL IN (%s)
                        ORDER BY idP, idS
                       ''' %
                       (seasonsString, leaguesString))

        playerClubSeasons = cursor.fetchall()

        for i in range(0, len(playerClubSeasons) - 1):
            playerId1 = playerClubSeasons[i][0]
            playerId2 = playerClubSeasons[i+1][0]
            clubId1   = playerClubSeasons[i][1]
            clubId2   = playerClubSeasons[i+1][1]

            if(playerId1 == playerId2 and clubId1 != clubId2):
                clubTransfersIn[clubId1][clubId2]  += 1
                clubTransfersOut[clubId2][clubId1] += 1

        for club in clubs:
            clubList.append("# %d \"%s\"\n" % (clubIndices[club[0]], club[1]))

        for clubInEntry1 in clubTransfersIn:
            for clubInEntry2 in clubTransfersIn:
                if(clubTransfersIn[clubInEntry1][clubInEntry2] != 0):
                    clubId1 = clubIndices[clubInEntry1]
                    clubId2 = clubIndices[clubInEntry2]

                    if(weightedByClubImportance):
                        clubImportance = calculateClubWeight(clubId2, clubsInfo, weightedByClubValue)
                    else:
                        clubImportance = 1

                    numOfTransfers = clubTransfersOut[clubInEntry1][clubInEntry2]

                    edgeList.append("%d %d %f\n" % (clubId1, clubId2, numOfTransfers * clubImportance))
                    numEdges += 1

        # output starting comments - number of nodes and edges, format
        # output player list
        # output edge list
        cursor.execute('''
                        SELECT COUNT(DISTINCT c.idClub)
                        FROM playerclubseason pcs
                        JOIN club c USING (idClub)
                        WHERE pcs.idS IN (%s) AND c.idL IN (%s)
                       ''' %
                       (seasonsString, leaguesString))

        numNodes = cursor.fetchone()

        file.write("# 'FootNetClub' directed weighted network\n")
        file.write("# %d nodes and %d edges\n" % (numNodes[0], numEdges))
        file.write("# By Matevz Lenic & Matic Tribuson\n")

        for clubEntry in clubList:
            file.write(clubEntry)

        for edgeEntry in edgeList:
            file.write(edgeEntry)

    except Exception, e:
        print "[Exporter]  Exception occurred!", e
        traceback.print_exc()

    finally:
        endTime = time.time()
        print "[Exporter]  Edge list exported, time spent %f s\n" %\
              (endTime - startTime)

        connection.close()
        file.close()


### ---- NETWORK ANALYSIS FUNCTIONS ---- ###

def calculatePageRank(graph):
    print "\n[PageRank calculator]  calculating PageRank scores"

    startTime  = time.time()
    ranking    = dict()
    newRanking = dict()

    # set all ranking to 1
    for node in graph.nodes():
        ranking[node] = 1

    iterations = 0

    # TODO: run until convergence...
    while iterations < 30:
        if(iterations % 10 == 0):
            print "[PageRank calculator]  Iteration %d" % iterations

        sum = 0

        for i in graph.nodes():
            value = 0
            for j in graph.neighbors(i):
                value += 0.85 * ranking[j] / graph.degree(j)

            sum += value
            newRanking[i] = value

        for k in graph.nodes():
            ranking[k] = ranking[k] + (1.0 - sum) / graph.number_of_nodes()

        ranking = newRanking

        iterations += 1

    endTime = time.time()
    print "[PageRank calculator]  PageRank calculation done, time spent: %f s\n" %\
          (endTime - startTime)

    return ranking


def calculateBetweennessCentrality(graph):
    print "\n[Betweenness calculator]  calculating Betweenness scores"

    startTime  = time.time()
    N          = graph.number_of_nodes() + 1
    cb         = dict()

    # initialize cb to zero
    for i in range(1, N):
        cb[i] = 0

    for node in graph.nodes():
        if(node % 500 == 0):
            print "[Betweenness calculator]  Processed %d nodes" % (node)

        S = list()
        P = list()
        Q = deque()

        sigma = dict()
        d     = dict()

        Q.append(node)

        # initialize structures for each node
        for i in range(1, N):
            P.append(list())
            sigma[i] = 0
            d[i]     = -1

        # just append another empty list because nodes start with 1
        # we will never use P[0] but that's fine
        P.append(list())

        sigma[node] = 1
        d[node]     = 0

        while len(Q) > 0:
            v = Q.popleft()
            S.append(v)

            for neighbor in graph.neighbors(v):
                # has neighbor been traversed before?
                if(d[neighbor] < 0):
                    Q.append(neighbor)
                    d[neighbor] = d[v] + 1

                # is shortest path to neighbor through v?
                if(d[neighbor] == d[v] + 1):
                    sigma[neighbor] += sigma[v]
                    P[neighbor].append(v)

        delta = dict()
        for i in range(1, N):
            delta[i] = 0

        while len(S) > 0:
            w = S.pop()
            for v in P[w]:
                delta[v] += (sigma[v] / float(sigma[w])) * (1 + delta[w])
                if(w != node):
                    cb[w] += delta[w]

    endTime = time.time()
    print "[Betweenness calculator]  Betweenness calculation done, time spent: %f s\n" %\
          (endTime - startTime)

    return cb


def calculateWeightedBetweennessCentrality(graph):
    print "\n[Weighted Betweenness calculator]  calculating weighted Betweenness scores"

    startTime = time.time()
    N         = graph.number_of_nodes() + 1
    cb        = dict()

    # initialize cb to zero
    for i in range(1, N):
        cb[i] = 0

    for node in graph.nodes():
        if(node % 500 == 0):
            print "[Weighted Betweenness calculator]  Processed %d nodes" % (node)

        S = list()
        P = list()
        Q = deque()

        sigma = dict()
        d     = dict()

        Q.append(node)

        # initialize structures for each node
        for i in range(1, N):
            P.append(list())
            sigma[i] = 0
            d[i]     = -1

        # just append another empty list because nodes start with 1
        # we will never use P[0] but that's fine
        P.append(list())

        sigma[node] = 1
        d[node]     = 0

        while len(Q) > 0:
            v = Q.popleft()
            S.append(v)

            for neighbor in graph.neighbors(v):
                weight = graph[v][neighbor]['weight']

                # has neighbor been traversed before?
                if(d[neighbor] < 0):
                    Q.append(neighbor)
                    # add inverse of price of the edge between neighbor and v
                    # inverse because higher weight here is better
                    if(weight != 0):
                        d[neighbor] = d[v] + (1.0 / weight)
                    else:
                        d[neighbor] = d[v] + constants.noWeightPathPenalty

                if(weight != 0):
                    shortestPath = d[v] + (1.0 / weight)
                else:
                    shortestPath = d[v] + constants.noWeightPathPenalty

                # is shortest path to neighbor through v?
                if(d[neighbor] == shortestPath):
                    sigma[neighbor] += sigma[v]
                    P[neighbor].append(v)

        delta = dict()
        for i in range(1, N):
            delta[i] = 0

        while len(S) > 0:
            w = S.pop()
            for v in P[w]:
                delta[v] += (sigma[v] / float(sigma[w])) * (1 + delta[w])
                if(w != node):
                    cb[w] += delta[w]

    endTime = time.time()
    print "[Weighted Betweenness calculator]  Weighted Betweenness calculation done, time spent: %f s\n" %\
          (endTime - startTime)

    return cb


def calculateBridgenessCentrality(graph):
    print "\n[Bridgeness calculator]  calculating weighted Bridgeness scores"

    startTime = time.time()
    N         = graph.number_of_nodes() + 1
    cb        = dict()

    # initialize cb to zero
    for i in range(1, N):
        cb[i] = 0

    for node in graph.nodes():
        sp = nx.shortest_path_length(graph, node)

        if(node % 500 == 0):
            print "[Bridgeness calculator]  Processed %d nodes" % (node)

        S = list()
        P = list()
        Q = deque()

        sigma = dict()
        d     = dict()

        Q.append(node)

        # initialize structures for each node
        for i in range(1, N):
            P.append(list())
            sigma[i] = 0
            d[i]     = -1

        # just append another empty list because nodes start with 1
        # we will never use P[0] but that's fine
        P.append(list())

        sigma[node] = 1
        d[node]     = 0

        while len(Q) > 0:
            v = Q.popleft()
            S.append(v)

            for neighbor in graph.neighbors(v):
                # has neighbor been traversed before?
                if(d[neighbor] < 0):
                    Q.append(neighbor)
                    d[neighbor] = d[v] + 1

                # is shortest path to neighbor through v?
                if(d[neighbor] == d[v] + 1):
                    sigma[neighbor] += sigma[v]
                    P[neighbor].append(v)

        delta = dict()
        for i in range(1, N):
            delta[i] = 0

        while len(S) > 0:
            w = S.pop()
            for v in P[w]:
                delta[v] += (sigma[v] / float(sigma[w])) * (1 + delta[w])
                if(sp[w] > 1):
                    cb[w] += delta[w]

    endTime = time.time()
    print "[Bridgeness calculator]  Bridgeness calculation done, time spent: %f s\n" %\
          (endTime - startTime)

    return cb