from graph.Graph import Graph
from server.Services import Services
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *
from algorithms.rr import *
from time import time

class GraphAlgorithms(Services):
    def __init__(self):
        Services.__init__(self)

    def run_algoritm_floyd_warshall(self, values):
        graph = Graph.import_values(values)
        t = time()
        dist = Floyd_Warshall(graph)
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)

    def run_algoritm_dijkstra(self, values, source):
        graph = Graph.import_values(values)
        t = time()
        dist = Dijkstra(int(source), graph)
        time_seconds = time() - t

        return self.export_algorithm([dist], time_seconds)

    def run_algoritm_dijkstra_apsp(self, values):
        graph = Graph.import_values(values)
        t = time()
        dist = Dijkstra_apsp(graph)
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)

    def run_algoritm_rr_bfs_truncated(self, values, dist):
        graph = Graph.import_values(values)
        matrix_distances = self.import_matrix(dist)

        print(graph.last_vertex_modified)
        t = time()
        dist = Bfs_Truncated_With_Sources(graph, matrix_distances)
        time_seconds = time() - t

        return self.export_algorithm(dist, time_seconds)
