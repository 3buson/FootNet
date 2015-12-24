__author__ = 'Matevz Lenic'

from pyquery import PyQuery as pq
import lxml
import time
import os

import sys
sys.path.insert(0, '../')
import constants
import utils

from Player import Player
from Club import Club
from PlayerClubSeason import PlayerClubSeason
from ClubSeason import ClubSeason
from Season import Season

def parseFile(filename, league, season):
    document = pq(filename=filename)

    playersInserted = 0

    club          = Club()
    club.idClub   = filename.split("_",2)[1]
    club.idL      = constants.leagueIds[league]
    club.nameClub = document(".spielername-profil").html().strip()

    club.dbInsert()

    for i in document(document(document(".items")[0]).children()[1]).children().items():
        player = Player()
        pcs    = PlayerClubSeason()
        idx    = 0

        playerExists = False

        # check if player is already in the DB
        id = pq(i.children()[1])(".spielprofil_tooltip").attr('id')

        if(utils.checkIfPlayerExists(id)):
            playerExists = True

        pcs.idS    = int(season)
        pcs.idClub = club.idClub

        if(not playerExists):
            for j in range(0,len(i.children())):
                column = i.children()[j]

                if (str(pq(i.children()[2]).attr('class')) == "hide"):
                    prevClubPresent = False
                else:
                    prevClubPresent = True

                # Playing Number and Position
                if idx == 0:
                    player.playingPosition = pq(column).attr('title')

                    playingNumber = pq(column).children().html()

                    # if player does not have a number exclude him from the parsing
                    if playingNumber != '-':
                        player.playingNumber = int(playingNumber)
                    else:
                        break

                    pcs.playerNumber = playingNumber

                    idx += 1
                    continue

                # Player Name and ID
                if idx == 1:
                    nameElement = pq(column)(".spielprofil_tooltip")
                    names       = nameElement.attr('title').split(" ")
                    id          = nameElement.attr('id')

                    pcs.idP          = int(id)
                    player.idP       = int(id)
                    player.firstName = names[0]
                    if len(names) > 1:
                        player.lastName = " ".join(names[1:len(names)])

                    idx += 1
                    continue

                # Birth date (only if not current season)
                if idx == 2:
                    if(prevClubPresent) and not playerExists:
                        age = pq(column).html().split(" ")
                        player.birthDate = int(pq(column).html().split(" ")[2])

                        idx += 1
                        continue
                    else:
                        idx += 1
                        continue

                # Player nationality / birth date
                if idx == 3:
                    if(not playerExists):
                        if(prevClubPresent):
                            flagElement = pq(pq(column).html())

                            # check for multiple nationality
                            if len(flagElement.children()) > 0:
                                nationality = flagElement.children().attr('title')
                            else:
                                nationality = flagElement.attr('title')

                            player.nationality = nationality
                        else:
                            player.birthDate = int(pq(column).html().split(" ")[2])

                    idx += 1
                    continue

                # Player nationality (only if current season)
                if (idx == 4):
                    if(not prevClubPresent and not playerExists):
                        flagElement = pq(pq(column).html())

                        # check for multiple nationality
                        if len(flagElement.children()) > 0:
                            nationality = flagElement.children().attr('title')
                        else:
                            nationality = flagElement.attr('title')

                        player.nationality = nationality

                    idx += 1
                    continue

                # Player market value
                if (idx == 5):
                    priceString = "0"
                    multiplier  = 1

                    for character in pq(column).html().split("<")[0]:
                        if(character.isdigit() or character == '.' or character == ','):
                            priceString += character
                        elif(character == 'm'):
                            multiplier = 1000000
                        elif(character == 'k'):
                            multiplier = 1000

                    price = float(priceString) * multiplier

                    pcs.playerValue = price

            # player.to_string()
            player.dbInsert()

            playersInserted += 1

        else:
            # parse only player market value
            priceString = "0"
            multiplier  = 1

            for character in pq(i.children()[5]).html().split("<")[0]:
                if(character.isdigit() or character == '.' or character == ','):
                    priceString += character
                elif(character == 'm'):
                    multiplier = 1000000
                elif(character == 'k'):
                    multiplier = 1000

            price = float(priceString) * multiplier

            pcs.playerValue = price

        pcs.dbInsert()

        # cleanup
        del player
        del pcs

    del club

    print "Inserted %d new player(s)" % playerExists

# --- PARSE ALL FILES IN A DIRECTORY --- #
rootDirectory = "../FileGetter/html/"

for dirname1, dirnames1, filenames1 in os.walk(rootDirectory):
    # loop through leagues
    for leagueDirectory in dirnames1:
        currentDirectory1 = os.path.join(dirname1, leagueDirectory)
        for dirname2, dirnames2, filenames2 in os.walk(currentDirectory1):
            # loop through seasons
            for seasonDirectory in dirnames2:
                currentDirectory2 = os.path.join(currentDirectory1, seasonDirectory)
                # loop through clubs
                for filename in os.listdir(currentDirectory2):
                    print "Parsing file %s, legue: %s, season: %s..." %\
                          (filename, leagueDirectory, seasonDirectory)

                    startTime = time.time()
                    parseFile(currentDirectory2 + '/' + filename, leagueDirectory, seasonDirectory)
                    endTime = time.time()

                    print "Parsed file %s, legue: %s, season: %s | Time spent %f s" %\
                          (filename, leagueDirectory, seasonDirectory, (endTime - startTime))

                print "\nParsed season %s, league: %s\n" % (seasonDirectory, leagueDirectory)

        print "\nParsed all seasons for league %s\n" % leagueDirectory


# --- PARSE ONE FILE ONLY --- #
# filename = "../FileGetter/html/LaLiga/15/VCF_1049"
# parseFile(filename, 'LaLiga', '15')