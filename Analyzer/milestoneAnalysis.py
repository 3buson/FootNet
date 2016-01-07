__author__ = 'Matevz Lenic'

import snap
import networkx as nx
from operator import itemgetter
import sys

sys.path.insert(0, '../')
import utils

def main():
    # FNetwork = utils.createWeightedGraphFromEdgeList('../FootNet.adj')
    #
    # print FNetwork.edges(data=True)[0]
    #
    # print "[Analyzer]  calculating pagerank..."
    # # pagerank = nx.pagerank(FNetwork)
    # pagerank = utils.calculatePageRank(FNetwork)
    #
    # print "[Analyzer]  sorting pagerank dictionary..."
    # pagerank = sorted(pagerank.items(), key=itemgetter(1), reverse=True)
    #
    # # print top 25
    # for i in range(0, 25):
    #     print pagerank[i]

    #utils.createPlayerEdgeListFromDB("FootNet.adj")

    utils.createClubEdgeListFromDB('ClubNet.adj')

if __name__ == "__main__":
    main()