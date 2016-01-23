__author__ = 'Matevz Lenic'

import snap
import networkx as nx
from operator import itemgetter
import sys
import os

sys.path.insert(0, '../')
import utils


def printNetworkProperties(network, directed):
    print "[Analyzer]  Calculating average degrees..."
    degrees          = network.degree()
    averageDegree    = sum(degrees.values()) / float(len(degrees.values()))
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
    export   = raw_input('Do you want to do an edge list export first? (Y/N): ')
    filename = raw_input('Do you want to analyze players or clubs? (Players/Clubs): ')

    playerAnalysis = (filename.lower() == 'players')

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
            utils.createClubEdgeListFromDB('ClubNet.adj', seasons, leagues, False)

    if(playerAnalysis):
        [network, nodeData] = utils.createWeightedGraphFromEdgeList('PlayerNet.adj')
    else:
        [network, nodeData] = utils.createWeightedGraphFromEdgeList('ClubNet.adj', directed=True)

    # directed = (filename == 'Clubs')
    # printNetworkProperties(network, directed)

    print "[Analyzer]  calculating PageRank..."
    pagerank = nx.pagerank(network)
    # pagerank = utils.calculatePageRank(network)
    print "[Analyzer]  sorting PageRank dictionary..."
    pagerank = sorted(pagerank.items(), key=itemgetter(1), reverse=True)

    if(not playerAnalysis):
        print "[Analyzer]  calculating Betweenness centrality..."
        betweenness = nx.betweenness_centrality(network)
        # betweenness = utils.calculateWeightedBetweennessCentrality(network)
        print "[Analyzer]  sorting Betweenness centrality dictionary..."
        betweenness = sorted(betweenness.items(), key=itemgetter(1), reverse=True)

    # print top 25
    if(not ageGroups):
        print "\n[Analyzer - Results]  PageRank"
        for i in range(0, 100):
            if(not playerAnalysis):
                print "Node name: %s, score: %f" % (nodeData[pagerank[i][0]], pagerank[i][1])
            else:
                print "Node name: %s, score: %f" % (nodeData[pagerank[i][0]][0], pagerank[i][1])
    else:
        # separate players into age groups
        print "\n[Analyzer - Results]  Separating players into page groups..."

        baseFilename  = 'perspectivePlayers'
        playersGroups = dict()
        for age in range(18,25):
            print "\n[Analyzer - Results]  Processing age group ", age

            playersGroups[age] = list()
            for pagerankRecord in pagerank:
                # if player has 'correct' age
                if(nodeData[pagerankRecord[0]][1] == age):
                    # add player ID, player age and player PageRank score to list
                    playersGroups[age].append([pagerankRecord[0], nodeData[pagerankRecord[0]][1], pagerankRecord[1]])
                if(len(playersGroups[age]) >= 25):
                    break

            # check if directory 'Visualizations' exists and create it if necessary
            directory = 'PlayersByAgeGroups'
            if not os.path.exists(directory):
                os.makedirs(directory)

            # write this to a file
            f = open(directory + '/' + baseFilename + `age` + '.txt', 'w')
            f.write("PageRank results for players aged %d\n\n" % age)

            for playerRecord in playersGroups[age]:
                f.write("Player name: %s, player age: %d, score: %f\n" %
                        (nodeData[playerRecord[0]][0], playerRecord[1], playerRecord[2]))

            f.close()

        print "\n[Analyzer - Results]  PageRank scores by age groups written into files."


    if(not playerAnalysis):
        print "\n[Analyzer - Results]  Betweenness centrality"
        for i in range(0, 100):
            print "Node name: %s, score: %f" %\
                  (nodeData[betweenness[i][0]], betweenness[i][1])

if __name__ == "__main__":
    main()