__author__ = 'Matevz Lenic'

import snap
import matplotlib.pyplot as plt
import time

def analyzePageRank(FNGraph):
    t1 = time.time()
    print "Started calculating PageRank scores: \n"
    PRankH = snap.TIntFltH()
    snap.GetPageRank(FNGraph, PRankH)
    PRankH.Sort(False,"Asc")
    for item in PRankH:
        print "\t %s %.7f" % (item, PRankH[item])
    print "\nFinished calculating in %.3f seconds\n" % (time.time()-t1)

def analyzeBetweenness(FNGraph):
    t1 = time.time()
    print "Started calculating Betweenness scores: \n"
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(FNGraph, Nodes, Edges, 1.0)
    Nodes.Sort(False, "Asc")
    for node in Nodes:
        print "\tnode: %d centrality: %.7f" % (node, Nodes[node])
    print "\nFinished calculating in %.3f seconds\n" % (time.time()-t1)

def analyzeDegrees(FNGraph):
    t1 = time.time()
    print "Started analysing network degrees: \n"
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(FNGraph, DegToCntV)
    avgDeg = 0
    xVec = list()
    yVec = list()
    for item in DegToCntV:
        avgDeg += int(item.GetVal2()) * int(item.GetVal1())
        xVec.append(item.GetVal1())
        yVec.append(item.GetVal2())
    avgDeg = avgDeg/FNGraph.GetNodes()
    print "\tNetwork average degree %d" % avgDeg

    #plot degree distribution
    plt.figure(0)
    plt.plot(xVec, yVec, 'b-')
    plt.title("Degree distribution for Football network \n Average degree: %d" % avgDeg)
    plt.ylabel("Number of nodes")
    plt.xlabel("Degrees")
    plt.show()
    print "\nFinished calculating in %.3f seconds\n" % (time.time()-t1)

def analyzeMisc(FNGraph):
    #Getting LCC, average distances, clustering
    t1 = time.time()
    print "Started calculating miscellaneous network statistics: \n"
    FNGraph = snap.LoadEdgeList(snap.PUNGraph, "adjlist")
    print '\tPercentage of nodes in LCC in Football network: %.3f' % float(snap.GetMxWccSz(FNGraph))
    GraphClustCoeff = snap.GetClustCf (FNGraph, -1)
    print "\tClustering coefficient: %.3f" % GraphClustCoeff

    print "Finished calculating in %f seconds\n" % (time.time()-t1)


def main():
    FNGraph = snap.LoadEdgeList(snap.PUNGraph, "EPLLaLiga131415")
    #analyzePageRank(FNGraph)
    #analyzeBetweenness(FNGraph)
    #analyzeDegrees(FNGraph)
    analyzeMisc(FNGraph)


if __name__ == "__main__":
    main()