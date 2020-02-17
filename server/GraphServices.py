from graph.Graph import Graph


class GraphServices:
    export_type = 'javascript'

    def __init__(self):
        pass

    def create_graph(self, num_nodes, probability_edges):
        print("Generate graph. nodes: " + str(num_nodes) + ", edges probability: ", str(probability_edges))
        graph = Graph.creategraph(num_nodes, probability_edges)
        return self.export(graph)

    def export(self, graph):

        return self.export_to_cytoscape(graph)

    def export_to_cytoscape(self, graph):
        size_vertex = range(graph.vertex.size)
        size_edges = range(graph.source.size)
        directed = 'true' if graph.directed else 'false'

        nodes = []
        for i in size_vertex:
            nodes.append({
                'data': {
                    'id': str(int(graph.vertex[i]))
                }
            })

        edges = []
        for i in size_edges:
            edges.append({
                'data': {
                    'id': str(int(graph.source[i])) + '-' + str(int(graph.target[i])),
                    'source': str(int(graph.source[i])),
                    'target': str(int(graph.target[i])),
                    'directed': directed
                }
            })

        return {
            'nodes': nodes,
            'edges': edges
        }
