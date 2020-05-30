import os
import sys
import json
import sys
import numpy as np
from time import time
import pandas as pd

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

num_try = 20
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

filename = "graph_"+ str(num_nodes) +"_" + str(probability_edges) + ".json"

results = []

for i in range(num_try):
    print("Loading graph [" + str(num_nodes) + ", " + str(probability_edges) + "]", i, " of ", num_try)
    graph = Graph.creategraph(num_nodes, probability_edges)
    dist_before = Dijkstra_apsp(graph)

    if type_incremental == "decrease_worst_edge":
        graph.decrease_worst_weight()
    elif type_incremental == "insert_worst_edge":
        graph.insert_worst_edge()
    elif type_incremental == "decrease_edge":
        graph.decrease_random_weight()
    else:
        graph.insert_random_edge(weights=[1])

    calculate = Algorithm(graph.export_values())
    calculate.attempt = 30

    for algorithm_name in calculate.list()['incremental']:
        times = calculate.run_algorithm(algorithm_name, dist_before)
        for time in times:
            results.append({
                "algorithm": algorithm_name,
                "time": time,
                "nodes": len(calculate.graph.nodes),
                "edges": len(calculate.graph.source),
                "density": calculate.graph.get_density(),
                "type": type_incremental
            })

df = pd.DataFrame(results)
filenameFinal = filename.replace("graph", type_incremental)
filenameFinal = filenameFinal.replace("json", "csv")
filenameFinal = 'results_many_random/' + filenameFinal
print("To export: ", filenameFinal)
df.to_csv (filenameFinal, index=False, header=True)
