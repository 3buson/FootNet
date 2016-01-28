__author__ = 'Matevz Lenic'

import snap
import time
import matplotlib.pyplot as plt


def analyzeCloseness(FNGraph):
    t1 = time.time()

    print "Started calculating Closeness scores: \n"

    closeness = dict()

    for NI in FNGraph.Nodes():
        closeness[NI.GetId()] = snap.GetClosenessCentr(FNGraph, NI.GetId())

    nodesSortedByCloseness = sorted(closeness, key=closeness.get, reverse=True)

    # print top 25
    for i in range(0, 25):
        print "\tNode %d \t Closeness: %f" %\
            (nodesSortedByCloseness[i], closeness[nodesSortedByCloseness[i]])

    print "\nFinished calculating in %.3f seconds\n" % (time.time()-t1)


def analyzePageRank(FNGraph):
    t1 = time.time()

    print "Started calculating PageRank scores: \n"

    PRankH = snap.TIntFltH()

    snap.GetPageRank(FNGraph, PRankH)
    PRankH.Sort(False, False)

    nodesPrinted = 0
    for item in PRankH:
        if(nodesPrinted < 25):
            print "\tNode: %s \t PageRank: %.7f" % (item, PRankH[item])
        else:
            break

        nodesPrinted += 1

    print "\nFinished calculating in %.3f seconds\n" % (time.time()-t1)


def analyzeBetweenness(FNGraph):
    t1 = time.time()

    print "Started calculating Betweenness scores: \n"

    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()

    snap.GetBetweennessCentr(FNGraph, Nodes, Edges, 1.0)
    Nodes.Sort(False, False)

    nodesPrinted = 0
    for node in Nodes:
        if(nodesPrinted < 25):
            print "\tNode: %d \t Betweenness: %.7f" % (node, Nodes[node])
        else:
            break

        nodesPrinted += 1

    print "\nFinished calculating in %.3f seconds\n" % (time.time()-t1)


def analyzeDegrees(FNGraph):
    t1 = time.time()

    print "Started analysing network degrees: \n"

    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(FNGraph, DegToCntV)

    avgDeg = 0
    xVec   = list()
    yVec   = list()

    for item in DegToCntV:
        avgDeg += int(item.GetVal2()) * int(item.GetVal1())
        xVec.append(item.GetVal1())
        yVec.append(item.GetVal2())

    avgDeg = avgDeg/FNGraph.GetNodes()

    print "\tNetwork average degree %d" % avgDeg

    # plot degree distribution
    plt.figure(0)
    plt.plot(xVec, yVec, 'b-')
    plt.title("Degree distribution for Football network \n Average degree: %d" % avgDeg)
    plt.ylabel("Number of nodes")
    plt.xlabel("Degrees")
    plt.savefig('DegreeDistribution.png')

    print "\nFinished calculating in %.3f seconds\n" % (time.time()-t1)


def analyzeMisc(FNGraph):
    # LCC, average distances, clustering
    t1 = time.time()

    print "Started calculating miscellaneous network statistics:"

    print '\tPercentage of nodes in LCC in Football network: %.3f' % (snap.GetMxWccSz(FNGraph) * 100.0)
    GraphClustCoeff = snap.GetClustCf (FNGraph, -1)
    print "\tClustering coefficient: %.3f" % GraphClustCoeff

    diam = snap.GetBfsFullDiam(FNGraph, 1432, False)
    print "\tNetwork diameter: %.3f\n" % diam

    print "\tCalculating average distance..."

    avgDist   = 0
    iter1     = 0
    allNodes1 = FNGraph.GetNodes()

    for NI in FNGraph.Nodes():
        if(iter1 % 100 == 0):
            print "\t\tCalculated for %d nodes" % iter1
        NIdToDistH = snap.TIntH()
        snap.GetShortPath(FNGraph, NI.GetId(), NIdToDistH)
        singleDistSum = 0

        for item in NIdToDistH:
            singleDistSum += NIdToDistH[item]

        avgDist += (1.0/allNodes1) * float(singleDistSum)/(allNodes1-1)
        iter1   += 1

    print "\tNetwork average distance: %.3f" % avgDist

    print "\nFinished calculating in %f seconds\n" % (time.time() - t1)


def main():
    FNGraph = snap.LoadEdgeList(snap.PUNGraph, "EPLLaLiga131415")
    #analyzeCloseness(FNGraph)
    #analyzePageRank(FNGraph)
    #analyzeBetweenness(FNGraph)
    #analyzeDegrees(FNGraph)
    #analyzeMisc(FNGraph)


if __name__ == "__main__":
    main()