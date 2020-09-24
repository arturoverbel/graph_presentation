import os
import sys
import numpy as np
from time import time

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.dijkstra import *
from algorithms.eg import *
from algorithms.rr import *
from algorithms.quinca import *
from algorithms.forest import *

sources = [0, 0, 1, 2, 2, 3]
targets = [1, 2, 2, 3, 4, 4]
weights = [2, 3, 2, 1, 3, 1]


graph = Graph(sources, targets, weights)

graph.print_r()

dist = Dijkstra_apsp(graph)

print("DONE")
print(dist)

print(graph.insert_worst_edge())

#t = time()
#Even_Gazit(graph, dist.copy())
#print( "Time: ", (time() - t) * 1000 )
#3.00

#t = time()
#Bfs_Truncated_With_Sources(graph, dist.copy())
#print( "Time: ", (time() - t) * 1000 )
#4.86

#t = time()
#Quinca(graph, dist.copy())
#print( "Time: ", (time() - t) * 1000 )
#2.86

t = time()
Forest_apsp(graph, dist.copy())
print( "Time: ", (time() - t) * 1000 )
#3.012
