import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.quinca import *
from algorithms.floyd_warshall import *
from algorithms.rr import *

def find_total(graph, v, to_find="sources"):
    sources = 0

    vis = [False for i in graph.nodes]

    Q = deque([v])
    vis[v] = True

    while len(Q) > 0:
        x = Q.popleft()

        list = graph.source[graph.target == x] if to_find == 'sources' else graph.target[graph.source == x]

        for z in list:
            if not vis[z]:
                vis[z] = True
                Q.append(z)
                sources += 1

    return sources

sources = [1, 2, 3, 0, 2, 3, 1, 2]
targets = [0, 0, 0, 4, 1, 1, 5, 5]
weights = [2, 2, 4, 1, 3, 2, 2, 2]

graph = Graph(sources, targets, weights)

node_sources = {}
for node in graph.nodes:
    total = find_total(graph, node, "sources")
    node_sources[node] = total

node_targets = {}
for node in graph.nodes:
    total = find_total(graph, node, "targets")
    node_targets[node] = total

print(node_sources)
print(node_targets)


max_path_long = 0
node_source = 0
node_target = 0
for x in graph.nodes:
    for y in graph.nodes:
        if x == y:
            continue

        total_path_long = node_sources[x] + node_targets[y]
        print(x, y, "::", total_path_long)
        if total_path_long > max_path_long:
            max_path_long = total_path_long
            node_source = x
            node_target = y

print(node_source, node_target)




#print("Worst scenary: ", source_worst_scenary, target_worst_scenary)
