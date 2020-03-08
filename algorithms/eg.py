import numpy as np


def Even_Gazit(graph, dist):
    dist = np.array(dist)
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    if dist[u, v] <= w_uv:
        return dist

    dist[u, v] = w_uv

    for x in graph.vertex:
        for y in graph.vertex:
            sum = dist[x, u] + w_uv + dist[v, y]
            if sum < dist[x, y]:
                dist[x, y] = sum

    return dist
