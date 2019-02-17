import numpy as np

def Dijkstra(source, graph):

    total_vertex = len(graph.vertex)
    Q = np.array(graph.vertex)

    dist = np.zeros(total_vertex)
    dist.fill(np.inf)

    dist[graph.vertex == source] = 0

    while len(Q) != 0:

        min = np.inf
        u = 0
        for q in Q:
            if dist[graph.vertex == q] <= min:
                min = dist[graph.vertex == q]
                u = q

        Q = np.delete(Q, np.argwhere(Q == u))

        for v in graph.target[graph.source == u]:
            alt = dist[graph.vertex == u] + graph.get_weight(u, v)
            index_v = graph.vertex == v
            if alt < dist[index_v]:
                dist[index_v] = alt

    return dist

def Dijkstra_apsp(graph):

    result = np.full((graph.vertex.size, graph.vertex.size), np.inf)
    count = 0
    for v in graph.vertex:
        result[count] = Dijkstra(v, graph)
        count = count + 1

    return result
