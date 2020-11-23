import numpy as np
from collections import defaultdict
from collections import deque


def Dijkstra_Truncated(graph, dist_source):
    u, v, w_uv = graph.last_edge_updated

    if dist_source[v] <= dist_source[u] + w_uv:
        return

    dist_source[v] = dist_source[u] + w_uv

    PQ = defaultdict(int)
    S[v] = Find_Affected_Sources(graph, dist_source[v])

    while len(PQ) > 0:
        (y, weight) = min(PQ.items(), key=lambda x: x[1])
        PQ.pop(y)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for z, weigth_uv in zip(u_targets, u_weights):
            if dist_source[z] <= weight + weigth_uv:
                continue

            new_weight = weight + weigth_uv
            dist_source[z] = new_weight
            PQ[z] = new_weight

    return dist_source


def Bfs_Truncated(graph, source, dist):
    u, v, w_uv = graph.last_edge_updated
    if dist[source, v] <= dist[source, u] + w_uv:
        return dist

    vis = [False for i in graph.nodes]

    dist[source, v] = dist[source, v] + w_uv

    Q = deque([v])
    vis[v] = True

    while len(Q) > 0:
        y = Q.popleft()
        dist[source, y] = dist[source, u] + w_uv + dist[v, y]

        for z in graph.get_targets_from_source(y):
            if not vis[z] and dist[source, z] > dist[source, u] + w_uv + dist[v, z]:
                vis[z] = True
                Q.append(z)

    return dist


def Find_Affected_Sources(graph, dist):
    u, v, w_uv = graph.last_edge_updated
    sources_affected = deque([])

    if dist[u, v] <= w_uv:
        return sources_affected

    vis = [False for i in graph.nodes]

    Q = deque([v])
    vis[v] = True

    while len(Q) > 0:
        x = Q.popleft()

        # TODO it can be better?
        for z in graph.source[graph.target == x]:
            if not vis[z] and dist[z, v] > dist[z, u] + w_uv:
                vis[z] = True
                Q.append(z)
                sources_affected.append(z)

    return sources_affected


def Bfs_Truncated_With_Sources(graph, dist):
    for source in Find_Affected_Sources(graph, dist):
        dist = Bfs_Truncated(graph, source, dist)

    return dist
