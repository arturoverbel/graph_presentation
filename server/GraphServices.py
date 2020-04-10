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

    def create_graph_and_insert_random_edge(self, num_nodes, probability_edges, directed):
        graph = Graph.creategraph(num_nodes, probability_edges, directed=directed)
        dist = Floyd_Warshall(graph)
        graph.insert_random_edge()

        return {
            "graph": self.export(graph),
            "dist": self.export_matrix(dist)
        }

    def create_graph_and_insert_worst_edge(self, num_nodes, directed):
        graph = Graph.creategraph_for_worst_escenary_edge_insert(num_nodes, directed=directed)
        dist = Floyd_Warshall(graph)
        graph.dynamic_incremental_edge_middle()

        return {
            "graph": self.export(graph),
            "dist": self.export_matrix(dist)
        }

    def create_graph_and_insert_random_node(self, num_nodes, probability_edges, directed):
        graph = Graph.creategraph(num_nodes, probability_edges, directed=directed)
        dist = Floyd_Warshall(graph)
        graph.insert_random_node()

        return {
            "graph": self.export(graph),
            "dist": self.export_matrix(dist)
        }

    def create_graph_and_decrease_random_weight(self, num_nodes, probability_edges, directed):
        graph = Graph.creategraph(num_nodes, probability_edges, directed=directed)
        dist = Floyd_Warshall(graph)
        graph.decrease_random_weight()

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
