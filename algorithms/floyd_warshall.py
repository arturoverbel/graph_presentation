import numpy as np


def Floyd_Warshall(graph):

    total_vertex = len(graph.vertex)
    dist = np.zeros((total_vertex, total_vertex))
    dist.fill(np.inf)

    for idx in range(graph.source.size):
        dist[graph.source[idx], graph.target[idx]] = graph.weight[idx]

    for k in graph.vertex:
        for i in graph.vertex:
            for j in graph.vertex:
                if k == i:
                    dist[k, i] = 0
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]

    return dist
