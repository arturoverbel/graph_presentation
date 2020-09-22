import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.dijkstra import *

sources = [0, 0, 1, 2, 2, 3]
targets = [1, 2, 2, 3, 4, 4]
weights = [2, 3, 2, 1, 3, 1]


graph = Graph(sources, targets, weights)

graph.print_r()

dist = Dijkstra(0, graph)
print("DONE")
print(dist)
