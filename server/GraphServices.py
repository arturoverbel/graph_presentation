from graph.Graph import Graph
from server.Services import Services


class GraphServices(Services):
    def __init__(self):
        Services.__init__(self)

    def create_graph(self, num_nodes, probability_edges):
        print("Generate graph. nodes: " + str(num_nodes) + ", edges probability: ", str(probability_edges))
        graph = Graph.creategraph(num_nodes, probability_edges, directed=True)

        return self.export(graph)
