from graph.Graph import Graph


class GraphServices:

    def __init__(self):
        pass

    @staticmethod
    def create_graph(num_nodes, probability_edges):
        graph = Graph.creategraph(num_nodes, probability_edges)
        return graph.export_arrays()
