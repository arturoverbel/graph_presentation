import numpy as np


def Forest(source, graph, dist):
    dist = np.array(dist)

    x = graph.last_vertex_modified[0]
    y = graph.last_vertex_modified[1]
    w_xy = graph.last_vertex_modified[2]

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

        start = np.searchsorted(graph.source, u, side='left')
        end = np.searchsorted(graph.source, u, side='right')

        for index, v in enumerate(graph.target[start:end]):
            new_weight_uv = dist[u] + graph.weight[start + index]
            if new_weight_uv < dist[v]:
                dist[v] = new_weight_uv
                H[v] = new_weight_uv

    return dist

def Forest_apsp(graph, dist):

    for source in graph.vertex:
        dist[source] = Forest(source, graph, dist[source])

    return dist
