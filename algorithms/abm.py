import numpy as np
from collections import deque

# Affected Block Matriz = ABM Updated
def ABM_Updated(graph, dist):
    u, v, c_uv = graph.last_edge_updated

    if c_uv >= dist[u, v]:
        return dist

    AA = deque()
    DD = deque()

    for k in graph.nodes:
        if (c_uv + dist[v, k]) < dist[u, k]:
            DD.append(k)
        if (dist[k, u] + c_uv) < dist[k, v]:
            AA.append(k)

    for j in DD:
        for i in AA:
            sum = dist[i, u] + c_uv + dist[v, j]
            if sum < dist[i, j]:
                dist[i, j] = sum

    return dist
