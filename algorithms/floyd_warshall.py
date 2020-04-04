import numpy as np


def Floyd_Warshall(graph):

    total_nodes = len(graph.nodes)
    dist = np.zeros((total_nodes, total_nodes))
    dist.fill(np.inf)

    for idx in range(graph.source.size):
        dist[graph.source[idx], graph.target[idx]] = graph.weight[idx]

    for k in graph.nodes:
        for i in graph.nodes:
            for j in graph.nodes:
                if k == i:
                    dist[k, i] = 0
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]

    return dist
