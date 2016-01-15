__author__ = 'matic'

import matplotlib.pyplot as plt
import pandas as pd
import sys

sys.path.insert(0, '../')
import constants
import utils


def main():
    connection = utils.connectToDB()
    cursor     = connection.cursor()

    inputType     = raw_input('Do you want price fluctuation for a specific club (current squad) or for selected players? (Club/Players): ')

    if(inputType.lower() == 'club'):
        byClubs = True
    else:
        byClubs = False

    if(not byClubs):
        playersInput  = raw_input('Please enter desired player IDs separated by comma: ')
        players       = playersInput.split(',')
        players       = [int(player) for player in players]
        playersString = ','.join(map(str, players))
    else:
        clubInput = raw_input('Please enter desired club ID: ')
        clubId    = int(clubInput)
        players   = []

    currentSeason = constants.currentSeason
    allSeasons    = constants.allSeasons[0:-1]
    allSeasons    = [season + 2000 for season in allSeasons]

    # 26 RGB colors for chart
    colors = constants.rgb26

    # scale RGB values to the [0, 1] interval
    for i in range(len(colors)):
        r, g, b   = colors[i]
        colors[i] = (r / 255.0, g / 255.0, b / 255.0)

    plt.figure(figsize=(12,14))

    # prepare the data
    playersDataDict    = dict()
    lastSeasonDataDict = dict()
    playersNames       = dict()

    if(byClubs):
        cursor.execute("SELECT pcs.idP, pcs.idS, pcs.playerValue, p.firstName, p.lastName FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idP IN (SELECT idP FROM playerclubseason WHERE idS = ? AND idClub = ?) ORDER BY idP, idS",
                         currentSeason, clubId)
        playersData = cursor.fetchall()

        cursor.execute("SELECT pcs.idP, pcs.playerValue FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idP IN (SELECT idP FROM playerclubseason WHERE idS = ? AND idClub = ?) AND pcs.idS = ? ORDER BY idP, idS",
                        currentSeason, clubId, currentSeason)
        lastSeasonData = cursor.fetchall()
    else:
        cursor.execute("SELECT pcs.idP, pcs.idS, pcs.playerValue, p.firstName, p.lastName FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idP IN (%s) ORDER BY idP, idS"
                         % playersString)
        playersData = cursor.fetchall()

        cursor.execute("SELECT pcs.idP, pcs.playerValue, FROM playerclubseason pcs JOIN player p USING (idP) WHERE pcs.idS = %s AND pcs.idP IN (%s) ORDER BY playerValue"
                        % (currentSeason, playersString))
        lastSeasonData = cursor.fetchall()

    maxValue = 0

    for lastSeasonDataForPlayer in lastSeasonData:
        playerId = lastSeasonDataForPlayer[0]
        value    = lastSeasonDataForPlayer[1]

        lastSeasonDataDict[playerId] = float(value) / 1000000

    for playerData in playersData:
        playerId  = playerData[0]
        seasonId  = playerData[1]
        value     = playerData[2]

        firstName = playerData[3]
        lastName  = playerData[4]

        if(byClubs):
            if(playerId not in players):
                players.append(playerId)

        # we want values in millions of pounds
        if(not value):
            value = 0
        else:
            value = float(value) / 1000000

        if(value > maxValue):
            maxValue = value

        if(playerId in playersDataDict.keys()):
            playersDataDict[playerId][seasonId - 1] = value
        else:
            playersDataDict[playerId] = [0] * 15

        playersNames[playerId] = unicode(lastName, 'latin-1')


    # remove some plot frame lines
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    # limit the range of the plot to where the data is
    plt.xlim(allSeasons[0], allSeasons[len(allSeasons) - 1])

    maximum = int(round(maxValue))
    step    = int(round(maxValue / 10))

    plt.yticks(range(0, maximum, step), [u"\xA3"  + str(x) + " mil" for x in range(0, maximum, step)], fontsize=14)
    plt.xticks(fontsize=14)

    # print tick lines across the plot
    for y in range(0, maximum, step):
        plt.plot(range(allSeasons[0], allSeasons[len(allSeasons) - 1] + 1),
                 [y] * len(range(allSeasons[0], allSeasons[len(allSeasons) - 1] + 1)),
                 "--", lw=0.5, color="black", alpha=0.3)

    # remove the tick marks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    positions = list()

    for idx, playerId in enumerate(lastSeasonDataDict.keys()):
        # each line with different color
        plt.plot(allSeasons, playersDataDict[playerId],
                lw=2.5, color=colors[idx % len(colors)])

        posY = int(playersDataDict[playerId][-1])

        # prevent overlapping text
        if(posY in positions):
            posY += 2

            while(posY in positions):
                posY += 2

        positions.append(posY)
        plt.text(allSeasons[-1], posY, playersNames[playerId], fontsize=14, color=colors[idx])

    plt.text(allSeasons[len(allSeasons) / 2], -5, "Football players market value fluctuation through seasons 2001-2015",
             fontsize=13, ha="center")

    plt.savefig("playersValueFluctuation.png")

if __name__ == "__main__":
    main()