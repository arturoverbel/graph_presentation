import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.quinca import *

sources = [0, 2, 2, 3, 3, 4, 5]
targets = [4, 0, 4, 5, 1, 3, 4]
weights = [3, 5, 5, 9, 8, 4, 8]
graph = Graph(sources, targets, weights)
graph.print_r()
print("Insert Worst Edge")

#graph.draw()

graph.insert_worst_edge()
graph.print_r()
print(graph.last_edge_updated)
