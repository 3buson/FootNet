__author__ = 'Matevz Lenic'

import pyodbc

import utils

class ClubSeason:

    def __init__(self, idS=None, idClub=None, ranking=None, value=None):
        self.idS     = idS
        self.idClub  = idClub
        self.ranking = ranking
        self.value   = value

    def dbInsert(self):
        connection = utils.connectToDB()
        cursor     = connection.cursor()

        try:
            cursor.execute("INSERT IGNORE INTO clubseason(idS,idClub,ranking,value) VALUES (?, ?, ?, ?)",
                       self.idS, self.idClub, self.ranking, self.value)

        except pyodbc.DatabaseError, e:
            print "ERROR - DatabaseError", e
            pass

        connection.commit()