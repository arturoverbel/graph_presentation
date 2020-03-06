import numpy as np

def Floyd_Warshall(graph):

    total_vertex = len(graph.vertex)
    dist = np.zeros((total_vertex, total_vertex))
    dist.fill(np.inf)

    for idx in range(graph.source.size):
        index_s = graph.vertex == graph.source[idx]
        index_t = graph.vertex == graph.target[idx]
        dist[index_s, index_t] = graph.weight[idx]
    for index in range(graph.vertex.size):
        dist[index, index] = 0

    for k in np.nditer(graph.vertex):
        for i in np.nditer(graph.vertex):
            for j in np.nditer(graph.vertex):
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]

    return dist
