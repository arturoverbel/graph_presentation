import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphPro:
    source = []
    target = []
    weight = []
    vertex = []

    undirected = 0

    def __init__(
        self,
        source=[],
        target=[],
        weight=[],
        directed=True,
        set_vertex_with_num_nodes=0
    ):
        self.directed = directed
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)

        if self.directed is False:
            self.source = np.concatenate([self.source, self.target])
            self.target = np.concatenate([self.target, np.array(source)])
            self.weight = np.concatenate([self.weight, self.weight])

        idx = self.source.argsort()
        self.source = self.source[idx]
        self.target = self.target[idx]
        self.weight = self.weight[idx]

        if set_vertex_with_num_nodes == 0:
            self.set_vertex()
        else:
            self.set_vertex_with_num_nodes(set_vertex_with_num_nodes)


    def set_vertex(self):
        max_vertex = max(np.concatenate([np.unique(self.source), np.unique(self.target)]))
        self.vertex = np.arange(max_vertex+1)
        return self.vertex

    def set_vertex_with_num_nodes(self, num_nodes):
        self.vertex = np.arange(num_nodes)
        return self.vertex

    def draw(self, with_weight=True):
        gr = nx.DiGraph()
        gr.add_weighted_edges_from(self.export())

        list_edges = list(gr.edges())
        list_nodes = list(gr.nodes())
        last = ()
        last_nodes = []

        if self.last_vertex_modified.size > 0:
            last = (int(self.last_vertex_modified[0]), int(self.last_vertex_modified[1]))
            if last in list_edges:
                list_edges.remove(last)
                if not self.directed:
                    list_edges.remove((self.last_vertex_modified[1], self.last_vertex_modified[0]))

        if self.last_node_modified is not None:
            for source in self.last_node_modified['source']:
                edge = (int(source), int(self.last_node_modified['node']))
                if edge in list_edges:
                    list_edges.remove(edge)
                last_nodes.append(edge)
            for target in self.last_node_modified['target']:
                edge = (int(self.last_node_modified['node']), int(target))
                if edge in list_edges:
                    list_edges.remove(edge)
                last_nodes.append(edge)
            if self.last_node_modified['node'] in list_nodes:
                list_nodes.remove(self.last_node_modified['node'])

        pos = nx.spring_layout(gr)
        nx.draw_networkx_edges(gr, pos=pos, with_labels=True, edgelist=list_edges, node_size=600)
        nx.draw_networkx_nodes(gr, pos=pos, with_labels=True, nodelist=list_nodes, node_size=600)

        if len(last) > 0:
            color = ''
            if self.last_vertex_action == "ADD":
                color = 'b'
            elif self.last_vertex_action == "DELETE":
                color = 'r'
            elif self.last_vertex_action == "UPDATE":
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
                nx.draw_networkx_nodes(gr, pos=pos, with_labels=True, nodelist=[self.last_node_modified['node']],
                                       node_color=color_node,
                                       node_size=600)
                nx.draw_networkx_edges(gr, pos=pos, edgelist=last_nodes, width=2.0, edge_color=color)
                list_nodes.append(self.last_node_modified['node'])

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in gr.edges(data=True)])
            nx.draw_networkx_edge_labels(gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        labels = dict()
        for i in list_nodes:
            labels[i] = str(i)
        nx.draw_networkx_labels(gr, pos, labels)

        plt.show()
