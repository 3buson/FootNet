__author__ = 'Matevz Lenic'

from pyquery import PyQuery as pq
import lxml
from Player import Player
from Club import Club
from PlayerClubSeason import PlayerClubSeason
from ClubSeason import ClubSeason

filename = "../FileGetter/html/LaLiga/15/VCF_1049"

d = pq(filename=filename)
club = Club()
club.idClub = filename.split("_",2)[1]
club.nameClub = d(".spielername-profil").html().strip()

for i in d(d(d(".items")[0]).children()[1]).children().items():
    player = Player()
    pcs = PlayerClubSeason()
    idx = 0
    for j in range(0,len(i.children())):
        column = i.children()[j]
        print pq(column)
        if (str(pq(i.children()[2]).attr('class')) == "hide"):
            prevClubPresent = False
        else:
            prevClubPresent = True

        # Playing Position
        if idx == 0:
            player.playingPosition  =    pq(column).attr('title')
            player.playingNumber    =    int(pq(column).children().html())
            idx += 1
            continue

        # Player Name
        if idx == 1:
            nameElement =   d(".spielprofil_tooltip")
            names =         d(".spielprofil_tooltip").html().split(" ")
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
                player.nationality = pq(pq(column).html()).attr('title')
            else:
                player.birthDate = int(pq(column).html().split(" ")[2])
            idx += 1
            continue

        # Player nationality (only if current season)
        if (idx == 4):
            if(not prevClubPresent):
                player.nationality = pq(pq(column).html()).attr('title')
                idx += 1
            continue

        # Player market valuew
        if (idx == 5):
            priceString = ""
            addNum = False
            for let in pq(column).html().split("<")[0]:
                if(let.isdigit() or let == '.' or let == ','):
                    priceString += let
                elif(let == 'm'):
                    multiplier = 1000000
                elif(let == 'k'):
                    multiplier = 1000

            price = float(priceString) * multiplier
            print price

    player.to_string()
    break
