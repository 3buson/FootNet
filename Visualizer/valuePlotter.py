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

    # "Tableau 20" RGB colors
    colors = constants.tabelau20

    # scale RGB values to the [0, 1] interval
    for i in range(len(colors)):
        r, g, b   = colors[i]
        colors[i] = (r / 255.0, g / 255.0, b / 255.0)

    plt.figure(figsize=(12, 14))

    # prepare the data
    playersDataDict = dict()

    if(byClubs):
        playersData = cursor.execute("SELECT idP, idS, playerValue FROM playerclubseason WHERE idP IN (SELECT idP FROM playerclubseason WHERE idS = ? AND idClub = ?) ORDER BY idP, idS", currentSeason, clubId)
    else:
        playersData = cursor.execute("SELECT idP, idS, playerValue FROM playerclubseason WHERE idP IN (%s) ORDER BY idP, idS" % playersString)

    maxValue = 0

    for playerData in playersData:
        playerId = playerData[0]
        seasonId = playerData[1]
        value    = playerData[2]

        if(byClubs):
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

    for rank, column in enumerate(players):
        # each line with different color
        plt.plot(allSeasons, playersDataDict[column],
                lw=2.5, color=colors[rank % len(colors)])

        # Add a text label to the right end of every line. Most of the code below
        # is adding specific offsets y position because some labels overlapped.
        # y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5
        # if column == "Foreign Languages":
        #     y_pos += 0.5
        # elif column == "English":
        #     y_pos -= 0.5
        # elif column == "Communications\nand Journalism":
        #     y_pos += 0.75
        # elif column == "Art and Performance":
        #     y_pos -= 0.25
        # elif column == "Agriculture":
        #     y_pos += 1.25
        # elif column == "Social Sciences and History":
        #     y_pos += 0.25
        # elif column == "Business":
        #     y_pos -= 0.75
        # elif column == "Math and Statistics":
        #     y_pos += 0.75
        # elif column == "Architecture":
        #     y_pos -= 0.75
        # elif column == "Computer Science":
        #     y_pos += 0.75
        # elif column == "Engineering":
        #     y_pos -= 0.25

        # Again, make sure that all labels are large enough to be easily read
        # by the viewer.
        # plt.text(2011.5, y_pos, column, fontsize=14, color=tableau20[rank])

    plt.text(allSeasons[len(allSeasons) / 2], -5, "Football players market value fluctuation through seasons 2001-2015",
             fontsize=13, ha="center")

    # plt.show()
    plt.savefig("playersValueFluctuation.png", bbox_inches="tight")

if __name__ == "__main__":
    main()