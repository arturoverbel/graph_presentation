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
                index_k = graph.vertex == k
                index_i = graph.vertex == i
                index_j = graph.vertex == j

                if dist[index_i, index_j] > dist[index_i, index_k] + dist[index_k, index_j]:
                    dist[index_i, index_j] = dist[index_i, index_k] + dist[index_k, index_j]

    return dist
