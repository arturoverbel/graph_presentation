import numpy as np
import types

from reportlab.lib.validators import isInstanceOf

from graph.GraphPro import GraphPro


class DynamicGraph(GraphPro):
    last_vertex_modified = np.array([])
    last_vertex_action = ""
    last_node_modified = {
        'node': None,
        'source': np.array([]),
        'target': np.array([]),
    }
    last_node_action = ""

    def __init__(self, source=[], target=[], weight=[], directed=True):
        GraphPro.__init__(self, source, target, weight, directed)
        self.clean_vars()

    def clean_vars(self):
        self.last_vertex_modified = np.array([])
        self.last_vertex_action = ""
        self.last_node_modified = {
            'node': None,
            'source': np.array([]),
            'target': np.array([]),
        }
        self.last_node_action = ""

    def dynamic_decreasing_random_edge(self):
        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.vertex, 1)[0]
            choisen = self.target[source == self.source]
            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                break
            flag = flag + 1
            if flag >= count_max:
                return -2

        return self.dynamic_decreasing_edge(source, target)

    def dynamic_decreasing_edge(self, source, target):
        self.clean_vars()

        index = np.where(np.logical_and(self.source == source, self.target == target))[0][0]
        returned = np.array([])

        self.source = np.delete(self.source, index)
        returned = np.append(returned, source)

        self.target = np.delete(self.target, index)
        returned = np.append(returned, target)

        self.weight = np.delete(self.weight, index)

        self.last_vertex_modified = returned
        self.last_vertex_action = "DELETE"

        return returned

    def dynamic_incremental_random_edge(self, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9]):

        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.vertex, 1)[0]
            index_for_target = np.invert(np.logical_or(np.in1d(self.vertex, self.target[source == self.source]), self.vertex == source))

            choisen = self.vertex[index_for_target]
            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                break
            flag = flag + 1
            if flag >= count_max:
                return -2

        w = np.random.choice(weights)
        return self.dynamic_incremental_edge(source, target, w)

    def dynamic_incremental_edge(self, source, target, weight=1):
        self.clean_vars()

        returned = np.array([])
        self.source = np.append(self.source, source)
        returned = np.append(returned, source)
        self.target = np.append(self.target, target)
        returned = np.append(returned, target)
        self.weight = np.append(self.weight, weight)
        returned = np.append(returned, weight)

        self.last_vertex_modified = returned
        self.last_vertex_action = "ADD"

        return returned

    def dynamic_incremental_node(self, node, sources, w_sources, targets, w_targets):
        self.clean_vars()
        if self.vertex[self.vertex == node].size > 0:
            return -1

        sources = np.array(sources)
        targets = np.array(targets)
        self.source = np.concatenate((self.source, sources, np.full(targets.size, node)))
        self.target = np.concatenate((self.target, np.full(sources.size, node), targets))
        self.weight = np.concatenate((self.weight, w_sources, w_targets))
        self.vertex = np.append(self.vertex, node)

        self.last_node_modified['node'] = node
        self.last_node_modified['source'] = sources
        self.last_node_modified['target'] = targets
        self.last_node_action = "ADD"

        return self.last_node_modified

    def dynamic_decreasing_node(self, node):
        self.clean_vars()
        if self.vertex[self.vertex == node].size == 0:
            return -1

        index = np.where(np.logical_or(self.source == node, self.target == node))[0]
        for i in index:
            self.source = np.delete(self.source, index)
            self.target = np.delete(self.target, index)
            returned = np.append(returned, source)
        print(index)

        return self.last_node_modified

    def vertex_update(self, source, target, weight=1):
        self.clean_vars()
        self.weight[np.logical_and(self.source == source, self.target == target)] = weight
        if not self.directed:
            self.weight[np.logical_and(self.source == target, self.target == source)] = weight

        self.last_vertex_modified = np.array([source, target, weight])
        self.last_vertex_action = "UPDATE"
        return True

    def vertex_update_random(self, weight=1):
        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.vertex, 1)[0]
            index_for_target = np.logical_or(np.in1d(self.vertex, self.target[source == self.source]), self.vertex == source)
            choisen = self.vertex[index_for_target]

            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                if self.get_weight(source, target) > 1:
                    break

            flag = flag + 1
            if flag >= count_max:
                return -2

        return self.vertex_update(source, target, weight=weight)
