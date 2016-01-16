__author__ = 'matic'

import matplotlib.pyplot as plt
from random import shuffle
import sys
import os

sys.path.insert(0, '../')
import constants
import utils


def main():
    connection = utils.connectToDB()
    cursor     = connection.cursor()

    # type input
    inputType = raw_input('Do you want price fluctuation for a specific club (current squad) or for selected players? (Club/Players): ')
    byClubs   = (inputType.lower() == 'club')

    # players/club input
    if(not byClubs):
        playersInput  = raw_input('Please enter desired player IDs separated by comma: ')
        players       = playersInput.split(',')
        players       = [int(player) for player in players]
        playersString = ','.join(map(str, players))
    else:
        clubInput = raw_input('Please enter desired club ID: ')
        clubId    = int(clubInput)
        players   = []

    # seasons input
    seasonsInput = raw_input('Please enter desired seasons separated by comma (all for all of them): ')

    if(seasonsInput == 'all'):
        seasons       = constants.allSeasons[0:-1]
        lastSeason    = seasons[-1]
        seasons       = [int(season) + 2000 for season in seasons]
        seasonsString = constants.allSeasonsString
    else:
        seasons       = seasonsInput.split(',')
        lastSeason    = seasons[-1]
        seasonsString = ','.join(map(str, seasons))
        seasons       = [int(season) + 2000 for season in seasons]

    # filename input
    filename = raw_input("Please enter image filename: ")

    # 30 RGB colors for chart
    colors = constants.rgb30
    # mix them so similar colors will not represent players with similar value
    shuffle(colors)

    # scale RGB values to the [0, 1] interval
    for i in range(len(colors)):
        r, g, b   = colors[i]
        colors[i] = (r / 255.0, g / 255.0, b / 255.0)


    plotLength = 20 - max(0, (15 - (len(seasons) * 3)))
    plt.figure(figsize=(plotLength,14))

    # prepare the data
    playersDataDict    = dict()
    lastSeasonDataDict = dict()
    sortedPlayers      = list()
    playersNames       = dict()

    if(byClubs):
        cursor.execute("SELECT pcs.idP, pcs.idS, pcs.playerValue, p.firstName, p.lastName FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idP IN (SELECT idP FROM playerclubseason WHERE idS = %s AND idClub = %d) AND idS IN (%s) ORDER BY idP, idS"
                       % (lastSeason, clubId, seasonsString))
        playersData = cursor.fetchall()

        cursor.execute("SELECT DISTINCT pcs.idP, pcs.playerValue FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idP IN (SELECT idP FROM playerclubseason WHERE idS = ? AND idClub = ?) AND pcs.idS = ? ORDER BY playerValue",
                        lastSeason, clubId, lastSeason)
        lastSeasonData = cursor.fetchall()
    else:
        cursor.execute("SELECT pcs.idP, pcs.idS, pcs.playerValue, p.firstName, p.lastName FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idP IN (%s) AND pcs.idS IN (%s) ORDER BY idP, idS"
                         % (playersString, seasonsString))
        playersData = cursor.fetchall()

        cursor.execute("SELECT DISTINCT pcs.idP, pcs.playerValue, FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idS = %s AND pcs.idP IN (%s) ORDER BY playerValue"
                        % (lastSeason, playersString))
        lastSeasonData = cursor.fetchall()

    maxValue = 0

    for lastSeasonDataForPlayer in lastSeasonData:
        playerId = lastSeasonDataForPlayer[0]
        value    = lastSeasonDataForPlayer[1]

        sortedPlayers.append(playerId)

        if(value):
            value = float(value) / 1000000
        else:
            value = 0.0

        lastSeasonDataDict[playerId] = value

    for playerData in playersData:
        playerId  = playerData[0]
        seasonId  = playerData[1]
        value     = playerData[2]

        firstName = playerData[3]
        lastName  = playerData[4]

        if(byClubs):
            if(playerId not in players):
                players.append(playerId)

        if(not value or int(value) == -1):
            value = 0
        else:
            value = int(round(value))

        if(value > maxValue):
            maxValue = value

        if(playerId in playersDataDict.keys()):
            playersDataDict[playerId][seasons.index(seasonId + 2000)] = value
        else:
            playersDataDict[playerId] = [0] * len(seasons)

            playersDataDict[playerId][seasons.index(seasonId + 2000)] = value

        if(lastName):
            name = lastName
        else:
            name = firstName

        try:
            playerName = unicode(name, 'latin-1')
        except TypeError:
            playerName = name

        playersNames[playerId] = playerName


    # remove some plot frame lines
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    # limit the range of the plot to where the data is
    plt.xlim(seasons[0], seasons[len(seasons) - 1])

    valueMaximum   = int(round(maxValue))
    valueStep      = int(round(maxValue / 10))
    seasonsMinimum = seasons[0]
    seasonsMaximum = seasons[-1] + 1
    seasonsStep    = 1

    plt.yticks(range(0, valueMaximum, valueStep),
               [u"\xA3"  + str(x / 1000000) + " mil " for x in range(0, valueMaximum, valueStep)],
               fontsize=14)

    plt.xticks(range(seasonsMinimum, seasonsMaximum, seasonsStep),
               [str(x) for x in range(seasonsMinimum, seasonsMaximum, seasonsStep)],
               fontsize=14)

    # print tick lines across the plot
    for y in range(0, valueMaximum, valueStep):
        plt.plot(range(seasons[0], seasons[len(seasons) - 1] + 1),
                 [y] * len(range(seasons[0], seasons[len(seasons) - 1] + 1)),
                 "--", lw=0.5, color="black", alpha=0.3)

    # remove the tick marks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    positions        = list()
    displace         = maxValue / 40
    displaceCaptionY = maxValue / 15
    displaceCaptionX = (seasons[0] + seasons[-1]) / 2.0

    for idx, playerId in enumerate(sortedPlayers):
        # each line with different color
        plt.plot(seasons, playersDataDict[playerId],
                lw=2.5, color=colors[idx % len(colors)])

        value = playersDataDict[playerId][-1]
        posY  = int(round(value))

        # prevent overlapping text
        if(posY in positions):
            posY += displace

            while(posY in positions):
                posY += displace

        positions.append(posY)

        if(idx != len(sortedPlayers) - 1):
            nextPlayerValue = playersDataDict[sortedPlayers[idx + 1]][-1]
            if(posY > nextPlayerValue):
                positions.append(nextPlayerValue)

        plt.text(seasons[-1], posY, playersNames[playerId],
                 fontsize=14, color=colors[idx % len(colors)])


    caption = "Football players market value fluctuation through seasons %s-%s for club "\
              % (seasons[0], seasons[-1])

    if(byClubs):
        caption += filename

    plt.text(displaceCaptionX, -displaceCaptionY,
             caption, fontsize=20, ha="center")

    # check if directory 'Visualizations' exists and create it if necessary
    directory = 'Visualizations/ValuePlots'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # plt.show()
    plt.savefig(directory + '/' + filename + '.png')

if __name__ == "__main__":
    main()