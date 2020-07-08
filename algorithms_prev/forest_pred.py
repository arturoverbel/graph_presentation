import numpy as np
import heapq

def Forest_PRED(source, graph, t_dist, t_pred):
    x, y, w_xy = graph.last_edge_updated

    # Phase 1
    if t_dist[y] < t_dist[x] + w_xy:
        return t_dist, t_pred

    # Phase 2
    t_pred[y] = x
    t_dist[y] = t_dist[x] + w_xy

    H = []
    heapq.heappush(H, (t_dist[y], y)) # H is a min-heap

    # Phase 3
    while len(H) > 0:
        (weight, u) = heapq.heappop(H)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for index, v in enumerate(u_targets):
            if t_dist[u] + u_weights[index] < t_dist[v]:
                t_pred[v] = u
                t_dist[v] = t_dist[u] + u_weights[index]
                heapq.heappush(H, (t_dist[v], v))

    return t_dist, t_pred

def Forest_apsp_PRED(graph, dist, pred):

    for source in graph.nodes:
        d, p = Forest_PRED(source, graph, dist[source], pred[source])
        dist[source] = d
        pred[source] = p

    return dist, pred
