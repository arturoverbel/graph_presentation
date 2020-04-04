import numpy as np


def Dijkstra_Truncated(graph, dist_source):
    u, v, w_uv = graph.last_edge_updated

    dist_source = np.array(dist_source)
    if dist_source[v] <= dist_source[u] + w_uv:
        return

    dist_source[v] = dist_source[u] + w_uv
    PQ = {v: dist_source[v]}

    while len(PQ) > 0:
        (y, weight) = min(PQ.items(), key=lambda x: x[1])
        PQ.pop(y)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for index, w in enumerate(u_targets):
            if dist_source[w] <= weight + u_weights[index]:
                continue

            new_weight = weight + graph.weight[start + index]
            dist_source[w] = new_weight
            PQ[w] = new_weight

    return dist_source


def Bfs_Truncated(graph, source, dist):
    u, v, w_uv = graph.last_edge_updated
    vis = { i : False for i in graph.nodes }

    if dist[source, v] <= dist[source, u] + w_uv:
        return dist

    dist[source, v] = dist[source, v] + w_uv

    Q = [v]
    vis[v] = True

    while len(Q) > 0:
        y = Q.pop(0)
        dist[source, y] = dist[source, u] + w_uv + dist[v, y]

        for w in graph.get_targets_from_source(y):
            if not vis[w] and dist[source, w] > dist[source, u] + w_uv + dist[v, w]:
                vis[w] = True
                Q.append(w)

    return dist


def Find_Source_Affected(graph, dist):
    u, v, w_uv = graph.last_edge_updated
    vis = { i : False for i in graph.nodes }

    source_affected = []

    if dist[u, v] <= w_uv:
        return source_affected

    dist[u, v] = dist[u, v] + w_uv

    PQ = [v]
    vis[v] = True

    while len(PQ) > 0:
        x = PQ.pop(-1)

        for z in graph.source[graph.target == x]:
            if not vis[z] and dist[z, v] > dist[z, u] + w_uv:
                vis[z] = True
                PQ.append(z)
                source_affected.append(z)

    return source_affected

def Bfs_Truncated_With_Sources(graph, dist):

    for source in Find_Source_Affected(graph, dist):
        dist = Bfs_Truncated(graph, source, dist)

    return dist
