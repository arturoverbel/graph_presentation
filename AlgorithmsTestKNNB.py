from graph.Graph import Graph
from algorithms.knnb import *
from algorithms.floyd_warshall import *

sources = [1, 2, 3, 0, 2, 3]
targets = [0, 0, 0, 4, 1, 1]
weights = [3, 2, 4, 1, 3, 2]

graph = Graph(sources, targets, weights, True)
source = 1

dist = Floyd_Warshall(graph)
print(dist)

graph.dynamic_incremental_random_node(num_edges=3)

print("<--------KNNB node incremental------->\n")

new_dist_knnb = KNNB_Node_Incremental(graph, dist)
print(new_dist_knnb)

dist2 = Floyd_Warshall(graph)
print(dist2)

graph.draw()
