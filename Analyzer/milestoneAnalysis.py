__author__ = 'Matevz Lenic'

import snap
import networkx as nx
from operator import itemgetter
import sys

sys.path.insert(0, '../')
import utils

def main():
    export       = raw_input('Do you want to do an edge list export first? (Y/N): ')
    filename     = raw_input('Do you want to analyze players or clubs? (Players/Clubs): ')
    seasonsInput = raw_input('Please enter desired seasons separated by comma (all for all of them): ')

    if(seasonsInput != 'all'):
        seasons = seasonsInput.split(',')

        seasons = [int(season) for season in seasons]
    else:
        seasons = seasonsInput


    if(export == 'Y'):
        if(filename == 'Clubs'):
            utils.createClubEdgeListFromDB('ClubNet.adj', seasons)
        else:
            utils.createPlayerEdgeListFromDB("PlayerNet.adj", seasons)

    if(filename == 'Clubs'):
        [network, nodeData] = utils.createWeightedGraphFromEdgeList('ClubNet.adj', directed=True)
    else:
        [network, nodeData] = utils.createWeightedGraphFromEdgeList('PlayerNet.adj')

    print "[Analyzer]  calculating PageRank..."
    pagerank = nx.pagerank(network)
    # pagerank = utils.calculatePageRank(network)
    print "[Analyzer]  sorting PageRank dictionary..."
    pagerank = sorted(pagerank.items(), key=itemgetter(1), reverse=True)

    print "[Analyzer]  calculating Betweenness centrality..."
    betweenness = nx.betweenness_centrality(network)
    # betweenness = utils.calculateWeightedBetweennessCentrality(network)
    print "[Analyzer]  sorting Betweenness centrality dictionary..."
    betweenness = sorted(betweenness.items(), key=itemgetter(1), reverse=True)

    # print top 25

    print "\n[Results]  PageRank"
    for i in range(0, 100):
        print "Node name: %s, score: %f" % (nodeData[pagerank[i][0]][0], pagerank[i][1])

    print "\n[Results]  Betweenness centrality"
    for i in range(0, 100):
        print "Node name: %s, score: %f" % (nodeData[betweenness[i][0]][0], betweenness[i][1])

if __name__ == "__main__":
    main()