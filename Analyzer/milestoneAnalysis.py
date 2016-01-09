__author__ = 'Matevz Lenic'

import snap
import networkx as nx
from operator import itemgetter
import sys

sys.path.insert(0, '../')
import utils

def main():
    # utils.createClubEdgeListFromDB('ClubNet.adj')
    # utils.createPlayerEdgeListFromDB("PlayerNet.adj")

    [playersNetwork, playersData] = utils.createWeightedGraphFromEdgeList('PlayerNet.adj')

    print "[Analyzer]  calculating PageRank..."
    playersPagerank = nx.pagerank(playersNetwork)
    # playersPagerank = utils.calculatePageRank(FNetwork)

    print "[Analyzer]  sorting PageRank dictionary..."
    playersPagerank = sorted(playersPagerank.items(), key=itemgetter(1), reverse=True)

    # print top 25
    for i in range(0, 25):
        print "Player name: %s, score: %f" % (playersData[playersPagerank[i][0]][0], playersPagerank[i][1])

if __name__ == "__main__":
    main()