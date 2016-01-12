__author__ = 'Matevz Lenic'

import snap
import networkx as nx
from operator import itemgetter
import sys

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

    if(export == 'Y'):
        seasonsInput = raw_input('Please enter desired seasons separated by comma (all for all of them): ')
        leaguesInput = raw_input('Please enter IDs of desired leagues separated by comma (all for all of them): ')
    else:
        seasonsInput = 'all'
        leaguesInput = 'all'

    if(seasonsInput == 'all'):
        seasons = seasonsInput
    else:
        seasons = seasonsInput.split(',')
        seasons = [int(season) for season in seasons]

    if(leaguesInput == 'all'):
        leagues = leaguesInput
    # for easier testing
    elif(leaguesInput == 'INA'):
        leagues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    else:
        leagues = leaguesInput.split(',')
        leagues = [int(league) for league in leagues]

    if(export == 'Y'):
        if(filename == 'Players'):
            utils.createPlayerEdgeListFromDB("PlayerNet.adj", seasons)
        else:
            utils.createClubEdgeListFromDB('ClubNet.adj', seasons, leagues, False)

    if(filename == 'Players'):
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

    if(filename == 'Clubs'):
        print "[Analyzer]  calculating Betweenness centrality..."
        betweenness = nx.betweenness_centrality(network)
        # betweenness = utils.calculateWeightedBetweennessCentrality(network)
        print "[Analyzer]  sorting Betweenness centrality dictionary..."
        betweenness = sorted(betweenness.items(), key=itemgetter(1), reverse=True)

    # print top 25
    print "\n[Results]  PageRank"
    for i in range(0, 100):
        print "Node name: %s, score: %f" % (nodeData[pagerank[i][0]][0], pagerank[i][1])

    if(filename == 'Clubs'):
        print "\n[Results]  Betweenness centrality"
        for i in range(0, 100):
            print "Node name: %s, score: %f" % (nodeData[betweenness[i][0]][0], betweenness[i][1])

if __name__ == "__main__":
    main()