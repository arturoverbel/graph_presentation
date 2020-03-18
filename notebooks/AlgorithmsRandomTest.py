from graph.Graph import Graph
from algorithms.dijkstra import *
from algorithms.floyd_warshall import *


print("<--------Test Create------->\n")

graph = Graph.creategraph(4, .2)
graph.print_r()

#dist = Dijkstra_apsp(graph)
#print(dist)

dist = Floyd_Warshall(graph)
print(dist)
