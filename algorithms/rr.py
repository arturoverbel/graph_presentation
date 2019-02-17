import numpy as np

def Dijkstra_Truncated(graph, dist_source):
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    dist_source = np.array(dist_source)
    if dist_source[graph.vertex == v] <= dist_source[graph.vertex == u] + w_uv:
        return

    dist_source[graph.vertex == v] = dist_source[graph.vertex == u] + w_uv
    PQ = {v: dist_source[v]}

    while len(PQ) > 0:
        (y, weight) = min(PQ.items(), key=lambda x: x[1])
        PQ.pop(y)
        for w in graph.target[graph.source == y]:
            if dist_source[graph.vertex == w] <= weight + graph.get_weight(y, w):
                continue

            new_weight = weight + graph.get_weight(y, w)
            dist_source[graph.vertex == w] = new_weight
            PQ[w] = new_weight

    return dist_source

def Bfs_Truncated(graph, source, dist):
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    dist = np.array(dist)
    if dist[graph.vertex == source, graph.vertex == v] <= dist[graph.vertex == source, graph.vertex == u] + w_uv:
        return dist

    dist[graph.vertex == source, graph.vertex == v] = dist[graph.vertex == source, graph.vertex == v] + w_uv

    PQ = np.array([v])
    vis = {v: True}

    while len(PQ) > 0:
        y, PQ = PQ[-1], PQ[:-1]
        dist[graph.vertex == source, graph.vertex == y] = \
            dist[graph.vertex == source, graph.vertex == u] + w_uv + dist[graph.vertex == v, graph.vertex == y]
        for w in graph.target[graph.source == y]:
            if (w not in vis or not vis[w]) \
                    and dist[graph.vertex == source, graph.vertex == w] > \
                    dist[graph.vertex == source, graph.vertex == u] + w_uv + dist[graph.vertex == v, graph.vertex == w]:
                vis[w] = True
                PQ = np.append(PQ, [w])

    return dist

def Find_Source_Affected(graph, dist):
    dist = np.array(dist)
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    source_affected = np.array([])
    dist = np.array(dist)
    if dist[graph.vertex == u, graph.vertex == v] <= w_uv + [0]:
        return source_affected

    dist[graph.vertex == u, graph.vertex == v] = dist[graph.vertex == u, graph.vertex == v] + w_uv

    PQ = np.array([v])
    vis = {v: True}

    while len(PQ) > 0:
        x, PQ = PQ[-1], PQ[:-1]
        for z in graph.source[graph.target == x]:
            if (z not in vis or not vis[z]) \
                    and dist[graph.vertex == z, graph.vertex == v] > \
                    dist[graph.vertex == z, graph.vertex == u] + w_uv:
                vis[z] = True
                PQ = np.append(PQ, [z])
                source_affected = np.append(source_affected, [z])

    return source_affected

def Bfs_Truncated_With_Sources(graph, dist):
    dist = np.array(dist)
    for source in Find_Source_Affected(graph, dist.tolist()):
        dist = Bfs_Truncated(graph, source, dist)

    return dist
