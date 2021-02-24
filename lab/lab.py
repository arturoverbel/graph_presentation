from generate_and_result import run
import sys

"""
### REFERENCE
types = ['insert_edge', 'decrease_edge', 'insert_worst_edge', 'decrease_worst_edge']
num_nodes = [100,1000,10000]
probability_edges = [0.1, 0.2, 0.3, 0.4, 0.5, 0.01, 0.02, 0.03, 0.04, 0.05]

/*
 * Generate graphs on /synthetics
 * and results .josn on /results
 */
python3 lab.py insert_worst_edge 100 0.1

For draw =>

python3 draw.py

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
    exit("Don't enough args")

type_exec = sys.argv[1]
num_nodes_exec = sys.argv[2]
probability_exec = sys.argv[3]

exec(type_exec=type_exec, num_nodes_exec=num_nodes_exec,probability_exec=probability_exec)
