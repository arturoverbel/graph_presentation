import os
import sys
import json
import sys
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.floyd_warshall import *

def export_matrix(matrix_result):

    matrix_to_export = []
    for row in matrix_result:
        matrix_to_export.append([
            str(a) if a == np.inf else str(int(a))
            for a in row
        ])

    return matrix_to_export

num_nodes = 100
probability_edges = 0.1
filename = "graph.json"

if len(sys.argv) == 3:
    num_nodes = int(sys.argv[1])
    probability_edges = float(sys.argv[2]) * 2
    pp = int(float(sys.argv[2]) * 100)
    filename = "synthetics/graph_" + str(num_nodes) + "_" + str(sys.argv[2]) + ".json"
else:
    print("Faltan argumentos")
    exit()


graph = Graph.creategraph(num_nodes, probability_edges)
dist = Floyd_Warshall(graph)
graph.insert_random_edge(weights=[1])

graph_values = {
    "graph": graph.export_values(),
    "dist": export_matrix(dist)
}

print("-------------------------")
print("Filename: " + filename)
graph.stats()

with open(filename, 'w') as outfile:
    json.dump(graph_values, outfile)
