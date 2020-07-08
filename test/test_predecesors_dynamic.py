import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms_prev.dijkstra_prev import *
from algorithms_prev.forest_pred import *
from algorithms_prev.abm_pred import *

graph = Graph.creategraph(20, .8)
dist_before, prev_before = Dijkstra_apsp_PREV(graph)
graph.insert_worst_edge()

def test_predecesors():
    dist, pred = Forest_apsp_PRED(graph, dist_before.copy(), prev_before.copy())
    np.testing.assert_equal(True, Graph.testDistPred(dist, pred))

    dist2, pred2 = ABM_Update_PRED(graph, dist_before.copy(), prev_before.copy())
    np.testing.assert_equal(True, Graph.testDistPred(dist2, pred2))

    #np.testing.assert_array_equal(pred_dijkstra, pred_fw)
