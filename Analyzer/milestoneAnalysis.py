__author__ = 'Matevz Lenic'

import snap
import networkx as nx
import sys

sys.path.insert(0, '../')
import utils

def main():
    #utils.createPlayerEdgeListFromDB("FootNet.adj")
    FNetwork = utils.createWeightedGraphFromEdgeList('FootNet.adj')
    PRDict = dict()
    print FNetwork.edges(data=True)[0]
    PRDict = nx.pagerank(FNetwork)
    print PRDict[1]

if __name__ == "__main__":
    main()