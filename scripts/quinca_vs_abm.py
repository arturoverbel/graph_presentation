import os
import sys
from time import time
import statistics

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph
from algorithms.quinca import *
from algorithms.abm import *
from algorithms.floyd_warshall import *
from algorithms.eg import *

# Data for Graph
repetitions = 5
num_nodes = 100
probability_edges = 0.4

#GRaph Incremental
graph = Graph.creategraph(num_nodes, probability_edges)
result_before_dist = np.array(Floyd_Warshall(graph))
graph.insert_worst_edge()


al_quinca = True
al_abm = True
al_eg = True

#QUINCA
if al_quinca:
    time_list_quinca = []
    for i in range(repetitions):
        t = time()
        dist = Quinca(graph, result_before_dist.copy())
        time_miliseconds = (time() - t) * 1000
        print("Quinca: ", time_miliseconds)
        time_list_quinca.append(time_miliseconds)

    print("======Quinca: ", statistics.mean(time_list_quinca), statistics.stdev(time_list_quinca))

#ABM
if al_abm:
    time_list_abm = []
    for i in range(repetitions):
        t2 = time()
        dist2 = ABM_Update(graph, result_before_dist.copy())
        time_miliseconds2 = (time() - t2) * 1000
        print("Abm: ", time_miliseconds2)
        time_list_abm.append(time_miliseconds2)

    print("======ABM: ", statistics.mean(time_list_abm), statistics.stdev(time_list_abm))

#EG
if al_eg:
    time_list_eg = []
    for i in range(repetitions):
        t3 = time()
        dist3 = Even_Gazit(graph, result_before_dist.copy())
        time_miliseconds3 = (time() - t3) * 1000
        print("EG: ", time_miliseconds3)
        time_list_eg.append(time_miliseconds3)

    print("======EG: ", statistics.mean(time_list_eg), statistics.stdev(time_list_eg))
