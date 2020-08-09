from folder import get_folder
from time import time
import pandas as pd
import numpy as np
import json
import sys
import sys
import os

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


def run(
    type_incremental,
    num_nodes,
    probability_edges,
    num_try=30,
    attempt=10,
    saveFileExec=True,
    labExec=True,
    printer=True
):
    ## Define params
    labExec = bool(labExec)
    saveFileExec = bool(saveFileExec)
    num_nodes = int(num_nodes)
    num_try = int(num_try)
    attempt = int(attempt)
    probability_edges = float(probability_edges)
    results = []

    dirGraphs =  get_folder("synthetics", type_incremental, num_nodes, probability_edges)
    dirResults =  get_folder("results", type_incremental, num_nodes, probability_edges)

    if printer:
        print("=============================================")
        print("Num nodes: ", num_nodes)
        print("Probability Edge: ", probability_edges)
        print("Graph count: ", num_try)
        print("Try algorithms: ", num_try)
        print("Exporting graphs: ", saveFileExec)
        print("Exec algorithms: ", labExec)
        print("\n")


    ### Define lab for exec

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
        calculate.attempt = attempt

        ### Save graph

        if saveFileExec:
            graph_values = {
                "graph": graph.export_values(),
                "dist": export_matrix(dist_before)
            }
            filename = dirGraphs + "g_" + str(i) + ".json"

            with open(filename, 'w') as outfile:
                json.dump(graph_values, outfile)

        ### Exec lab and save on results[]

        if labExec:
            for algorithm_name in calculate.list()['incremental']:
                times = calculate.run_algorithm(algorithm_name, dist_before)
                for time in times:
                    results.append({
                        "algorithm": algorithm_name,
                        "time": time,
                        "nodes": len(calculate.graph.nodes),
                        "edges": len(calculate.graph.source),
                        "density": probability_edges,
                        "type": type_incremental
                    })

    ### Set Data Frame
    df = pd.DataFrame(results)
    filename = dirResults + "result.csv"

    if labExec:
        if printer:
            print("To export: ", filename)
        df.to_csv (filename, index=False, header=True)

    print("END")

    return {
        "dataframe": df,
        "filename": filename
    }
