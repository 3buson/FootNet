__author__ = 'Matevz Lenic'

import os
import sys
import time
import snap
import networkx as nx
from datetime import date
from operator import itemgetter

sys.path.insert(0, '../')
import utils
import constants


def printNetworkProperties(network, directed):
    print "[Analyzer]  Calculating average degrees..."
    degrees       = network.degree()
    averageDegree = sum(degrees.values()) / float(len(degrees.values()))
    print "[Analyzer]  Average degree: %f" % averageDegree

    if(directed):
        inDegrees        = network.in_degree()
        outDegrees       = network.out_degree()
        averageInDegree  = sum(inDegrees.values())  / float(len(inDegrees.values()))
        averageOutDegree = sum(outDegrees.values()) / float(len(outDegrees.values()))
        print "[Analyzer]  Average in degree: %f"  % averageInDegree
        print "[Analyzer]  Average out degree: %f" % averageOutDegree

    print "[Analyzer]  Calculating percentage of nodes in LCC..."
    numOfNodes = network.number_of_nodes()
    if(directed):
        lcc     = max(nx.strongly_connected_component_subgraphs(network), key=len)
        lccSize = len(lcc)
    else:
        lcc     = max(nx.connected_component_subgraphs(network), key=len)
        lccSize = len(lcc)
    print "[Analyzer]  Percentage of nodes in LCC: %f" % (lccSize / float(numOfNodes))

    print "[Analyzer]  Calculating average distance..."
    averageDistance = nx.average_shortest_path_length(lcc)
    print "[Analyzer]  Average distance: %f" % averageDistance


    if(not directed):
        print "[Analyzer]  Calculating average clustering..."
        averageClustering = nx.average_clustering(network)
        print "[Analyzer]  Average clustering: %f" % averageClustering

        print "[Analyzer]  Calculating diameter..."
        diameter = nx.diameter(lcc)
        print "[Analyzer]  Diameter: %d" % diameter


def main():
    export       = raw_input('Do you want to do an edge list export first? (Y/N): ')
    outputToFile = raw_input('Do you want to output results to a file as well? (Y/N): ')
    filename     = raw_input('Do you want to analyze players or clubs? (Players/Clubs): ')

    playerAnalysis = (filename.lower() == 'players')
    outputToFile   = (outputToFile.lower() == 'y')

    if(outputToFile):
        outputFile = open(filename + 'AnalysisResults.txt', 'w')

    if(export.lower() == 'y'):
        export       = True
        seasonsInput = raw_input('Please enter desired seasons separated by comma (all for all of them): ')
        leaguesInput = raw_input('Please enter IDs of desired leagues separated by comma (all for all of them): ')
    else:
        export       = False
        seasonsInput = 'all'
        leaguesInput = 'all'

    if(seasonsInput.lower() == 'all'):
        seasons = seasonsInput
    else:
        seasons = seasonsInput.split(',')
        seasons = [int(season) for season in seasons]

    if(leaguesInput.lower() == 'all'):
        leagues = leaguesInput
    # for easier testing
    elif(leaguesInput.lower() == 'ina'):
        leagues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    else:
        leagues = leaguesInput.split(',')
        leagues = [int(league) for league in leagues]

    if(playerAnalysis):
        ageGroups = raw_input('Do you want to analyze players perspectiveness? (Y/N): ')
        ageGroups = (ageGroups == 'Y')
    else:
        ageGroups = False

    if(export):
        if(playerAnalysis):
            utils.createPlayerEdgeListFromDB("PlayerNet.adj", seasons, leagues)
        else:
            utils.createClubEdgeListFromDB('ClubNet.adj', seasons, leagues)

    if(playerAnalysis):
        [network, nodeData] = utils.createWeightedGraphFromEdgeList('PlayerNet.adj')
    else:
        [network, nodeData] = utils.createWeightedGraphFromEdgeList('ClubNet.adj', directed=True)

    # directed = (filename == 'Clubs')
    # printNetworkProperties(network, directed)

    print "[Analyzer]  calculating PageRank..."

    startTime = time.time()
    pagerank  = nx.pagerank(network)
    endTime   = time.time()

    print "[Analyzer]  PageRank calculated, time spent: %f s" % (endTime - startTime)
    print "[Analyzer]  sorting PageRank dictionary..."

    pagerank = sorted(pagerank.items(), key=itemgetter(1), reverse=True)

    if(not playerAnalysis):
        print "[Analyzer]  calculating Betweenness centrality..."
        betweenness = nx.betweenness_centrality(network)
        # betweenness = utils.calculateWeightedBetweennessCentrality(network)
        print "[Analyzer]  sorting Betweenness centrality dictionary..."
        betweenness = sorted(betweenness.items(), key=itemgetter(1), reverse=True)


    # print top 100
    pagerankString = "\n[Analyzer - Results]  PageRank"
    print pagerankString

    if(outputToFile):
        outputFile.write(pagerankString + '\n\n')

    for i in range(0, 100):
        if(not playerAnalysis):
            outputString = "Node name: %s, score: %f" % (nodeData[pagerank[i][0]], pagerank[i][1])
            print outputString

            if(outputToFile):
                outputFile.write(outputString + '\n')
        else:
            outputString = "Node name: %s, score: %f" % (nodeData[pagerank[i][0]][0], pagerank[i][1])
            print outputString

            if(outputToFile):
                outputFile.write(outputString + '\n')

    if(ageGroups):
        # separate players into age groups
        print "\n[Analyzer - Results]  Separating players into age groups..."

        baseFilename  = 'perspectivePlayers'
        playersGroups = dict()
        for age in range(constants.youngestAgeGroup, constants.oldestAgeGroup):
            birthYear = date.today().year - age

            print "[Analyzer - Results]  Processing players born in %d" % birthYear

            playersGroups[age] = list()
            for pagerankRecord in pagerank:
                playerId    = pagerankRecord[0]
                playerAge   = nodeData[pagerankRecord[0]][1]
                playerScore = pagerankRecord[1]

                # if player has 'correct' age
                if(playerAge == age):
                    playersGroups[age].append([playerId, playerAge, playerScore])
                # only do this for top 50 players of each age group
                if(len(playersGroups[age]) >= 50):
                    break

            # check if directory 'PlayersByAgeGroups' exists and create it if necessary
            directory = 'PlayersByAgeGroups'
            if not os.path.exists(directory):
                os.makedirs(directory)

            # write this to a file
            f = open(directory + '/' + baseFilename + `birthYear` + '.txt', 'w')
            f.write("PageRank results for players born in %d\n\n" % birthYear)

            for playerRecord in playersGroups[age]:
                f.write("Player name: %s, score: %f\n" %
                        (nodeData[playerRecord[0]][0], playerRecord[2]))

            f.close()

        print "\n[Analyzer - Results]  PageRank scores by age groups written into files."


    if(not playerAnalysis):
        betweennessString = "\n[Analyzer - Results]  Betweenness centrality"
        print betweennessString

        if(outputToFile):
            outputFile.write('\n' + betweennessString + '\n\n')
        for i in range(0, 100):
            outputString = "Node name: %s, score: %f" % (nodeData[betweenness[i][0]], betweenness[i][1])
            print outputString

            if(outputToFile):
                outputFile.write(outputString + '\n')


    if(outputToFile):
        outputFile.close()


if __name__ == "__main__":
    main()