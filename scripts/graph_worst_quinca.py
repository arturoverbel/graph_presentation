import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.quinca import *

num_nodes = 100
g = Graph.creategraph_for_worst_escenary_edge_insert(num_nodes)

result_before_dist = np.array(Floyd_Warshall(g))


g.dynamic_incremental_edge_middle()

dist_rr = Quinca(g, result_before_dist)
