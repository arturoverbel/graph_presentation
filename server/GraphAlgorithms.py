from graph.Graph import Graph
from server.Services import Services
from algorithms.floyd_warshall import *


class GraphAlgorithms(Services):
    def __init__(self):
        Services.__init__(self)

    def run_algoritm_floyd_warshall(self, values):
        graph = Graph(values['source'], values['target'], values['weight'])
        dist = Floyd_Warshall(graph)

        return self.export_matrix(dist)
