import os
import sys
import json
import sys
import numpy as np
from time import time

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.Algorithm import Algorithm
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *

def export_matrix(matrix_result):

    matrix_to_export = []
    for row in matrix_result:
        matrix_to_export.append([
            str(a) if a == np.inf else str(int(a))
            for a in row
        ])

    return matrix_to_export

num_try = 30
num_nodes = 100
probability_edges = 0.1
type_incremental = "insert_edge"


if len(sys.argv) < 3:
    print("Faltan argumentos")
    exit()

if len(sys.argv) >= 3:
    num_nodes = int(sys.argv[1])
    probability_edges = float(sys.argv[2])
    pp = int(float(sys.argv[2]) * 100)

type_incremental = "insert_edge"
if len(sys.argv) >= 4:
    type_incremental = sys.argv[3]

filename = "graph_"+ str(num_nodes) +"_" + str(probability_edges) + "_" + type_incremental + ".json"

print("Creating graph...")
graph = Graph.creategraph(num_nodes, probability_edges)
print("Graph created")
print("Running calculate dist...")
t = time()
#dist = Floyd_Warshall(graph)
dist = Dijkstra_apsp(graph)
time_seconds = time() - t
print("Dist [] Done")

graph_values = {
    "graph": graph.export_values(),
    "dist": export_matrix(dist),
    'time_fw': time_seconds
}

results = []

for i in range(num_try):
    graph = Graph.creategraph(num_nodes, probability_edges)
    dist_before = Dijkstra_apsp(graph)

    if type == "decrease_worst_edge":
        graph.decrease_worst_weight()
    elif type == "insert_worst_edge":
        graph.insert_worst_edge()
    elif type == "decrease_edge":
        graph.decrease_random_weight()
    else:
        graph.insert_random_edge(weights=[1])

    calculate = Algorithm(graph.export_values())

    for algorithm_name in calculate.list()['incremental']:
        result_run = calculate.run_algorithm(algorithm_name, dist_before)
        results.append({
            "algorithm": algorithm_name,
            "mean_times": result_run['mean_times'],
            "stdev_times": result_run['stdev_times'],
            "nodes": len(graph.nodes),
            "edges": len(graph.source),
            "density": graph.get_density(),
            "type": type_incremental
        })

file_result = "results_z/" + filename
with open(file_result, 'w') as outfile:
    json.dump(results, outfile)
