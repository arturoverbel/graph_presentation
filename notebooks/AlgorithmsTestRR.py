from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *
from algorithms.rr import *

sources = [1, 2, 3, 0, 2]
targets = [0, 0, 0, 4, 1]
weights = [3, 2, 4, 1, 3]

graph = Graph(sources, targets, weights, True)
source = 1

dist_source = Dijkstra(source, graph)
#print(dist_source)

dist = Dijkstra_apsp(graph)
#print(dist)

dist = Floyd_Warshall(graph)
print(dist)

graph.dynamic_incremental_edge(source=4, target=3, weight=1)

print("<--------Dijkstra_Truncated------->\n")

#dist_source_rr = Dijkstra_Truncated(graph, dist_source)
#print(dist_source_rr)

sources_affected = Find_Affected_Sources(graph, dist)
print(sources_affected)

print("<--------Bfs_Truncated------->\n")

#dist_rr = Bfs_Truncated(graph, source, dist)
#print(dist_rr)

#dist_rr_all = Bfs_Truncated_With_Sources(graph, dist)
#print(dist_rr_all)

#dist2 = Floyd_Warshall(graph)
#print(dist2)

#graph.draw()
