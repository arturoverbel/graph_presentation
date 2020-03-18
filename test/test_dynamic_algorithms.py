import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.eg import *
from algorithms.quinca import *

sources = [1, 2, 3, 0, 2, 3]
targets = [0, 0, 0, 4, 1, 1]
weights = [3, 2, 4, 1, 3, 2]

graph = Graph(sources, targets, weights)
result_before_dist = Floyd_Warshall(graph)

graph.dynamic_incremental_edge(source=4, target=3, weight=1)

result_after_dist = Floyd_Warshall(graph)


def test_eg():
    dist_eg = Even_Gazit(graph, result_before_dist)
    np.testing.assert_array_equal(dist_eg, result_after_dist)


def test_quinca():
    dist_quinca = Quinca(graph, result_before_dist)
    np.testing.assert_array_equal(dist_quinca, result_after_dist)
