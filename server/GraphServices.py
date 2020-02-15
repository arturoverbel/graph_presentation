from graph.Graph import Graph


class GraphServices:
    export_type = 'javascript'

    def __init__(self):
        pass

    def create_graph(self, num_nodes, probability_edges):
        graph = Graph.creategraph(num_nodes, probability_edges)
        return self.export(graph)

    def export(self, graph):
        print(self.export_type)
        if self.export_type == 'array':
            return graph.export_arrays()
        if self.export_type == 'default':
            return graph.export()

        return graph.export_javascript()
