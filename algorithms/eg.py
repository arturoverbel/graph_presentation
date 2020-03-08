import numpy as np


def Even_Gazit(graph, dist):
    dist = np.array(dist)
    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]


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
