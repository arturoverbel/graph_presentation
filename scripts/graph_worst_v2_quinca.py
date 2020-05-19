import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.quinca import *

graph = Graph.creategraph(10, .8)
result_before_dist = np.array(Floyd_Warshall(graph))

graph.insert_worst_edge()

dist_rr = Quinca(graph, result_before_dist)


print(dist_rr)
