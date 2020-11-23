
def Even_Gazit(graph, dist):
    u, v, w_uv = graph.last_edge_updated

    if dist[u, v] <= w_uv:
        return dist

    dist[u, v] = w_uv

    for x in graph.nodes:
        for y in graph.nodes:
            sum = dist[x, u] + w_uv + dist[v, y]
            if sum < dist[x, y]:
                dist[x, y] = sum

    return dist
