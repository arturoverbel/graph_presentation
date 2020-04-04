from graph.DynamicIncrementalGraph import DynamicIncrementalGraph
import numpy as np


class Graph(DynamicIncrementalGraph):

    def __init__(
        self,
        source=[],
        target=[],
        weight=[],
        directed=True,
        set_nodes_with_num_nodes=0
    ):
        DynamicIncrementalGraph.__init__(self, source, target, weight, directed, set_nodes_with_num_nodes)

    def print_r(self):
        print("Source: ", self.source)
        print("Target: ", self.target)
        print("Weight: ", self.weight)
        print("Vertex: ", self.nodes)

    def get_weight(self, n1, n2):
        if n1 == n2:
            return 0
        w = self.weight[np.logical_and(self.source == n1, self.target == n2)]
        return np.inf if w.size == 0 else w[0]

    def export(self):
        return [(int(self.source[i]), int(self.target[i]), self.weight[i]) for i in range(self.source.size)]

    def export_values(self):
        directed = 'true' if self.directed else 'false'

        return {
            'source': list(np.array([str(int(x)) for x in self.source])),
            'target': list(np.array([str(int(x)) for x in self.target])),
            'weight': list(np.array([str(int(x)) for x in self.weight])),
            'nodes': list(np.array([str(int(x)) for x in self.nodes])),
            'directed': directed,
            'last_edge_action': self.last_edge_action,
            'last_edge_updated': list(np.array([str(int(x)) for x in self.last_edge_updated])),
            'last_node_action': self.last_node_action,
            'last_node_updated': {
                'node': self.last_node_updated['node'],
                'source': list(np.array([str(int(x)) for x in self.last_node_updated['source']])),
                'target': list(np.array([str(int(x)) for x in self.last_node_updated['target']]))

            }
        }

    @staticmethod
    def import_values(values):
        directed = True if values['directed'] == 'true' else False

        new_values = {
            'source': np.array([int(x) for x in values['source']]),
            'target': np.array([int(x) for x in values['target']]),
            'weight': np.array([int(x) for x in values['weight']]),
            'nodes': np.array([int(x) for x in values['nodes']]),
            'directed': directed,
            'last_edge_action': values['last_edge_action'],
            'last_edge_updated': np.array([int(x) for x in values['last_edge_updated']]),
            'last_node_action': values['last_node_action'],
            'last_node_updated': {
                'node': values['last_node_updated']['node'],
                'source': np.array([int(x) for x in values['last_node_updated']['source']]),
                'target': np.array([int(x) for x in values['last_node_updated']['target']])
            }
        }

        g = Graph(new_values['source'], new_values['target'], new_values['weight'], new_values['directed'])
        g.last_edge_action = new_values['last_edge_action']
        g.last_edge_updated = new_values['last_edge_updated']
        g.last_node_action = new_values['last_node_action']
        g.last_node_updated = new_values['last_node_updated']

        return g


    @staticmethod
    def creategraph(total_nodes, pro_edges, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9], directed=True):

        source = []
        target = []
        weight = []

        for i in range(total_nodes):
            for k in range(i+1, total_nodes):
                if k == i:
                    continue

                p = 1 - pro_edges
                has_edge = np.random.choice(2, 1, p=[p, pro_edges])[0]

                if not has_edge:
                    continue

                probabilities = np.zeros(len(weights))
                probabilities = probabilities + (1 / len(weights))
                w = np.random.choice(weights, 1, p=probabilities)[0]

                source.append(i)
                target.append(k)
                weight.append(w)

        return Graph(source, target, weight, directed, set_nodes_with_num_nodes=total_nodes)
