import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph

num_nodes = 9
g = Graph.creategraph_for_worst_escenary_edge_insert(num_nodes)
g.dynamic_incremental_edge_middle()

g.draw()
