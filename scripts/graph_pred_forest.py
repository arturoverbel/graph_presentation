import os
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms_prev.dijkstra_prev import *
from algorithms_prev.forest_pred import *
from algorithms_prev.abm_pred import *

#Grafos Aleatorios
graph = Graph.creategraph(6, .8)
graph.print_r()

dist, prev = Dijkstra_apsp_PREV(graph)
print(prev)

#graph.dynamic_incremental_edge(source=3, target=4, weight=2)
graph.insert_worst_edge()

print("------------------FOREST-----------------------")
dist2, prev2 = Forest_apsp_PRED(graph, dist.copy(), prev.copy())
print(prev2)
print("Data is correct? ", Graph.testDistPred(dist2, prev2))

print("----------------------ABM-------------------")
dist3, prev3 = ABM_Update_PRED(graph, dist.copy(), prev.copy())
print(prev3)
print("Data is correct? ", Graph.testDistPred(dist3, prev3))
