import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphPro():
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

    def draw(self, with_weight=True):
        gr = nx.DiGraph()
        gr.add_weighted_edges_from(self.export())
        pos = nx.spring_layout(gr)
        list_edges = list(gr.edges())
        last = ()

        if self.last_vertex_modified.size > 0:
            last = (int(self.last_vertex_modified[0]), int(self.last_vertex_modified[1]))
            list_edges.remove(last)
            if not self.directed:
                list_edges.remove((int(self.last_vertex_modified[1]), int(self.last_vertex_modified[0])))

        nx.draw(gr, pos=pos, with_labels=True, edgelist=list_edges, node_size=600)

        if with_weight:
            edge_labels = dict([((u, v,), d['weight']) for u, v, d in gr.edges(data=True)])
            nx.draw_networkx_edge_labels(gr, pos=pos, edgelist=list_edges, edge_labels=edge_labels)

        if len(last) > 0:
            nx.draw_networkx_edges(gr, pos=pos, edgelist=[last], width=2.0, edge_color='b')

        plt.axis('off')
        plt.show()
