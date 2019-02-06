import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphPro:
    source = []
    target = []
    weight = []
    vertex = []

    undirected = 0

    def __init__(self, source=[], target=[], weight=[], directed=True):
        self.source = np.array(source)
        self.target = np.array(target)
        self.weight = np.array(weight)
        self.directed = directed

        self.set_vertex()

    def set_vertex(self):
        vertex = np.unique(self.source)
        vertex2 = np.unique(self.target)
        self.vertex = np.unique(np.concatenate([vertex, vertex2]))
        return self.vertex

    def draw(self, with_weight=True):
        gr = nx.DiGraph()
        gr.add_weighted_edges_from(self.export())
        pos = nx.spring_layout(gr)
        list_edges = list(gr.edges())
        list_nodes = list(gr.nodes)
        last = ()
        last_nodes = []

        if self.last_vertex_modified.size > 0:
            last = (int(self.last_vertex_modified[0]), int(self.last_vertex_modified[1]))
            if last in list_edges:
                list_edges.remove(last)
                if not self.directed:
                    list_edges.remove((int(self.last_vertex_modified[1]), int(self.last_vertex_modified[0])))

        if self.last_node_modified is not None:
            if self.last_node_modified['node'] in list_nodes:
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
                list_nodes.remove(self.last_node_modified['node'])

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
            elif self.last_node_action == "DELETE":
                color = 'r'
                color_node = 'y'
            elif self.last_node_action == "UPDATE":
                color = 'g'
                color_node = 'g'

            if color != '':
                nx.draw_networkx_edges(gr, pos=pos, edgelist=last_nodes, width=2.0, edge_color=color)
                nx.draw_networkx_nodes(gr, pos=pos, with_labels=True, nodelist=[self.last_node_modified['node']],
                                       node_color=color_node,
                                       node_size=600)
                list_nodes.append(self.last_node_modified['node'])

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in gr.edges(data=True)])
            nx.draw_networkx_edge_labels(gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        labels = dict()
        for i in list_nodes:
            labels[i] = str(i)
        nx.draw_networkx_labels(gr, pos, labels)

        plt.show()
