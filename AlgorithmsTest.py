from graph.Graph import Graph
from algorithms.dijkstra import *
from algorithms.floyd_warshall import *

sources = [1, 2, 3, 0, 4, 1, 2, 1, 3]
targets = [0, 0, 0, 4, 0, 2, 1, 3, 1]
weights = [2, 2, 4, 1, 1, 3, 3, 2, 2]

print("<--------Test Create------->\n")

graph = Graph(sources, targets, weights)
graph.print_r()

dist = Dijkstra(1, graph)
print(dist)

dist = Dijkstra_apsp(graph)
print(dist)

dist = Floyd_Warshall(graph)
print(dist)

#graph.draw()
