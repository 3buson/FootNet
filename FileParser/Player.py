__author__ = 'Matevz Lenic'

import pyodbc

import utils
import constants

class Player:

    def __init__(self, idP=0, nationality="", firstName="", lastName="",
                 birthDate=0, playingPosition=0, playingNumber=0, height=None):
        self.idP             = idP
        self.nationality     = nationality
        self.firstName       = firstName
        self.lastName        = lastName
        self.birthDate       = birthDate
        self.playingPosition = playingPosition
        self.playingNumber   = playingNumber
        self.height          = height

    def to_string(self):
        print "idP - %d;\nnationality - %s;\nfirstName - %s;\nlastName - %s;\n" \
              "birthdate - %d;\nplayingPosition - %s;\nplayingNumber - %d\n" % \
              (self.idP, self.nationality, self.firstName, self.lastName,
               self.birthDate, self.playingPosition, self.playingNumber)


    def dbInsert(self, connection):
        cursor = connection.cursor()

        countriesDict = utils.getCountriesDics()

        if(self.nationality == ''):
            self.nationality = 'Unknown'

        if(countriesDict.has_key(self.nationality)):
            idC = countriesDict[self.nationality]
        else:
            idC = countriesDict['Unknown']

        try:
            cursor.execute("INSERT IGNORE INTO player(idP, idC, firstName, lastName, birthDate, playingPosition, playingNumber, height) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       self.idP, idC, self.firstName, self.lastName, self.birthDate, self.playingPosition, self.playingNumber, self.height)

        except pyodbc.DatabaseError, e:
            print "[Player class]  ERROR - DatabaseError", e
            pass

        connection.commit()