import numpy as np


def Floyd_Warshall(graph):

    dist = np.full((graph.nodes.size, graph.nodes.size), np.inf)

    for idx in range(graph.source.size):
        dist[graph.source[idx], graph.target[idx]] = graph.get_weight_idx(idx)

    for k in graph.nodes:
        for i in graph.nodes:
            if k == i:
                dist[k, i] = 0
            for j in graph.nodes:
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]

    return dist
