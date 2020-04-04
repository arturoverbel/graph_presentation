from graph.Graph import Graph
import numpy as np


class Services:
    def __init__(self):
        pass

    def export(self, graph, matrix_result=[[]]):

        return self.export_to_cytoscape(graph, matrix_result)

    def export_algorithm(self, dist, time):

        return {
            'matrix': self.export_matrix(dist),
            'time': time
        }

    def export_matrix(self, matrix_result):

        matrix_to_export = []
        for row in matrix_result:
            matrix_to_export.append([
                str(a) if a == np.inf else str(int(a))
                for a in row
            ])

        return matrix_to_export

    def import_matrix(self, matrix_result):

        matrix_to_import = []
        for row in matrix_result:
            matrix_to_import.append([
                np.inf if a == "inf" else float(int(a))
                for a in row
            ])

        return matrix_to_import

    def export_to_cytoscape(self, graph, matrix_result=[[]]):
        size_nodes = range(graph.nodes.size)
        size_edges = range(graph.source.size)
        directed = 'true' if graph.directed else 'false'

        nodes = []
        for i in size_nodes:
            nodes.append({
                'data': {
                    'id': str(int(graph.nodes[i]))
                }
            })

        edges = []
        for i in size_edges:
            edges.append({
                'data': {
                    'id': str(int(graph.source[i])) + '-' + str(int(graph.target[i])),
                    'source': str(int(graph.source[i])),
                    'target': str(int(graph.target[i])),
                    'label': str(int(graph.weight[i])),
                    'directed': directed
                },
                'clasess': 'default'
            })

        return {
            'elements': {
                'nodes': nodes,
                'edges': edges
            },
            'values': graph.export_values()
        }
