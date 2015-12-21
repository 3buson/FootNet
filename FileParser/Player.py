__author__ = 'Matevz Lenic'
import pyodbc

class Player:

    def __init__(self, idP=0, nationality="", firstName="", lastName="", birthDate=0, playingPosition=0, playingNumber=0):
        self.idP = idP
        self.nationality = nationality
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.playingPosition = playingPosition
        self.playingNumber = playingNumber

    def to_string(self):
        print "idP - %d;\nnationality - %s;\nfirstName - %s;\nlastName - %s;\nbirthdate - %d;\nplayingPosition - %s;\nplayingNumber - %d\n" % \
              (self.idP, self.nationality, self.firstName, self.lastName, self.birthDate, self.playingPosition, self.playingNumber)


    def dbInsert(self):
        cnxn = pyodbc.connect('DSN=FootNet')
        cursor = cnxn.cursor()
        idC = self.getCId(self.nationality, cursor)
        #TODO: Mapping of playing positions
        try:
            cursor.execute("INSERT IGNORE INTO player(idP,idC,firstName,lastName,birthDate,playingPosition, playingNumber) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       self.idP, idC, self.firstName, self.lastName, self.birthDate, self.playingPosition, self.playingNumber)
        except pyodbc.DatabaseError:
            print "ERROR"
            pass

        cnxn.commit()

    def getCId(self, nat, cursor):
        try:
            cursor.execute("SELECT idC from countries WHERE nameCountry = ?" , nat)
            r = cursor.fetchone()
        except pyodbc.DatabaseError:
            print "ERROR"
            pass
        return r.idC