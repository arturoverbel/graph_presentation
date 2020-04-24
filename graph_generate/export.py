import os
import sys
import json
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph

num_nodes = 100
probability_edges = 0.1
filename = "graph.json"

if len(sys.argv) == 3:
    num_nodes = int(sys.argv[1])
    probability_edges = float(sys.argv[2]) * 2
    pp = int(float(sys.argv[2]) * 100)
    filename = "graph_" + str(num_nodes) + "_" + str(pp) + ".json"
else:
    print("Faltan argumentos")
    exit()


graph = Graph.creategraph(num_nodes, probability_edges)
graph.insert_random_edge(weights=[1])
print("Filename: " + filename)
graph.stats()

graph_values = graph.export_values()

with open(filename, 'w') as outfile:
    json.dump(graph_values, outfile)
