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


def calculate_and_export(calculate, dist_before):
    results = []
    for algorithm_name in calculate.list()['incremental']:
        result_run = calculate.run_algorithm(algorithm_name, dist_before)
        results.append({
            "algorithm": algorithm_name,
            "time": result_run['time']
        })

    file_result = "results/" + filename
    with open(file_result, 'w') as outfile:
        json.dump(results, outfile)

def import_file(filename):
    file = basePath + filename
    print("Filename: ", file)

    data_import = {}
    with open(file) as json_file:
        data_import = json.load(json_file)

    return data_import


files = []

if len(sys.argv) < 2:
    for f in os.listdir(basePath):
        if os.path.isfile(os.path.join(basePath, f)) and f.endswith(".json"):
            files.append(f)

if len(sys.argv) >= 2:
    filename = sys.argv[1]
    files.append(filename)

type_incremental = "insert_edge"
if len(sys.argv) >= 3:
    type_incremental = sys.argv[2]




    print(files)
    print("Load ", len(files), "files")

print("================== Init LAB =======================")
for filename in files:
    data_import = import_file(filename)

    dist_before = import_matrix(data_import['dist'])
    calculate = Algorithm(data_import['graph'])
    calculate.graph.stats()

    calculate_and_export(calculate, dist_before)
    print("----------------------------------------")
