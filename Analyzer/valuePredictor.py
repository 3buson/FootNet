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


def predictPlayerValue(network, playerId, playersInfo):
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

    return int(round(predictedValue))

def main():
    tempFilename = 'PlayerNetPricePredictionTMP' + `randint(0,100)` + '.adj'
    playerId     = raw_input('Please enter ID of the player you want to predict value for: ')
    playerId     = int(playerId)
    seasons      = [13,14,15]

    # export edge list to a temporary file
    [playerIndices, playersInfo] = utils.createPlayerEdgeListFromDB(tempFilename, seasons)

    mappedPlayerId = playerIndices[int(playerId)]

    # remap playersInfo indices into networks indices
    playersInfoMapped = dict()
    for key in playersInfo.keys():
        playersInfoMapped[playerIndices[int(key)]] = playersInfo.pop(int(key))

    # create a network
    [network, nodeData] = utils.createWeightedGraphFromEdgeList(tempFilename)

    print "[Value predictor]  Predicting value for player %s..." % nodeData[mappedPlayerId][0]

    # predict the value for the selected player
    predictedValue = predictPlayerValue(network, mappedPlayerId, playersInfoMapped)
    predictedValue = predictedValue / 1000000.0

    print "[Value predictor]  Predicted value for player %s: %.2f million pounds" % (nodeData[mappedPlayerId][0], predictedValue)

    # remove temporary edge list
    os.remove(tempFilename)

if __name__ == "__main__":
    main()