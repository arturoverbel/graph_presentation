import numpy as np
from collections import deque

def Owner(graph, dist):
    u, v, c_uv = graph.last_edge_updated

    if c_uv >= dist[u, v]:
        return dist

    A = deque()
    D = deque()

    for l in graph.nodes:
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
