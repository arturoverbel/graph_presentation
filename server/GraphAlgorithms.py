from graph.Graph import Graph
from server.Services import Services
from algorithms.floyd_warshall import *
from algorithms.dijkstra import *


class GraphAlgorithms(Services):
    def __init__(self):
        Services.__init__(self)

    def run_algoritm_floyd_warshall(self, values):
        graph = Graph.import_values(values)
        dist = Floyd_Warshall(graph)

        return self.export_matrix(dist)

    def run_algoritm_dijkstra(self, values, source):
        graph = Graph.import_values(values)
        dist = Dijkstra(int(source), graph)

        return self.export_matrix([dist])

    def run_algoritm_dijkstra_apsp(self, values):
        graph = Graph.import_values(values)
        dist = Dijkstra_apsp(graph)

        return self.export_matrix(dist)
