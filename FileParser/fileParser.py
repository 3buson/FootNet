__author__ = 'Matevz Lenic'

from pyquery import PyQuery as pq
import lxml
from Player import Player
from Club import Club
from PlayerClubSeason import PlayerClubSeason
from ClubSeason import ClubSeason

filename = "../FileGetter/html/LaLiga/15/VCF_1049"

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
            player.playingNumber   = int(pq(column).children().html())
            idx += 1
            continue

        # Player Name
        if idx == 1:
            nameElement = pq(column)(".spielprofil_tooltip")
            names       = nameElement.attr('title').split(" ")

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
    # break
