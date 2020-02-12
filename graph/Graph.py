from graph.DynamicGraph import DynamicGraph
import numpy as np


class Graph(DynamicGraph):

    def __init__(self, source=[], target=[], weight=[], directed=True):
        DynamicGraph.__init__(self, source, target, weight, directed)

    def print_r(self):
        print("Source: ", self.source)
        print("Target: ", self.target)
        print("Weight: ", self.weight)
        print("Vertex: ", self.vertex)

    def get_weight(self, n1, n2):
        if n1 == n2:
            return 0
        w = self.weight[np.logical_and(self.source == n1, self.target == n2)]
        return np.inf if w.size == 0 else w[0]

    def export(self):
        return [(int(self.source[i]), int(self.target[i]), self.weight[i]) for i in range(self.source.size)]

    def export_arrays(self):
        size = range(self.source.size)
        return [
            [int(self.source[i]) for i in size],
            [int(self.target[i]) for i in size],
            [int(self.weight[i]) for i in size]
        ]

    @staticmethod
    def creategraph(total_nodes, pro_edges, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9], directed=True):

        source = np.array([])
        target = np.array([])
        weight = np.array([])

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

                source = np.append(source, i)
                target = np.append(target, k)
                weight = np.append(weight, w)

                if not directed:
                    source = np.append(source, k)
                    target = np.append(target, i)
                    weight = np.append(weight, w)

        return Graph(source, target, weight)
