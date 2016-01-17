__author__ = 'matic'

import snap
import networkx as nx
from datetime import date
import operator
import sys
import os

sys.path.insert(0, '../')
import constants
import utils


def predictPlayerValue(network, playerId, playersInfo):
    valueSum     = 0
    numNeighbors = 0

    # sum all neighbours values
    for neighbor in network.neighbors(playerId):
        if(neighbor in playersInfo.keys()):
            # add neighbors value
            bestSeason      = max(playersInfo[neighbor].iteritems(), key=operator.itemgetter(1))[0]
            value           = playersInfo[neighbor][bestSeason][4]
            birthYear       = playersInfo[neighbor][bestSeason][5]
            playingPosition = playersInfo[neighbor][bestSeason][6]

            if(value):
                value = float(value)
            else:
                value = 0.0

            # boost predicted value of players that have 'good' age
            if(birthYear):
                age          = date.today().year - int(birthYear)
                ageDeviation = abs(constants.mostValuableAge - age)

                initialValueBoost   = value / 2.0
                boostPercentDropoff = ageDeviation / 5
                valueBoost          = initialValueBoost * (1 - boostPercentDropoff)

                value += valueBoost


            # defenders and goalkeepers are usualy worth less
            if(playingPosition):
                if(playingPosition == 'MID' or playingPosition == 'ATT'):
                    value *= 1.5

            valueSum     += value
            numNeighbors += 1

    predictedValue = valueSum / float(numNeighbors)

    return int(round(predictedValue))

def main():
    tempFilename = 'PlayerNetPricePredictionTMP.adj'
    playerId     = raw_input('Please enter ID of the player you want to predict value for: ')
    seasons      = [13,14,15]

    # export edge list to a temporary file
    [playerIndices, playersInfo] = utils.createPlayerEdgeListFromDB(tempFilename, seasons)

    # remap playersInfo indices into networks indices
    for key in playersInfo.keys():
        playersInfo[playerIndices[key]] = playersInfo.pop(key)

    mappedPlayerId = playerIndices[int(playerId)]

    # create a network
    [network, nodeData] = utils.createWeightedGraphFromEdgeList(tempFilename)

    print "[Value predictor]  Predicting value for player %s..." % nodeData[mappedPlayerId][0]

    # predict the value for the selected player
    predictedValue = predictPlayerValue(network, mappedPlayerId, playersInfo)
    predictedValue = predictedValue / 1000000.0

    print "[Value predictor]  Predicted value for player %s: %.2f million pounds" % (nodeData[mappedPlayerId][0], predictedValue)

    # remove temporary edge list
    os.remove(tempFilename)

if __name__ == "__main__":
    main()