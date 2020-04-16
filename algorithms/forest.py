import numpy as np
from collections import defaultdict

def Forest(source, graph, t_dist):
    x, y, w_xy = graph.last_edge_updated

    # Phase 1
    if t_dist[y] < t_dist[x] + w_xy:
        return t_dist

    # Phase 2
    t_dist[y] = t_dist[x] + w_xy

    H = defaultdict(int)
    H[y] = t_dist[y]

    # Phase 3
    while len(H) > 0:
        (u, weight) = min(H.items(), key=lambda xx: xx[1])
        H.pop(u)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for index, v in enumerate(u_targets):
            if t_dist[u] + u_weights[index] < t_dist[v]:
                t_dist[v] = t_dist[u] + u_weights[index]
                H[v] = t_dist[v]

    return t_dist

def Forest_apsp(graph, dist):

    for source in graph.nodes:
        dist[source] = Forest(source, graph, dist[source])

    return dist
