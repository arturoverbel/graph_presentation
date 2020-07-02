import numpy as np


def Floyd_Warshall_PREV(graph):

    dist = np.full((graph.nodes.size, graph.nodes.size), np.inf)
    prev = np.full((graph.nodes.size, graph.nodes.size), -1)

    for idx in range(graph.source.size):
        dist[graph.source[idx], graph.target[idx]] = graph.weight[idx]
        prev[graph.source[idx], graph.target[idx]] = graph.source[idx]

    for k in graph.nodes:
        for i in graph.nodes:
            if k == i:
                dist[i, k] = 0
                prev[i, k] = -1
            for j in graph.nodes:
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    prev[i, j] = prev[k, j]

    return dist, prev
