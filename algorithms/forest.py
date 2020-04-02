import numpy as np


def Forest(source, graph, dist):
    dist = np.array(dist)

    x = graph.last_vertex_modified[0]
    y = graph.last_vertex_modified[1]
    w_xy = graph.last_vertex_modified[2]

    if c_uv >= dist[u, v]:
        return dist

    A = []
    D = []

    for l in graph.vertex:
        if (c_uv + dist[v, l]) < dist[u, l]:
            D.append(l)
        if (dist[l, u] + c_uv) < dist[l, v]:
            A.append(l)

    for j in D:
        for i in A:
            sum = dist[i, u] + c_uv + dist[v, j]
            if sum < dist[i, j]:
                dist[i, j] = sum

    return dist
