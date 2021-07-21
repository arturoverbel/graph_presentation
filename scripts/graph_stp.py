import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms_prev.dijkstra_prev import *
from algorithms_prev.floyd_warshall_prev import *
from algorithms_prev.abm_pred import *

"""
sources = [0, 0, 1, 1, 1, 2, 2, 2]
targets = [3, 4, 2, 3, 4, 1, 3, 4]
weights = [8, 6, 4, 5, 2, 9, 8, 5]
"""
#Grafo con más de una misma solución

sources = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]
targets = [1, 2, 5, 0, 3, 4, 5, 5, 3, 4, 0, 1, 0, 1, 4, 5, 0, 2, 3, 5, 1]
weights = [9, 6, 3, 6, 8, 7, 5, 4, 4, 4, 5, 1, 4, 4, 9, 2, 9, 7, 1, 4, 6]

"""
sources = [0, 0, 1, 3, 3]
targets = [1, 2, 2, 4, 5]
weights = [1, 1, 1, 1, 1]
"""

graph = Graph(sources, targets, weights)

#Grafos Aleatorios
"""
graph = Graph.creategraph(6, .8)
"""

graph.print_r()

print("-----------------------------------------")
dist, pred = Floyd_Warshall_PREV(graph)
print(pred)

#graph.insert_edge(4, 1, 2)
graph.insert_edge(5, 4, 1)
#graph.insert_edge(2, 3, 1)


print("-----------------------------------------")
dist, pred2 = ABM_Update_PRED(graph, dist, pred.copy())
print(pred2)

print("-----------------------------------------")
dist, pred3 = Floyd_Warshall_PREV(graph)
print(pred3)
