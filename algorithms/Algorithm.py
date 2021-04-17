from graph.Graph import Graph
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *
from algorithms.knnb import *
from algorithms.eg import *
from algorithms.quinca import *
from algorithms.abm import *
from algorithms.forest import *

from time import time


def get_incremental_action():
    return [
        'insert_edge',
        'decrease_edge',
        'insert_worst_edge',
        'decrease_worst_edge'
    ]


class Algorithm:

    def __init__(self, values):
        self.attempt = 30
        self.graph = Graph.import_values(values)

    def list(self):
        return {
            'static': ['dijkstra-apsp', 'floyd-warshall'],
            'incremental': [
                'abm',
                'rr-bfs-truncated',
                'even-gazit',
                'quinca',
                'forest'
            ]
        }

    def run_algorithm(self, algorithm, dist=[[]]):

        if algorithm == 'dijkstra-apsp':
            return self.run_algorithm_dijkstra_apsp()

        if algorithm == 'floyd-warshall':
            return self.run_algorithm_floyd_warshall()

        if algorithm == 'rr-bfs-truncated':
            return self.run_algorithm_rr_bfs_truncated(dist)

        if algorithm == 'even-gazit':
            return self.run_algorithm_eg(dist)

        if algorithm == 'quinca':
            return self.run_algorithm_quinca(dist)

        if algorithm == 'abm':
            return self.run_algorithm_abm(dist)

        if algorithm == 'forest':
            return self.run_algorithm_forest(dist)

    def run_algorithm_floyd_warshall(self):
        t = time()
        Floyd_Warshall(self.graph)
        time_seconds = (time() - t) * 1000

        return self.export_algorithm(time_seconds)

    def run_algorithm_dijkstra(self, source):
        t = time()
        Dijkstra(int(source), self.graph)
        time_seconds = (time() - t) * 1000

        return self.export_algorithm(time_seconds)

    def run_algorithm_dijkstra_apsp(self):
        times = []
        for tried in range(self.attempt):
            t = time()
            Dijkstra_apsp(self.graph)
            time_seconds = (time() - t) * 1000
            times.append(time_seconds)

        return self.export_algorithm(times)

    def run_algorithm_rr_bfs_truncated(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            Bfs_Truncated_With_Sources(self.graph, dist.copy())
            time_seconds = (time() - t) * 1000
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_knnb_node_incremental(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            KNNB_Node_Incremental(self.graph, dist.copy())
            time_seconds = (time() - t) * 1000
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_eg(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            Even_Gazit(self.graph, dist.copy())
            time_seconds = (time() - t) * 1000
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_quinca(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            Quinca(self.graph, dist.copy())
            time_seconds = (time() - t) * 1000
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_abm(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            ABM_Update(self.graph, dist.copy())
            time_seconds = (time() - t) * 1000
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def run_algorithm_forest(self, dist):
        times = []
        for tried in range(self.attempt):
            t = time()
            Forest_apsp(self.graph, dist.copy())
            time_seconds = (time() - t) * 1000
            times.append(time_seconds)

        return self.export_algorithm(np.array(dist), times)

    def export_algorithm(self, dist, times):
        return times
