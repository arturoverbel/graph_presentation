import numpy as np
from collections import defaultdict


def Dijkstra_PREV(source, graph):

    Q = list(graph.nodes)

    prev = np.full((graph.nodes.size), -1)
    dist = np.full((graph.nodes.size), np.inf)

    dist[source] = 0

    while len(Q) > 0:
        min, u, index = np.inf, 0, 0
        for i, q in enumerate(Q):
            if dist[q] < min:
                min, u, index = dist[q], q, i

        Q.pop(index)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for v, w_uv in zip(u_targets, u_weights):
            aux = dist[u] + w_uv
            if aux < dist[v]:
                dist[v] = aux
                prev[v] = u

    return dist, prev

def Dijkstra_apsp_PREV(graph):

    result = np.full((graph.nodes.size, graph.nodes.size), np.inf)
    result_prev = np.full((graph.nodes.size, graph.nodes.size), -1)

    total = len(graph.nodes)
    for i, v in enumerate(graph.nodes):
        result[i], result_prev[i] = Dijkstra_PREV(v, graph)

    return result, result_prev
