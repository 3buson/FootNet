__author__ = 'Matevz Lenic'

import snap
import networkx as nx
from operator import itemgetter
import sys

sys.path.insert(0, '../')
import utils

def main():
    filename = 'ClubNet.adj'

    utils.createClubEdgeListFromDB('ClubNet.adj')
    # utils.createPlayerEdgeListFromDB("PlayerNet.adj")

    [network, nodeData] = utils.createWeightedGraphFromEdgeList(filename)

    print "[Analyzer]  calculating PageRank..."
    pagerank = nx.pagerank(network)
    # pagerank = utils.calculatePageRank(FNetwork)

    print "[Analyzer]  sorting PageRank dictionary..."
    pagerank = sorted(pagerank.items(), key=itemgetter(1), reverse=True)

    # print top 25
    for i in range(0, 100):
        print "Node name: %s, score: %f" % (nodeData[pagerank[i][0]][0], pagerank[i][1])

if __name__ == "__main__":
    main()