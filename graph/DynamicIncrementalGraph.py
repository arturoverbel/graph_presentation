import numpy as np
import math

from graph.DynamicGraph import DynamicGraph


class DynamicIncrementalGraph(DynamicGraph):

    def __init__(
        self,
        source=[],
        target=[],
        weight=[],
        directed=True,
        set_nodes_with_num_nodes=0
    ):
        DynamicGraph.__init__(self, source, target, weight, directed, set_nodes_with_num_nodes)
        self.clean_vars()

    def insert_edge(self, source, target, weight=1):
        self.clean_vars()

        self.source = np.append(self.source, source)
        self.target = np.append(self.target, target)
        self.weight = np.append(self.weight, weight)

        self.last_edge_updated = np.array([source, target, weight])
        self.last_edge_action = "ADD"

        self.sort_sources()

        return {
            "last_edge_updated": self.last_edge_updated,
            "last_edge_action": self.last_edge_action
        }

    def insert_worst_edge(self, weight=1):
        self.clean_vars()

        result_found = self.find_source_target_worst_scenary_incremental_edge()
        source = result_found['source']
        target = result_found['target']

        return self.insert_edge(source, target, weight)

    def insert_random_edge(self, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9]):

        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.nodes, 1)[0]
            index_for_target = np.invert(np.logical_or(np.in1d(self.nodes, self.target[source == self.source]), self.nodes == source))

            choisen = self.nodes[index_for_target]
            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                break
            flag = flag + 1
            if flag >= count_max:
                return -2

        w = np.random.choice(weights)
        return self.insert_edge(source, target, w)

    def insert_node(self, node, sources, w_sources, targets, w_targets):
        self.clean_vars()
        if self.nodes[self.nodes == node].size > 0:
            return -2

        sources = np.array(sources)
        targets = np.array(targets)
        self.source = np.concatenate((self.source, sources, np.full(targets.size, node)))
        self.target = np.concatenate((self.target, np.full(sources.size, node), targets))
        self.weight = np.concatenate((self.weight, w_sources, w_targets))
        self.nodes = np.append(self.nodes, node)

        self.last_node_updated['node'] = node
        self.last_node_updated['source'] = sources
        self.last_node_updated['target'] = targets

        self.last_node_action = "ADD"

        self.sort_sources()

        return self.last_node_updated

    def insert_random_node(self, num_edges=1, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.clean_vars()
        node = np.amax(self.nodes) + 1

        number = math.ceil(num_edges/2)
        sources = np.random.choice(self.nodes, number, replace=False)
        w_sources = np.random.choice(weights, number)

        number = num_edges - number
        if number <= 0:
            targets = []
            w_targets = []
        else:
            targets = np.random.choice(self.nodes, number, replace=False)
            w_targets = np.random.choice(weights, number)

        return self.insert_node(node, sources, w_sources, targets, w_targets)

    def decrease_weight(self, source, target, weight=1):
        self.clean_vars()
        if weight > self.get_weight(source, target):
            return -2

        self.weight[np.logical_and(self.source == source, self.target == target)] = weight
        if not self.directed:
            self.weight[np.logical_and(self.source == target, self.target == source)] = weight

        self.last_edge_updated = np.array([source, target, weight])
        self.last_edge_action = "DECREASE"

        self.sort_sources()

        return {
            "last_edge_updated": self.last_edge_updated,
            "last_edge_action": self.last_edge_action
        }

    def decrease_worst_weight(self):
        self.clean_vars()

        result_found = self.find_edge_worst_scenary_update_edge()
        source = result_found['source']
        target = result_found['target']

        weight_current = self.get_weight(source, target)
        weight_new = 0 if weight_current > 0 else -1

        return self.decrease_weight(source, target, weight=weight_new)

    def decrease_random_weight(self, weight=1):
        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.nodes, 1)[0]
            index_for_target = np.logical_or(np.in1d(self.nodes, self.target[source == self.source]), self.nodes == source)
            choisen = self.nodes[index_for_target]

            if choisen.size != 0:
                target = np.random.choice(choisen, 1)[0]
                if self.get_weight(source, target) > 1:
                    break

            flag = flag + 1
            if flag >= count_max:
                return -2

        return self.edge_update(source, target, weight=weight)
