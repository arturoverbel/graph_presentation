import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms_prev.dijkstra_prev import *
from algorithms_prev.floyd_warshall_prev import *

graph = Graph.creategraph(9, .8)

def test_predecesors():
    dist, pred = Dijkstra_apsp_PREV(graph)
    np.testing.assert_equal(True, Graph.testDistPred(dist, pred))

    dist, pred = Floyd_Warshall_PREV(graph)
    np.testing.assert_equal(True, Graph.testDistPred(dist, pred))

    #np.testing.assert_array_equal(pred_dijkstra, pred_fw)
