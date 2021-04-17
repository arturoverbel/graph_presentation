import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.quinca import *

sources = [1, 2, 3, 0, 4, 1, 2, 1, 3]
targets = [0, 0, 0, 4, 0, 2, 1, 3, 1]

graph = Graph(sources, targets)
graph.print_r()
print("Insert Worst Edge")

#graph.draw()

graph.decrease_random_weight()
graph.print_r()
print(graph.last_edge_updated)
