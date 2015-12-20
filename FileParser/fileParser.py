__author__ = 'Matevz Lenic'

from pyquery import PyQuery as pq
import lxml
import os
from Player import Player
from Club import Club
from PlayerClubSeason import PlayerClubSeason
from ClubSeason import ClubSeason


def parseFile(filename, season):
    document = pq(filename=filename)
    club = Club()
    club.idClub = filename.split("_",2)[1]
    club.nameClub = document(".spielername-profil").html().strip()

    for i in document(document(document(".items")[0]).children()[1]).children().items():
        player = Player()
        pcs    = PlayerClubSeason()
        idx    = 0

        for j in range(0,len(i.children())):
            column = i.children()[j]

            if (str(pq(i.children()[2]).attr('class')) == "hide"):
                prevClubPresent = False
            else:
                prevClubPresent = True

            # Playing Position
            if idx == 0:
                player.playingPosition = pq(column).attr('title')

                playingNumber = pq(column).children().html()

                # if player does not have a number exclude him from the parsing
                if playingNumber != '-':
                    player.playingNumber   = int(playingNumber)
                else:
                    break


                idx += 1
                continue

            # Player Name and ID
            if idx == 1:
                nameElement = pq(column)(".spielprofil_tooltip")
                names       = nameElement.attr('title').split(" ")
                id          = nameElement.attr('id')

                player.idP       = int(id)
                player.firstName = names[0]
                if len(names) > 1:
                    player.lastName = " ".join(names[1:len(names)])

                idx += 1
                continue

            # Birth date (only if not current season)
            if idx == 2:
                print prevClubPresent
                if(prevClubPresent):
                    age = pq(column).html().split(" ")
                    player.birthDate = int(pq(column).html().split(" ")[2])

                    idx += 1
                    continue
                else:
                    idx += 1
                    continue

            # Player nationality / birth date
            if idx == 3:
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
                if(not prevClubPresent):
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
                priceString = ""
                addNum = False
                for character in pq(column).html().split("<")[0]:
                    if(character.isdigit() or character == '.' or character == ','):
                        priceString += character
                    elif(character == 'm'):
                        multiplier = 1000000
                    elif(character == 'k'):
                        multiplier = 1000

                price = float(priceString) * multiplier
                print price

        player.to_string()


# --- PARSE ALL FILES IN A DIRECTORY --- #

rootDirectory = "../FileGetter/html/"

for dirname, dirnames, filenames in os.walk(rootDirectory):
    # loop through leagues
    for leagueDirectory in dirnames:
        currentDirectory = os.path.join(dirname, leagueDirectory)
        for dirname1, dirnames1, filenames1 in os.walk(currentDirectory):
            # loop through seasons
            for seasonDirectory in dirnames1:
                currentDirectory1 = os.path.join(currentDirectory, seasonDirectory)
                # loop through clubs
                for filename in os.listdir(currentDirectory1):
                    parseFile(filename, seasonDirectory)