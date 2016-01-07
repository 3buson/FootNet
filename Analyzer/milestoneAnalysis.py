__author__ = 'Matevz Lenic'

import snap
import networkx as nx
import sys

sys.path.insert(0, '../')
import utils

def main():
    FNetwork = utils.createWeightedGraphFromEdgeList('../FootNet.adj')
    print FNetwork.edges(data=True)[0]

if __name__ == "__main__":
    main()