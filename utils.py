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
    file       = open(filename, 'w')
    connection = connectToDB(constants.databaseString)

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM player")

        players       = cursor.fetchall()
        playerIdx     = 1
        playerIndices = dict()
        # playerIndices dictionary will be used to map real player ids to consecutive ids for use in the network

        # output all the player IDs and their names
        for player in players:
            playerIndices[player[0]] = playerIdx
            file.write("# %d \"%s\"", playerIdx, "".join(player[1], player[2]))

            playerIdx += 1

        # output adjacency list
        for player in players:
            playerId = player[0]

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
                file.write("%s %s", playerIndices[playerId], playerIndices[linkedPlayer])


    except Exception, e:
        print "Exception occurred!", e

    finally:
        file.close()