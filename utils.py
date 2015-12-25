__author__ = 'matic'

import time
import pyodbc

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

def createPlayerEdgeListFromDB(filename):
    print "Exporting edge list"

    startTime = time.time()

    file       = open(filename, 'w')
    connection = connectToDB()

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM player")

        players       = cursor.fetchall()
        playerIdx     = 1
        playerIndices = dict()
        # playerIndices dictionary will be used to map real player ids to consecutive ids for use in the network

        # output all the player IDs and their names
        for player in players:
            if(player[0] > 0):
                playerIndices[player[0]] = playerIdx
                file.write("# %d \"%s\"\n" % (playerIdx, " ".join([str(player[2]) , str(player[3])])))

                playerIdx += 1

        # output adjacency list
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
                            file.write("%s %s\n" % (playerIndices[playerId], playerIndices[linkedPlayer]))

    except Exception, e:
        print "Exception occurred!", e

    finally:
        endTime = time.time()
        print "Edge list exported, time spend %f s" % (endTime - startTime)
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

def checkIfPlayerExists(playerId):
    exists = False

    try:
        connection = connectToDB()
        cursor     = connection.cursor()

        cursor.execute("SELECT * from player WHERE idP = ?", playerId)
        result = cursor.fetchall()

        if(len(result) > 0):
            exists = True

    except pyodbc.DatabaseError, e:
        print "ERROR - DatabaseError", e
        pass

    finally:
        return exists


# createPlayerEdgeListFromDB("EPLLaLiga131415")
