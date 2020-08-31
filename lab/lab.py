from generate_and_result import run
from export_fig import draw_all_plot, draw_group_plot
from folder import get_folder
import pandas as pd
import sys
from os import listdir
from os.path import isfile, join

"""
### REFERENCE
types = ['insert_edge', 'decrease_edge', 'insert_worst_edge', 'decrease_worst_edge']
num_nodes = [100,1000,10000]
probability_edges = [0.1, 0.2, 0.3, 0.4, 0.5, 0.01, 0.02, 0.03, 0.04, 0.05]

python3 lab.py insert_worst_edge 100 0.1
"""
def exec(
    type_exec,
    num_nodes_exec,
    probability_exec,
    num_graphs_random=30,
    try_exec_each_graph=10
):
    # Dataframe
    result = run(
        type_exec,
        num_nodes_exec,
        probability_exec,
        num_try = num_graphs_random,
        attempt = try_exec_each_graph,
        saveFileExec = True,
        labExec=True
    )

if len(sys.argv) != 4:
    exit("Faltan argumentos")

type_exec = sys.argv[1]
num_nodes_exec = sys.argv[2]
probability_exec = sys.argv[3]

exec(type_exec=type_exec, num_nodes_exec=num_nodes_exec,probability_exec=probability_exec)
