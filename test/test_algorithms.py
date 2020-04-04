import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.dijkstra import *
from algorithms.floyd_warshall import *

sources = [1, 2, 3, 0, 4, 1, 2, 1, 3]
targets = [0, 0, 0, 4, 0, 2, 1, 3, 1]
weights = [2, 2, 4, 1, 1, 3, 3, 2, 2]

static_graph = Graph(sources, targets, weights)
result_apsp = np.array([
    [0., np.inf, np.inf, np.inf, 1.],
    [2., 0., 3., 2., 3.],
    [2., 3., 0., 5., 3.],
    [4., 2., 5., 0., 5.],
    [1., np.inf, np.inf, np.inf, 0.]
])


def test_dijkstra():
    dist_sssp = np.array(Dijkstra(1, static_graph))
    np.testing.assert_array_equal(dist_sssp, np.array([2., 0., 3., 2., 3.]))


def test_dijkstra_apsp():
    dist = np.array(Dijkstra_apsp(static_graph))
    np.testing.assert_array_equal(dist, np.array(result_apsp))


def test_floyd_warshall():
    dist = np.array(Floyd_Warshall(static_graph))
    np.testing.assert_array_equal(dist, result_apsp)
