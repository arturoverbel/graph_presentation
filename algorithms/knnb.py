import numpy as np


def KNNB_Node_Incremental(graph, dist):

    dist = np.array(dist)

    add = np.full(graph.vertex.size - 1, np.inf)
    dist = np.vstack([dist, add])
    dist = np.hstack([dist, np.append(add, np.inf)[:, None]])
    dist[graph.vertex.size - 1, graph.vertex.size - 1] = 0

    z = graph.last_node_modified['node']
    T1 = graph.last_node_modified['source']
    T2 = graph.last_node_modified['target']

    min_in_z = {}
    min_out_z = {}

    for k_in in T1:
        dist[graph.vertex == k_in, graph.vertex == z] = graph.get_weight(k_in, z)

    for k_out in T2:
        dist[graph.vertex == z, graph.vertex == k_out] = graph.get_weight(z, k_out)

    for v in graph.vertex:
        if v == z:
            continue
        for k_in in T1:
            # if v == k_in:
            #    continue
            L_vz = dist[graph.vertex == v, graph.vertex == k_in][0] + graph.get_weight(k_in, z)
            if v not in min_in_z or L_vz < min_in_z[v]:
                min_in_z[v] = L_vz
        for k_out in T2:
            # if v == k_out:
            #    continue

            L_zv = dist[graph.vertex == k_out, graph.vertex == v][0] + graph.get_weight(z, k_out)
            if v not in min_out_z or L_zv < min_out_z[v]:
                min_out_z[v] = L_zv
    for i, L_iz in min_in_z.items():
        for j, L_jz in min_out_z.items():
            if i == j:
                continue
            if L_iz + L_jz < dist[graph.vertex == i, graph.vertex == j][0]:
                dist[graph.vertex == i, graph.vertex == j] = L_iz + L_jz

    for i, value in min_in_z.items():
        dist[graph.vertex == i, graph.vertex == z] = value
    for j, value in min_out_z.items():
        dist[graph.vertex == z, graph.vertex == j] = value

    return dist
