import numpy as np
from algorithms.rr import *


def Quinca(graph, dist):
    dist = np.array(dist)

    u = graph.last_vertex_modified[0]
    v = graph.last_vertex_modified[1]
    w_uv = graph.last_vertex_modified[2]

    S = {v: Find_Source_Affected(graph, dist.tolist())}

    dist[u, v] = w_uv

    Q = [v]
    P = {v: v}
    vis = {v: True}

    while len(Q) > 0:
        y = Q.pop(-1)
        # update distances for source nodes
        for x in S[P[y]]:
            if dist[x, y] > dist[x, u] + w_uv + dist[v, y]:
                dist[x, y] = dist[x, u] + w_uv + dist[v, y]
                if y != v:
                    if y not in S:
                        S[y] = []
                    S[y].append(x)

        #enqueue all neighbors that get closer to u
        start = np.searchsorted(graph.source, y, side='left')
        end = np.searchsorted(graph.source, y, side='right')

        for index, w in enumerate(graph.target[start:end]):
            if (w not in vis or not vis[w]) and dist[u, w] > w_uv + dist[v, w] and \
                    dist[v, w] == dist[v, y] + graph.weight[index]:
                Q.append(w)
                vis[w] = True
                P[w] = y

    return dist
