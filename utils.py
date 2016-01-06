__author__ = 'matic'

import time
import pyodbc
import networkx as nx
from datetime import date
from collections import deque

import constants

def connectToDB():
    connection = None

    while connection is None:
        try:
            connection = pyodbc.connect('DSN=FootNet')

        except Exception, e:
            print "Error connecting to database. Trying again in 1 sec !", e

        time.sleep(1)

    return connection


def calculatePlayersWeight(playerId1, playerId2, playersInfo):
    weight         = 0
    inflationRatio = 2.11 / 100 # average inflation ratio per year (percent)


    if(len(playersInfo[playerId1]) > len(playersInfo[playerId2])):
        playedMoreSeasons = playerId1
        playedLessSeasons = playerId2
    else:
        playedMoreSeasons = playerId2
        playedLessSeasons = playerId1


    for currentSeason in playersInfo[playedLessSeasons]:
        if(playersInfo[playedMoreSeasons].has_key(currentSeason)):
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

                weight += (playerValue1 + playerValue2) / 1000000.0

    return weight


def createPlayerEdgeListFromDB(filename):
    print "Exporting edge list"

    startTime = time.time()

    connection = connectToDB()

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM player")

        players       = cursor.fetchall()
        playerIdx     = 1
        numNodes      = 0
        numEdges      = 0
        playerIndices = dict()
        playerList    = list()
        edgeList      = list()
        # playerIndices dictionary will be used to map real player ids to consecutive ids for use in the network

        # get all player info
        cursor.execute("SELECT pcs.idP, pcs.idS, pcs.idClub, p.birthDate, pcs.playerValue FROM footballnetwork.playerclubseason pcs JOIN player p USING (idP) ORDER BY idP, idS")
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
                playerAge = date.today().year - player[4]
                playerIndices[player[0]] = playerIdx
                playerList.append("# %d \"%s\" %d\n" % (playerIdx, " ".join([str(player[2]) , str(player[3])]), playerAge))

                playerIdx += 1

        # save adjacency list to a list of strings
        for player in players:
            playerId = player[0]

            if(playerId > 0):
                # get all the clubs this player played for in a specific season (playerClubSeason - by playerID)
                cursor.execute("SELECT pcs.idClub, pcs.idS FROM playerclubseason pcs WHERE pcs.idP = ? ", playerId)
                clubsBySeasons = cursor.fetchall()

                # link all the players from all the clubs to the current player
                linkedPlayerIds = list()
                for clubBySeason in clubsBySeasons:
                    cursor.execute("SELECT pcs.idP FROM playerclubseason pcs WHERE pcs.idClub = ? AND pcs.idS = ?", clubBySeason[0], clubBySeason[1])
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
        cursor.execute("SELECT COUNT(idP) FROM footballnetwork.player")
        numNodes = cursor.fetchone()

        file = open(filename, 'w')
        file.write("# 'FootNet' undirected weighted network\n")
        file.write("# %d nodes and %d edges\n" % (numNodes[0], numEdges))
        file.write("# By Matevz Lenic & Matic Tribuson\n")

        for playerEntry in playerList:
            file.write(playerEntry)

        for edgeEntry in edgeList:
            file.write(edgeEntry)

    except Exception, e:
        print "Exception occurred!", e

    finally:
        endTime = time.time()
        print "Edge list exported, time spent %f s" % (endTime - startTime)
        file.close()


def getCountriesDics():
    cDict = dict()

    try:
        connection = connectToDB()
        cursor     = connection.cursor()

        cursor.execute("SELECT * from countries")
        result = cursor.fetchall()

        for resultRow in result:
            cDict[resultRow[1]] = resultRow[0]

    except pyodbc.DatabaseError, e:
        print "ERROR - DatabaseError", e
        pass

    finally:
        return cDict


def checkIfPlayerExists(connection, playerId):
    exists = False

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * from player WHERE idP = ?", playerId)
        result = cursor.fetchall()

        if(len(result) > 0):
            exists = True

    except pyodbc.DatabaseError, e:
        print "ERROR - DatabaseError", e
        pass

    finally:
        return exists


def calculatePageRank(graph):
    ranking    = dict()
    newRanking = dict()

    # set all ranking to 1
    for node in graph.nodes():
        ranking[node] = 1

    iterations = 0

    while iterations < 50:
        if(iterations % 10 == 0):
            print "Iteration %d" % iterations

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
    return ranking


def calculateBetweennessCentrality(graph):
    N = graph.number_of_nodes()

    cb = dict()

    # initialaze cb to zero
    for i in range(1, N):
        cb[i] = 0

    for node in graph.nodes():
        if(node % 500 == 0):
            print "Processed %d nodes" % (node)

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

    return cb


def calculateBridgenessCentrality(graph):
    N = graph.number_of_nodes()

    cb = dict()

    # initialaze cb to zero
    for i in range(1, N):
        cb[i] = 0

    for node in graph.nodes():
        sp = nx.shortest_path_length(graph, node)

        if(node % 500 == 0):
            print "Processed %d nodes" % (node)

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

    return cb


def createGraphFromEdgeList(filename):
    undirectedGraph = nx.Graph()

    with open(filename) as f:
        skipped = 0
        edges = 0
        for line in f:
            if(line[0] != '#'):
                edges += 1
                [node1, node2] = line.split()
                undirectedGraph.add_edge(int(node1), int(node2), weight=0)
            else:
                skipped += 1

    print "Read filename %s, skipped %d lines" %\
          (filename, skipped)
    print "Graph has %d nodes and %d edges" %\
          (undirectedGraph.number_of_nodes(), undirectedGraph.number_of_edges())
    print "Edges in edge list %d" % edges

    return undirectedGraph


def main():
    createPlayerEdgeListFromDB("FootNet.adj")

if __name__ == "__main__":
    main()
