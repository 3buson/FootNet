__author__ = 'Matevz Lenic'

import snap
import networkx as nx
from operator import itemgetter
import sys

sys.path.insert(0, '../')
import utils

def main():
    filename = 'PlayerNet.adj'
    seasons  = [10,11,12,13]

    # utils.createClubEdgeListFromDB('ClubNet.adj', seasons)
    utils.createPlayerEdgeListFromDB("PlayerNet.adj", seasons)

    # [network, nodeData] = utils.createWeightedGraphFromEdgeList(filename)
    [network, nodeData] = utils.createWeightedGraphFromEdgeList(filename, directed=True)

    print "[Analyzer]  calculating PageRank..."
    pagerank = nx.pagerank(network)
    # pagerank = utils.calculatePageRank(network)
    print "[Analyzer]  sorting PageRank dictionary..."
    pagerank = sorted(pagerank.items(), key=itemgetter(1), reverse=True)

    print "[Analyzer]  calculating Betweenness centrality..."
    # betweenness = nx.betweenness_centrality(network)
    # betweenness = utils.calculateWeightedBetweennessCentrality(network)
    # print "[Analyzer]  sorting Betweenness centrality dictionary..."
    # betweenness = sorted(betweenness.items(), key=itemgetter(1), reverse=True)

    # print top 25

    print "\n[Results]  PageRank"
    for i in range(0, 100):
        print "Node name: %s, score: %f" % (nodeData[pagerank[i][0]][0], pagerank[i][1])

    # print "\n[Results]  Betweenness centrality"
    # for i in range(0, 100):
    #     print "Node name: %s, score: %f" % (nodeData[betweenness[i][0]][0], betweenness[i][1])

if __name__ == "__main__":
    main()