import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms_prev.dijkstra_prev import *
from algorithms_prev.floyd_warshall_prev import *

graph = Graph.creategraph(9, .8)

def test_predecesors():
    d, pred_dijkstra = Dijkstra_apsp_PREV(graph)
    d, pred_fw = Floyd_Warshall_PREV(graph)

    print(pred_dijkstra)
    print(pred_fw)
    #np.testing.assert_array_equal(pred_dijkstra, pred_fw)
