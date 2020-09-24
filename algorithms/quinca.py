import numpy as np
from algorithms.rr import *
from collections import defaultdict
from collections import deque

def Quinca(graph, dist):
    print("================QUINCA====================")
    counter_iteraciones = 0
    counter_print = 0
    u, v, w_uv = graph.last_edge_updated

    if dist[u, v] <= w_uv:
        return dist

    S = defaultdict(list)
    S[v] = Find_Affected_Sources(graph, dist)

    dist[u, v] = w_uv

    Q = deque([v])
    P = {v: v}
    vis = [False for i in graph.nodes]
    vis[v] = True

    while len(Q) > 0:
        y = Q.popleft()
        # update distances for source nodes
        for x in S[P[y]]:
            counter_iteraciones += 1
            if dist[x, y] > dist[x, u] + w_uv + dist[v, y]:
                dist[x, y] = dist[x, u] + w_uv + dist[v, y]
                counter_print += 1
                print(counter_print, "----------", counter_iteraciones)
                print(dist)
                if y != v:
                    S[y].append(x)


        y_targets, y_weights = graph.get_targets_from_source(y, return_weight=True)

        for z, w_yz in zip(y_targets, y_weights):
            counter_iteraciones += 1
            if not vis[z] and dist[u, z] > w_uv + dist[v, z] and \
                    dist[v, z] == dist[v, y] + w_yz:
                Q.append(z)
                vis[z] = True
                P[z] = y

    print("=======QUINCA======= i= ", counter_iteraciones)
    return dist
