__author__ = 'Jekleni Lenic'

import snap

def analyzePageRank():
    FNGraph = snap.LoadEdgeList(snap.PUNGraph, "adjlist")
    PRankH = snap.TIntFltH()
    snap.GetPageRank(FNGraph, PRankH)
    for item in PRankH:
        print item, PRankH[item]

def analyzeBetweenness():
    FNGraph = snap.LoadEdgeList(snap.PUNGraph, "adjlist")
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(FNGraph, Nodes, Edges, 1.0)

    for node in Nodes:
        print "node: %d centrality: %f" % (node, Nodes[node])

#analyzePageRank()
analyzeBetweenness()
