import numpy as np


def Even_Gazit(graph, dist):
    print("================EG====================")

    counter_print = 0
    counter_iteraciones = 0

    u, v, w_uv = graph.last_edge_updated

    if dist[u, v] <= w_uv:
        return dist

    dist[u, v] = w_uv
    print(counter_print, "----------")
    print(dist)

    for x in graph.nodes:
        for y in graph.nodes:
            counter_iteraciones += 1
            sum = dist[x, u] + w_uv + dist[v, y]
            if sum < dist[x, y]:
                dist[x, y] = sum
                counter_print += 1
                print(counter_print, "----------", counter_iteraciones)
                print(dist)

    print("=======EG======= i= ", counter_iteraciones)
    return dist
