__author__ = 'matic'

import snap
import networkx as nx
from random import randint
from datetime import date
import operator
import sys
import os

sys.path.insert(0, '../')
import constants
import utils


def predictPlayerValue(network, playerIds, playersInfo):
    predictedValues = list()

    for playerId in playerIds:
        valueSum     = 0
        numNeighbors = 0

        # sum all neighbours values
        for neighbor in network.neighbors(playerId):
            if(neighbor in playersInfo.keys()):
                # add neighbors value
                bestSeason = max(playersInfo[neighbor].iteritems(), key=operator.itemgetter(1))[0]
                value      = playersInfo[neighbor][bestSeason][4]

                if(value):
                    value = float(value)
                else:
                    value = 0.0

                valueSum     += value
                numNeighbors += 1

        predictedValue = valueSum / float(numNeighbors)


        lastSeason      = max(playersInfo[playerId].keys())
        birthYear       = playersInfo[playerId][lastSeason][5]
        playingPosition = playersInfo[playerId][lastSeason][6]

        # boost predicted value of players that have 'good' age
        if(birthYear):
            age          = date.today().year - int(birthYear)
            ageDeviation = abs(constants.mostValuableAge - age)

            # young players should be penalized less
            if(age < constants.mostValuableAge):
                ageDeviation *= 0.8

            initialValueBoost   = value / 2.0
            boostPercentDropOff = ageDeviation / 5
            valueBoost          = initialValueBoost * max(-0.6, (1 - boostPercentDropOff))

            predictedValue += valueBoost

        # defenders and goalkeepers are usually worth less
        if(playingPosition):
            if(playingPosition == 'MID' or playingPosition == 'ATT'):
                predictedValue *= 1.5
            elif(playingPosition == 'GK'):
                predictedValue *= 0.8

        predictedValues.append(int(round(predictedValue)))

    return predictedValues

def main():
    tempFilename = 'PlayerNetPricePredictionTMP' + `randint(0,100)` + '.adj'
    playerIds    = raw_input('Please enter IDs of the players you want to predict value for (seperated by comma): ')
    playerIds    = playerIds.split(',')
    history      = raw_input('Enter how many seasons would you like to take into account in value predictor: ')
    seasons      = list()

    for i in range(0, int(history)):
        seasons.append(int(constants.currentSeason) - i)
    seasons.reverse()

    # export edge list to a temporary file
    [playerIndices, playersInfo] = utils.createPlayerEdgeListFromDB(tempFilename, seasons)

    mappedPlayerIds = [playerIndices[int(playerId)] for playerId in playerIds]

    # remap playersInfo indices into networks indices
    playersInfoMapped = dict()
    for key in playersInfo.keys():
        playersInfoMapped[playerIndices[int(key)]] = playersInfo.pop(int(key))

    # create a network
    [network, nodeData] = utils.createWeightedGraphFromEdgeList(tempFilename)

    playerNames       = [nodeData[mappedPlayerId][0] for mappedPlayerId in mappedPlayerIds]
    playerNamesString = ', '.join(playerNames)

    print "\n[Value predictor]  Predicting value for player(s) %s..." % \
          playerNamesString

    # predict the value for the selected player
    predictedValues = predictPlayerValue(network, mappedPlayerIds, playersInfoMapped)
    predictedValues = [predictedValue / 1000000.0 for predictedValue in predictedValues]

    print "\n"

    for idx, predictedValue in enumerate(predictedValues):
        print "[Value predictor]  Predicted value for player %s: %.2f million pounds" % \
              (playerNames[idx], predictedValue)

    # remove temporary edge list
    os.remove(tempFilename)

if __name__ == "__main__":
    main()