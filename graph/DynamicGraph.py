import numpy as np
import math
from collections import deque

from graph.GraphPro import GraphPro


class DynamicGraph(GraphPro):
    last_edge_updated = np.array([])
    last_edge_action = ""
    last_node_updated = {
        'node': None,
        'source': np.array([]),
        'target': np.array([]),
    }
    last_node_action = ""

    def __init__(
        self,
        source=[],
        target=[],
        weight=[],
        directed=True,
        set_nodes_with_num_nodes=0
    ):
        GraphPro.__init__(self, source, target, weight, directed, set_nodes_with_num_nodes)
        self.clean_vars()

    def clean_vars(self):
        self.last_edge_updated = np.array([])
        self.last_edge_action = ""
        self.last_node_updated = {
            'node': None,
            'source': np.array([]),
            'target': np.array([]),
        }
        self.last_node_action = ""

    def dynamic_decreasing_random_edge(self):
        count_max = 100
        flag = 0
        while True:
            source = np.random.choice(self.nodes, 1)[0]
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

        self.source = np.delete(self.source, index)
        self.target = np.delete(self.target, index)
        self.weight = np.delete(self.weight, index)

        self.last_edge_updated = np.array([source, target])
        self.last_edge_action = "DELETE"

        self.sort_sources()

        return {
            "last_edge_updated": self.last_edge_updated,
            "last_edge_action": self.last_edge_action
        }

    def dynamic_incremental_random_edge(self, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9]):

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
        return self.dynamic_incremental_edge(source, target, w)

    def dynamic_incremental_edge_middle(self, weight=1):
        self.clean_vars()

        mid_node = len(self.nodes) // 2

        return self.dynamic_incremental_edge(mid_node-1, mid_node, weight)

    def dynamic_incremental_edge(self, source, target, weight=1):
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

    def dynamic_incremental_random_node(self, num_edges=1, weights=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
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

        self.sort_sources()

        return self.dynamic_incremental_node(node, sources, w_sources, targets, w_targets)

    def dynamic_incremental_node(self, node, sources, w_sources, targets, w_targets):
        self.clean_vars()
        if self.nodes[self.nodes == node].size > 0:
            return -1

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

    def dynamic_decreasing_random_node(self):
        node = np.random.choice(self.nodes, 1)[0]
        return self.dynamic_decreasing_node(node)

    def dynamic_decreasing_node(self, node):
        self.clean_vars()
        if self.nodes[self.nodes == node].size == 0:
            return -1

        self.last_node_updated['node'] = node
        while True:
            indexes = np.where(np.logical_or(self.source == node, self.target == node))[0]
            if len(indexes) == 0:
                break
            source = self.source[indexes[0]]
            target = self.target[indexes[0]]
            self.source = np.delete(self.source, indexes[0])
            self.target = np.delete(self.target, indexes[0])

            self.last_node_updated['source'] = np.append(self.last_node_updated['source'], source)
            self.last_node_updated['target'] = np.append(self.last_node_updated['target'], target)

        self.last_node_action = "DELETE"

        self.sort_sources()

        return {
            "last_node_updated": self.last_node_updated,
            "last_node_action": self.last_node_action
        }

    def edge_update(self, source, target, weight=1):
        self.clean_vars()
        self.weight[np.logical_and(self.source == source, self.target == target)] = weight
        if not self.directed:
            self.weight[np.logical_and(self.source == target, self.target == source)] = weight

        self.last_edge_updated = np.array([source, target, weight])
        self.last_edge_action = "UPDATE"

        self.sort_sources()

        return {
            "last_edge_updated": self.last_edge_updated,
            "last_edge_action": self.last_edge_action
        }

    def edge_update_random(self, weight=1):
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

    def find_source_target_worst_scenary_incremental_edge(self):
        node_sources = {}
        node_targets = {}
        for node in self.nodes:
            node_sources[node] = self.find_total(node, "sources")
            node_targets[node] = self.find_total(node, "targets")

        print(node_sources)
        print(node_targets)
        max_path_long = 0
        node_source = 0
        node_target = 0
        for x in self.nodes:
            for y in self.nodes:
                if x == y:
                    continue

                if self.get_weight(x, y) != np.inf:
                    continue

                total_path_long = node_sources[x] * node_targets[y]
                if total_path_long > max_path_long:
                    max_path_long = total_path_long
                    node_source = x
                    node_target = y

        return {
            "source": node_source,
            "target": node_target
        }

    def find_edge_worst_scenary_update_edge(self):
        node_sources = {}
        node_targets = {}
        for node in self.nodes:
            node_sources[node] = self.find_total(node, "sources")
            node_targets[node] = self.find_total(node, "targets")

        max_path_long = 0
        node_source = 0
        node_target = 0
        for x in self.nodes:
            for y in self.nodes:
                if x == y:
                    continue

                if self.get_weight(x, y) == np.inf:
                    continue

                total_path_long = node_sources[x] + node_targets[y]
                if total_path_long > max_path_long:
                    max_path_long = total_path_long
                    node_source = x
                    node_target = y

        return {
            "source": node_source,
            "target": node_target
        }

    def find_total(self, node, to_find="sources"):
        sources = 0
        vis = [False for i in self.nodes]
        Q = deque([node])
        vis[node] = True

        while len(Q) > 0:
            x = Q.popleft()

            list = self.source[self.target == x] if to_find == 'sources' else self.target[self.source == x]

            for z in list:
                if not vis[z]:
                    vis[z] = True
                    Q.append(z)
                    sources += 1

        return sources
