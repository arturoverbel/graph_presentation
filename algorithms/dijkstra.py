import numpy as np
import heapq


def DijkstraQQ(source, graph):
    dist = np.zeros(len(graph.nodes))
    dist.fill(np.inf)
    dist[source] = 0

    Q = []
    for s in graph.nodes:
        if source == s:
            continue
        heapq.heappush(Q, (np.inf, s))

    while len(Q) > 0:
        weight, u = heapq.heappop(Q)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for v, w_uv in zip(u_targets, u_weights):
            aux = dist[u] + w_uv
            if aux < dist[v]:
                dist[v] = aux

    return dist


def Dijkstra(source, graph):

    Q = list(graph.nodes)

    dist = np.zeros(len(graph.nodes))
    dist.fill(np.inf)
    dist[source] = 0

    while len(Q) > 0:
        min_num, u, index = np.inf, 0, 0
        for i, q in enumerate(Q):
            if dist[q] < min_num:
                min_num, u, index = dist[q], q, i

        Q.pop(index)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for v, w_uv in zip(u_targets, u_weights):
            aux = dist[u] + w_uv
            if aux < dist[v]:
                dist[v] = aux

    return dist


def Dijkstra_apsp(graph):
    result = np.full((graph.nodes.size, graph.nodes.size), np.inf)
    for i, v in enumerate(graph.nodes):
        result[i] = Dijkstra(v, graph)

    return result
