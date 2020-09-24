import numpy as np
import heapq

def Forest(source, graph, t_dist):
    counter_iteraciones = 0
    counter_print = 0
    x, y, w_xy = graph.last_edge_updated

    # Phase 1
    if t_dist[y] < t_dist[x] + w_xy:
        return t_dist

    # Phase 2
    counter_iteraciones += 1
    t_dist[y] = t_dist[x] + w_xy
    
    print(counter_print, "----------", counter_iteraciones)
    print("node: ", source, " => ", t_dist)

    H = []
    heapq.heappush(H, (t_dist[y], y)) # H is a min-heap

    # Phase 3
    while len(H) > 0:
        (weight, u) = heapq.heappop(H)

        u_targets, u_weights = graph.get_targets_from_source(u, return_weight=True)

        for index, v in enumerate(u_targets):
            counter_iteraciones += 1
            if t_dist[u] + u_weights[index] < t_dist[v]:
                t_dist[v] = t_dist[u] + u_weights[index]
                counter_print += 1
                print(counter_print, "----------", counter_iteraciones)
                print("node: ", source, " => ", t_dist)
                heapq.heappush(H, (t_dist[v], v))

    return t_dist

def Forest_apsp(graph, dist):
    print("================Forest====================")
    counter_iteraciones = 0
    for source in graph.nodes:
        counter_iteraciones += 1
        dist[source] = Forest(source, graph, dist[source])
        print(dist)
        print("*********", counter_iteraciones)

    print("=======Forest======= i= ", counter_iteraciones)
    return dist
