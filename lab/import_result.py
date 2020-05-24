import os
import sys
import json
import numpy as np

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.Algorithm import Algorithm


basePath = "synthetics/"


def import_matrix(matrix_result):

    matrix_to_import = []
    for row in matrix_result:
        matrix_to_import.append([
            np.inf if a == "inf" else int(a)
            for a in row
        ])

    return np.array(matrix_to_import)


def calculate_and_export(calculate, type, dist_before):
    results = []

    if type == "decrease_worst_edge":
        calculate.graph.decrease_worst_weight()
    elif type == "insert_worst_edge":
        calculate.graph.insert_worst_edge()
    else:
        calculate.graph.insert_random_edge(weights=[1])

    for algorithm_name in calculate.list()['incremental']:
        result_run = calculate.run_algorithm(algorithm_name, dist_before)
        results.append({
            "algorithm": algorithm_name,
            "mean_times": result_run['mean_times'],
            "stdev_times": result_run['stdev_times'],
            "nodes": len(calculate.graph.nodes),
            "edges": len(calculate.graph.source),
            "density": calculate.graph.get_density(),
            "type": type
        })

    file_result = "results/" + filename.replace("graph", type)
    with open(file_result, 'w') as outfile:
        json.dump(results, outfile)

def import_file(filename):
    file = basePath + filename
    print("Filename: ", file)

    data_import = {}
    with open(file) as json_file:
        data_import = json.load(json_file)

    return data_import

type_incremental = "insert_edge"
if len(sys.argv) >= 2:
    type_incremental = sys.argv[1]


files = []

if len(sys.argv) < 3:
    for f in os.listdir(basePath):
        if os.path.isfile(os.path.join(basePath, f)) and f.endswith(".json"):
            files.append(f)

if len(sys.argv) >= 3:
    filename = sys.argv[2]
    files.append(filename)


print("Load ", len(files), "files")

print("================== Init LAB =======================")
for filename in files:
    data_import = import_file(filename)

    dist_before = import_matrix(data_import['dist'])
    calculate = Algorithm(data_import['graph'])

    calculate.graph.stats()

    calculate_and_export(calculate, type_incremental, dist_before)
    print("----------------------------------------")
