from graph.Graph import Graph
from server.Services import Services
from algorithms.floyd_warshall import *


class GraphServices(Services):
    def __init__(self):
        Services.__init__(self)

    def create_graph(self, num_nodes, probability_edges, directed):
        print("Generate. Nodes[" + str(num_nodes) + "] Edges[" + str(probability_edges) + "] Direc[" + str(directed)+ "]")
        graph = Graph.creategraph(num_nodes, probability_edges, directed=directed)

        return self.export(graph)

    def create_graph_and_incremental_edge(self, num_nodes, probability_edges, directed):
        graph = Graph.creategraph(num_nodes, probability_edges, directed=directed)
        dist = Floyd_Warshall(graph)
        graph.dynamic_incremental_random_edge()

        return {
            "graph": self.export(graph),
            "dist": self.export_matrix(dist)
        }

    def dynamic_incremental_random_edge(self, values):
        graph = Graph.import_values(values)
        graph.dynamic_incremental_random_edge()

        return self.export(graph)

    def dynamic_decreasing_random_edge(self, values):
        graph = Graph.import_values(values)
        graph.dynamic_decreasing_random_edge()

        return self.export(graph)

    def dynamic_update_random_edge(self, values):
        graph = Graph.import_values(values)
        graph.edge_update_random()

        return self.export(graph)
