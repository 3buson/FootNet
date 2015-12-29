__author__ = 'Matevz Lenic'

import pyodbc

import utils

class PlayerClubSeason:

    def __init__(self, idP=None, idClub=None, idS=None, playerValue=None, playerNumber=None, apps=None,
                 goals=None, assists=None, ownGoals=None, yellowCards=None, redCards=None, onSubs=None,
                 offSubs=None, penaltyGoals=None, minutesPerGoal=None, minutesPlayed=None):
        self.idP            = idP
        self.idClub         = idClub
        self.idS            = idS
        self.playerValue    = playerValue
        self.playerNumber   = playerNumber
        self.apps           = playerNumber
        self.goals          = playerNumber
        self.assists        = playerNumber
        self.ownGoals       = playerNumber
        self.yellowCards    = playerNumber
        self.redCards       = playerNumber
        self.onSubs         = playerNumber
        self.offSubs        = playerNumber
        self.penaltyGoals   = playerNumber
        self.minutesPerGoal = minutesPerGoal
        self.minutesPlayed  = minutesPlayed

    def dbInsert(self, connection):
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO playerclubseason(idP, idClub, idS, playerValue, playerNumber) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ON DUPLICATE KEY UPDATE",
                       self.idP, self.idClub, self.idS, self.playerValue, self.playerNumber, self.apps,
                       self.goals, self.assists, self.ownGoals, self.yellowCards, self.redCards, self.onSubs,
                       self.offSubs, self.penaltyGoals, self.minutesPerGoal, self.minutesPlayed)

        except pyodbc.DatabaseError, e:
            print "ERROR - DatabaseError", e
            pass

        connection.commit()