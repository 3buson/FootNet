__author__ = 'Matevz Lenic'

import pyodbc

import utils

class PlayerClubSeason:

    def __init__(self, idP=None, idClub=None, idS=None, playerValue=None, playerNumber=None):
        self.idP          = idP
        self.idClub       = idClub
        self.idS          = idS
        self.playerValue  = playerValue
        self.playerNumber = playerNumber

    def dbInsert(self):
        connection = utils.connectToDB()
        cursor     = connection.cursor()

        try:
            cursor.execute("INSERT IGNORE INTO playerclubseason(idP,idClub,idS,playerValue,playerNumber) VALUES (?, ?, ?, ?, ?)",
                       self.idP, self.idClub, self.idS, self.playerValue, self.playerNumber)
        except pyodbc.DatabaseError, e:
            print "ERROR - DatabaseError", e
            pass

        connection.commit()