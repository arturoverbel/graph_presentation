import numpy as np
from algorithms.rr import *


def Quinca(graph, dist):
    u, v, w_uv = graph.last_edge_updated

    S = {v: Find_Source_Affected(graph, dist)}

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

        y_targets, y_weights = graph.get_targets_from_source(y, return_weight=True)

        for index, w in enumerate(y_targets):
            w_yw = y_weights[index]
            if (w not in vis or not vis[w]) and dist[u, w] > w_uv + dist[v, w] and \
                    dist[v, w] == dist[v, y] + w_yw:
                Q.append(w)
                vis[w] = True
                P[w] = y

    return dist
