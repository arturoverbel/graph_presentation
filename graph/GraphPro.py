import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphPro:
    source = []
    target = []
    weight = []
    nodes = []

    undirected = 0

    def __init__(
        self,
        source=[],
        target=[],
        weight=[],
        directed=True,
        set_nodes_with_num_nodes=0
    ):
        self.directed = directed
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)

        if self.directed is False:
            self.source = np.concatenate([self.source, self.target])
            self.target = np.concatenate([self.target, np.array(source)])
            self.weight = np.concatenate([self.weight, self.weight])

        self.sort_sources()

        if set_nodes_with_num_nodes == 0:
            self.set_nodes()
        else:
            self.set_nodes_with_num_nodes(set_nodes_with_num_nodes)

    def set_nodes(self):
        max_nodes = max(np.concatenate([np.unique(self.source), np.unique(self.target)]))
        self.nodes = np.arange(max_nodes+1)
        return self.nodes

    def set_nodes_with_num_nodes(self, num_nodes):
        self.nodes = np.arange(num_nodes)
        return self.nodes

    def sort_sources(self):
        idx = self.source.argsort()
        self.source = self.source[idx]
        self.target = self.target[idx]
        self.weight = self.weight[idx]

    def get_targets_from_source(self, source, return_weight=False):
        start = np.searchsorted(self.source, source, side='left')
        end = np.searchsorted(self.source, source, side='right')

        if return_weight:
            return self.target[start:end], self.weight[start:end]

        return self.target[start:end]

    def draw(self, with_weight=True):
        gr = nx.DiGraph()
        gr.add_weighted_edges_from(self.export())

        list_edges = list(gr.edges())
        list_nodes = list(gr.nodes())
        last = ()
        last_nodes = []

        if self.last_edge_updated.size > 0:
            last = (int(self.last_edge_updated[0]), int(self.last_edge_updated[1]))
            if last in list_edges:
                list_edges.remove(last)
                if not self.directed:
                    list_edges.remove((self.last_edge_updated[1], self.last_edge_updated[0]))

        if self.last_node_updated is not None:
            for source in self.last_node_updated['source']:
                edge = (int(source), int(self.last_node_updated['node']))
                if edge in list_edges:
                    list_edges.remove(edge)
                last_nodes.append(edge)
            for target in self.last_node_updated['target']:
                edge = (int(self.last_node_updated['node']), int(target))
                if edge in list_edges:
                    list_edges.remove(edge)
                last_nodes.append(edge)
            if self.last_node_updated['node'] in list_nodes:
                list_nodes.remove(self.last_node_updated['node'])

        pos = nx.spring_layout(gr)
        nx.draw_networkx_edges(gr, pos=pos, with_labels=True, edgelist=list_edges, node_size=600)
        nx.draw_networkx_nodes(gr, pos=pos, with_labels=True, nodelist=list_nodes, node_size=600)

        if len(last) > 0:
            color = ''
            if self.last_node_action == "ADD":
                color = 'b'
            elif self.last_node_action == "DELETE":
                color = 'r'
            elif self.last_node_action == "UPDATE":
                color = 'g'

            if color != '':
                nx.draw_networkx_edges(gr, pos=pos, edgelist=[last], width=2.0, edge_color=color)

        if len(last_nodes) > 0:
            color = ''
            color_node = ''
            if self.last_node_action == "ADD":
                color = 'b'
                color_node = 'b'

            if color != '':
                nx.draw_networkx_nodes(gr, pos=pos, with_labels=True, nodelist=[self.last_node_updated['node']],
                                       node_color=color_node,
                                       node_size=600)
                nx.draw_networkx_edges(gr, pos=pos, edgelist=last_nodes, width=2.0, edge_color=color)
                list_nodes.append(self.last_node_updated['node'])

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in gr.edges(data=True)])
            nx.draw_networkx_edge_labels(gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        labels = dict()
        for i in list_nodes:
            labels[i] = str(i)
        nx.draw_networkx_labels(gr, pos, labels)

        plt.show()
