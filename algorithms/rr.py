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
    counter_iteraciones = 0

    u, v, w_uv = graph.last_edge_updated
    if dist[source, v] <= dist[source, u] + w_uv:
        return dist

    vis = [False for i in graph.nodes]

    dist[source, v] = dist[source, v] + w_uv
    print(dist)

    Q = deque([v])
    vis[v] = True

    while len(Q) > 0:
        y = Q.popleft()
        print("->", y)
        dist[source, y] = dist[source, u] + w_uv + dist[v, y]
        counter_iteraciones += 1
        print(dist)

        for z in graph.get_targets_from_source(y):
            print(z)
            counter_iteraciones += 1
            if not vis[z] and dist[source, z] > dist[source, u] + w_uv + dist[v, z]:
                vis[z] = True
                Q.append(z)

    print("---------- i_3: ", counter_iteraciones)
    return dist


def Find_Affected_Sources(graph, dist):
    u, v, w_uv = graph.last_edge_updated
    sources_affected = deque([])
    counter_iteraciones = 0

    if dist[u, v] <= w_uv:
        return sources_affected

    vis = [False for i in graph.nodes]

    Q = deque([v])
    vis[v] = True

    while len(Q) > 0:
        x = Q.popleft()

        # TODO it can be better?
        for z in graph.source[graph.target == x]:
            counter_iteraciones += 1
            if not vis[z] and dist[z, v] > dist[z, u] + w_uv:
                vis[z] = True
                Q.append(z)
                sources_affected.append(z)


    print("---------- i_2: ", counter_iteraciones)
    print("Sources affected: ", sources_affected)
    return sources_affected

def Bfs_Truncated_With_Sources(graph, dist):
    print("================RR====================")
    counter_print = 0
    counter_iteraciones = 0
    print(counter_print, "----------")
    print(dist)

    for source in Find_Affected_Sources(graph, dist):
        counter_iteraciones += 1

        counter_print += 1
        print(counter_print, "---------- i_1: ", counter_iteraciones)

        dist = Bfs_Truncated(graph, source, dist)


    print("=======RR======= i_1= ", counter_iteraciones)

    return dist
