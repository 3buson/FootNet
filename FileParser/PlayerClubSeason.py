__author__ = 'Matevz Lenic'

import pyodbc
import traceback

import utils

class PlayerClubSeason:

    def __init__(self, idP=None, idClub=None, idS=None, playerValue=None, playerNumber=None, apps=None, goals=None,
                 assists=None, ownGoals=None, yellowCards=None, redCards=None, onSubs=None, offSubs=None,
                 penaltyGoals=None, concededGoals=None, cleanSheets=None, minutesPerGoal=None, minutesPlayed=None):
        self.idP            = idP
        self.idClub         = idClub
        self.idS            = idS
        self.playerValue    = playerValue
        self.playerNumber   = playerNumber
        self.apps           = apps
        self.goals          = goals
        self.assists        = assists
        self.ownGoals       = ownGoals
        self.yellowCards    = yellowCards
        self.redCards       = redCards
        self.onSubs         = onSubs
        self.offSubs        = offSubs
        self.penaltyGoals   = penaltyGoals
        self.concededGoals  = concededGoals
        self.cleanSheets    = cleanSheets
        self.minutesPerGoal = minutesPerGoal
        self.minutesPlayed  = minutesPlayed

    def dbInsert(self, connection):
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT IGNORE INTO playerclubseason(idP, idClub, idS, playerValue, playerNumber, apps, goals, assists, ownGoals, yellowCards, redCards, onSubs, offSubs, penaltyGoals, concededGoals, cleanSheets, minutesPerGoal, minutesPlayed) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       self.idP, self.idClub, self.idS, self.playerValue, self.playerNumber, self.apps, self.goals,
                       self.assists, self.ownGoals, self.yellowCards, self.redCards, self.onSubs, self.offSubs,
                       self.penaltyGoals, self.concededGoals, self.cleanSheets, self.minutesPerGoal, self.minutesPlayed)

        except pyodbc.DatabaseError, e:
            print "[PlayerClubSeason class]  ERROR - DatabaseError", e
            traceback.print_exc()

            pass

        connection.commit()

    def dbUpdate(self, connection):
        cursor = connection.cursor()

        try:
            cursor.execute("UPDATE playerclubseason "
                           "SET apps=?, goals=?, assists=?, ownGoals=?, yellowCards=?, redCards=?, onSubs=?, offSubs=?, penaltyGoals=?, concededGoals=?, cleanSheets=?, minutesPerGoal=?, minutesPlayed=? "
                           "WHERE idP = ? AND idS = ?",
                       self.apps, self.goals, self.assists, self.ownGoals, self.yellowCards, self.redCards,
                       self.onSubs, self.offSubs, self.penaltyGoals, self.concededGoals,
                       self.cleanSheets, self.minutesPerGoal, self.minutesPlayed, self.idP, self.idS)

        except pyodbc.DatabaseError, e:
            print "[PlayerClubSeason class]  ERROR - DatabaseError", e
            traceback.print_exc()

            pass

        connection.commit()