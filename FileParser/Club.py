__author__ = 'Matevz Lenic'

import pyodbc
import traceback


class Club:

    def __init__(self, idClub=None, idL=None, nameClub=None):
        self.idClub   = idClub
        self.idL      = idL
        self.nameClub = nameClub

    def dbInsert(self, connection):
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT IGNORE INTO club(idClub, idL, nameClub) "
                           "VALUES (?, ?, ?)",
                       self.idClub, self.idL, self.nameClub)
        except pyodbc.DatabaseError, e:
            print "[Club class]  ERROR - DatabaseError", e
            traceback.print_exc()

        connection.commit()