from graph.Graph import Graph
from server.Services import Services
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *
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
