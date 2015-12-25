__author__ = 'Matevz Lenic'

from pyquery import PyQuery as pq
import time
import sys
import re
import os

sys.path.insert(0, '../')
import constants
import utils

from Club import Club
from Player import Player
from Season import Season
from ClubSeason import ClubSeason
from PlayerClubSeason import PlayerClubSeason

def parseFile(filename, league, season):
    document = pq(filename=filename)

    # check if club squad table is present
    if(len(document(".items")) < 1):
        print "Club squad not available"
        return

    clubId          = filename.split("_",2)[1]
    clubValue       = 0
    playersInserted = 0

    club          = Club()
    club.idClub   = clubId
    club.idL      = constants.leagueIds[league]
    club.nameClub = document(".spielername-profil").html().strip()

    club.dbInsert()

    # parse club ranking
    if(season != constants.currentSeason):
        htmlString = open(filename).read().replace('\t', '')
        standing = re.search(r"(.*)Platz", htmlString).group(1)[:-2]
    else:
        standing = 0

    # parse players table
    for i in document(document(document(".items")[0]).children()[1]).children().items():
        player = Player()
        pcs    = PlayerClubSeason()
        idx    = 0

        playerExists      = False
        playerObjectValid = True

        # check if player is already in the DB
        playerId = pq(i.children()[1])(".spielprofil_tooltip").attr('id')

        if(utils.checkIfPlayerExists(playerId)):
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
                    position = pq(column).attr('title')

                    if(position == 'Torwart' or position == 'Goalkeeper'):
                        player.playingPosition = 'GK'
                    elif(position == 'Abwehr' or position == 'Defence'):
                        player.playingPosition = 'DEF'
                    elif(position == 'Mittelfeld' or position == 'Midfield'):
                        player.playingPosition = 'MID'
                    elif(position == 'Sturm' or position == 'Striker'):
                        player.playingPosition = 'ATT'
                    else:
                        player.playingPosition = 'UNK'

                    playingNumber = pq(column).children().html()

                    # if player does not have a number exclude him from the parsing
                    if playingNumber != '-':
                        player.playingNumber = int(playingNumber)
                    else:
                        playerObjectValid = False
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

                    clubValue += price

                    pcs.playerValue = price

            if(playerObjectValid):
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

            clubValue += price

            pcs.playerValue = price

        cs         = ClubSeason()
        cs.idClub  = clubId
        cs.idS     = int(season)
        cs.ranking = int(standing)
        cs.value   = clubValue

        cs.dbInsert()
        pcs.dbInsert()

        # cleanup
        del player
        del pcs
        del cs

    del club

    print "Inserted %d new player(s)" % playersInserted

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
# filename = "../FileGetter/html/LaLiga/14/VCF_1049"
# parseFile(filename, 'LaLiga', '14')