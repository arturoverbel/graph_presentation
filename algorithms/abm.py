import numpy as np
from collections import deque

# Affected Block Matriz = ABM Updated
def ABM_Updated(graph, dist):
    u, v, c_uv = graph.last_edge_updated

    if c_uv >= dist[u, v]:
        return dist

    affected_sources = deque()
    affected_targets = deque()

    for k in graph.nodes:
        if (c_uv + dist[v, k]) < dist[u, k]:
            affected_targets.append(k)
        if (dist[k, u] + c_uv) < dist[k, v]:
            affected_sources.append(k)

    for j in affected_targets:
        for i in affected_sources:
            sum = dist[i, u] + c_uv + dist[v, j]
            if sum < dist[i, j]:
                dist[i, j] = sum

    return dist
