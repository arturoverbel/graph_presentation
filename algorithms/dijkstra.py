import numpy as np


def Dijkstra(source, graph):

    Q = list(graph.vertex)

    dist = np.zeros(len(graph.vertex))
    dist.fill(np.inf)
    dist[source] = 0

    while len(Q) > 0:
        min, u, index = np.inf, 0, 0
        for i, q in enumerate(Q):
            if dist[q] < min:
                min, u, index = dist[q], q, i

        Q.pop(index)

        # Find neighbors indexes of u, assuming sources array is sorted #
        start = np.searchsorted(graph.source, u, side='left')
        end = np.searchsorted(graph.source, u, side='right')

        for v in graph.target[start:end]:
            aux = dist[u] + graph.get_weight(u, v)  ## What is get_weight()? Ain't weights stored in weights array?
            if aux < dist[v]:
                dist[v] = aux

    return dist


def Dijkstra_apsp(graph):

    result = np.full((graph.vertex.size, graph.vertex.size), np.inf)
    for i, v in enumerate(graph.vertex):
        result[i] = Dijkstra(v, graph)

    return result
