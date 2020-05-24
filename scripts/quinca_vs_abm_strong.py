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


## Data graph
repetitions = 10
num_nodes = 300
num_nodes_max = 301
probability_edges = 0.4
multliplicador = 1000



for num_notes_current in range(num_nodes, num_nodes_max):

    print("----------------------------------------------")
    print("Nodes: ", num_notes_current)

    time_list_abm = []
    for i in range(repetitions):
        graph2 = Graph.creategraph(num_notes_current, probability_edges)
        result_before_dist2 = np.array(Floyd_Warshall(graph2))
        graph2.insert_worst_edge()

        ## Warm
        for i in range(5):
            dist111 = Quinca(graph2, result_before_dist2)
            dist1112 = ABM_Update(graph2, result_before_dist2)
            dist1113 = Even_Gazit(graph2, result_before_dist2)

        t2 = time()
        dist2 = ABM_Update(graph2, result_before_dist2)
        time_miliseconds2 = (time() - t2) * multliplicador
        time_list_abm.append(time_miliseconds2)
        print("abm: ", time_miliseconds2)

    print("==========ABM: ", statistics.mean(time_list_abm))

    ## QUINCA

    time_list_quinca = []
    for i in range(repetitions):
        graph = Graph.creategraph(num_notes_current, probability_edges)
        result_before_dist = np.array(Floyd_Warshall(graph))
        graph.insert_worst_edge()

        ## Warm
        for i in range(5):
            dist111 = Quinca(graph, result_before_dist)
            dist1112 = ABM_Update(graph, result_before_dist)
            dist1113 = Even_Gazit(graph, result_before_dist)

        t = time()
        dist = Quinca(graph, result_before_dist)
        time_miliseconds = (time() - t) * multliplicador
        time_list_quinca.append(time_miliseconds)
        print("Quinca: ", time_miliseconds)

    print("=======QUINCA: ", statistics.mean(time_list_quinca))


    time_list_eg = []
    for i in range(repetitions):
        graph3 = Graph.creategraph(num_notes_current, probability_edges)
        result_before_dist3 = np.array(Floyd_Warshall(graph3))
        graph3.insert_worst_edge()

        ## Warm
        for i in range(5):
            dist111 = Quinca(graph3, result_before_dist3)
            dist1112 = ABM_Update(graph3, result_before_dist3)
            dist1113 = Even_Gazit(graph3, result_before_dist3)

        t = time()
        dist = Even_Gazit(graph3, result_before_dist3)
        time_miliseconds3 = (time() - t) * multliplicador
        print("EG: ", time_miliseconds3)
        time_list_eg.append(time_miliseconds3)

    print("========EG: ", statistics.mean(time_list_eg))
