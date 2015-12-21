__author__ = 'Matevz Lenic'
import pyodbc

class Club:

    def __init__(self, idClub=None, idL=None, nameClub=None):
        self.idClub = idClub
        self.idL = idL
        self.nameClub = nameClub

    def dbInsert(self):
        cnxn = pyodbc.connect('DSN=FootNet')
        cursor = cnxn.cursor()
        try:
            cursor.execute("INSERT IGNORE INTO club(idClub,idL,nameClub) VALUES (?, ?, ?)",
                       self.idC, self.idL, self.nameClub)
        except pyodbc.DatabaseError:
            print "ERROR"
            pass

        cnxn.commit()