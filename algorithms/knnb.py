import numpy as np


def KNNB_Node_Incremental(graph, dist):
    add = np.full(graph.nodes.size - 1, np.inf)
    dist = np.vstack([dist, add])
    dist = np.hstack([dist, np.append(add, np.inf)[:, None]])
    dist[graph.nodes.size - 1, graph.nodes.size - 1] = 0

    z = graph.last_node_updated['node']
    T1 = graph.last_node_updated['source']
    T2 = graph.last_node_updated['target']

    min_in_z = {}
    min_out_z = {}

    for k_in in T1:
        dist[graph.nodes == k_in, graph.nodes == z] = graph.get_weight(k_in, z)

    for k_out in T2:
        dist[graph.nodes == z, graph.nodes == k_out] = graph.get_weight(z, k_out)

    for v in graph.nodes:
        if v == z:
            continue
        for k_in in T1:
            # if v == k_in:
            #    continue
            L_vz = dist[graph.nodes == v, graph.nodes == k_in][0] + graph.get_weight(k_in, z)
            if v not in min_in_z or L_vz < min_in_z[v]:
                min_in_z[v] = L_vz
        for k_out in T2:
            # if v == k_out:
            #    continue

            L_zv = dist[graph.nodes == k_out, graph.nodes == v][0] + graph.get_weight(z, k_out)
            if v not in min_out_z or L_zv < min_out_z[v]:
                min_out_z[v] = L_zv
    for i, L_iz in min_in_z.items():
        for j, L_jz in min_out_z.items():
            if i == j:
                continue
            if L_iz + L_jz < dist[graph.nodes == i, graph.nodes == j][0]:
                dist[graph.nodes == i, graph.nodes == j] = L_iz + L_jz

    for i, value in min_in_z.items():
        dist[graph.nodes == i, graph.nodes == z] = value
    for j, value in min_out_z.items():
        dist[graph.nodes == z, graph.nodes == j] = value

    return dist
