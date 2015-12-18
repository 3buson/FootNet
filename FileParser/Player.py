__author__ = 'Matevz Lenic'

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

