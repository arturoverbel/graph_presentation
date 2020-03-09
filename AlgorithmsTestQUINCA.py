from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.quinca import *

sources = [1, 2, 3, 0, 2, 3]
targets = [0, 0, 0, 4, 1, 1]
weights = [3, 2, 4, 1, 3, 2]

graph = Graph(sources, targets, weights, True)

dist = Floyd_Warshall(graph)
print(dist)

graph.dynamic_incremental_edge(source=4, target=3, weight=1)

print("<--------QUINCA------->\n")

dist_eg = Quinca(graph, dist)
print(dist_eg)

print("<-------- Floyd Warshall------->\n")

dist2 = Floyd_Warshall(graph)
print(dist2)

#graph.draw()
