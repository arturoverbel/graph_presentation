import numpy as np

def Dijkstra_Truncated(graph, dist_source):
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    dist_source = np.array(dist_source)
    if dist_source[v] <= dist_source[u] + w_uv:
        return

    dist_source[v] = dist_source[u] + w_uv
    PQ = {v: dist_source[v]}

    while len(PQ) > 0:
        (y, weight) = min(PQ.items(), key=lambda x: x[1])
        PQ.pop(y)
        for w in graph.target[graph.source == y]:
            if dist_source[w] <= weight + graph.get_weight(y, w):
                continue

            new_weight = weight + graph.get_weight(y, w)
            dist_source[w] = new_weight
            PQ[w] = new_weight

    return dist_source

def Bfs_Truncated(graph, source, dist):
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    dist = np.array(dist)
    if dist[source, v] <= dist[source, u] + w_uv:
        return dist

    dist[source, v] = dist[source, v] + w_uv

    PQ = [v]
    vis = {v: True}

    while len(PQ) > 0:
        y = PQ.pop(-1)

        dist[source, y] = dist[source, u] + w_uv + dist[v, y]
        for w in graph.target[graph.source == y]:
            if (w not in vis or not vis[w]) and dist[source, w] > dist[source, u] + w_uv + dist[v, w]:
                vis[w] = True
                PQ.append([w])

    return dist

def Find_Source_Affected(graph, dist):
    dist = np.array(dist)
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    source_affected = []
    dist = np.array(dist)
    if dist[u, v] <= w_uv + [0]:
        return source_affected

    dist[u, v] = dist[u, v] + w_uv

    PQ = [v]
    vis = {v: True}

    while len(PQ) > 0:
        x = PQ.pop(-1)
        for z in graph.source[graph.target == x]:
            if (z not in vis or not vis[z]) and dist[z, v] > dist[z, u] + w_uv:
                vis[z] = True
                PQ.append([z])
                source_affected.append([z])

    return source_affected

def Bfs_Truncated_With_Sources(graph, dist):
    dist = np.array(dist)
    for source in Find_Source_Affected(graph, dist.tolist()):
        dist = Bfs_Truncated(graph, source, dist)

    return dist
