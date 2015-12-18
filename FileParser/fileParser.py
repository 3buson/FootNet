__author__ = 'Matevz Lenic'

from pyquery import PyQuery as pq
import lxml
from Player import Player
from Club import Club
from PlayerClubSeason import PlayerClubSeason
from ClubSeason import ClubSeason

filename = "./html/EFC_29_14.html"

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

        if idx == 0:
            player.playingPosition  =    pq(column).attr('title')
            player.playingNumber    =    int(pq(column).children().html())
            idx += 1
            continue
        if idx == 1:
            nameElement =   d(".spielprofil_tooltip")
            names =         d(".spielprofil_tooltip").html().split(" ")
            player.firstName = names[0]
            if len(names) > 1:
                player.lastName = " ".join(names[1:len(names)])
            idx += 1
            continue
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
        if idx == 3:
            if(prevClubPresent):
                player.nationality = pq(pq(column).html()).attr('title')
            else:
                player.birthDate = int(pq(column).html().split(" ")[2])
            idx += 1
            continue
        if (idx == 4):
            if(not prevClubPresent):
                player.nationality = pq(pq(column).html()).attr('title')
                idx += 1
            continue
        #price
        if (idx == 5):
            priceString = ""
            addNum = False
            for let in pq(column).html().split("<")[0]:
                if(let == u'\xa3'):
                    addNum = True
                    continue
                else:
                    if(let != "m"):
                        priceString += let
        print float(priceString)
    player.to_string()
    break