import numpy as np


def Forest(source, graph, dist):
    x, y, w_xy = graph.last_edge_updated

    # Phase 1
    new_weight_y = dist[x] + w_xy

    if dist[y] < new_weight_y:
        return dist

    # Phase 2
    dist[y] = new_weight_y
    H = {y: new_weight_y}

    # Phase 3
    while len(H) > 0:
        (u, weight) = min(H.items(), key=lambda xx: xx[1])
        H.pop(u)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for index, v in enumerate(u_targets):
            new_weight_uv = dist[u] + u_weights[index]
            if new_weight_uv < dist[v]:
                dist[v] = new_weight_uv
                H[v] = new_weight_uv

    return dist

def Forest_apsp(graph, dist):

    for source in graph.nodes:
        dist[source] = Forest(source, graph, dist[source])

    return dist
