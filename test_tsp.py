from graph.Graph import Graph
import numpy as np
import os

os.system('clear')
print("<--------Test Create------->\n")

def insert_multiple(x, lst):
    return [lst[:i] + [x] + lst[i:] for i in range(len(lst) + 1)]


def barter(c):
    if len(c) == 0:
        return [[]]
    return sum([insert_multiple(c[0], s) for s in barter(c[1:])], [])


def search_min(all_routes):
    routes_valid = []
    min_route = []
    min_weight = np.Inf

    for i in range(len(all_routes)):
        route = all_routes[i]
        is_route_valid = True
        total_weight = 0

        for j in range(len(route)):
            if j == 0:
                continue
            w = graph.get_weight(route[j-1], route[j])
            if w == 0 or w == np.Inf:
                is_route_valid = False
                break
            else:
                total_weight = total_weight + w

        if is_route_valid is False:
            continue

        w = graph.get_weight(route[-1], route[0])
        if (w == 0 or w == np.Inf) is False:
            total_weight = total_weight + w

        all_routes[i].append(route[0])
        routes_valid.append(all_routes[i])

        if total_weight < min_weight:
            min_weight = total_weight
            min_route = all_routes[i]

    return {
        "routes_valid": routes_valid,
        "min_route": min_route,
        "min_weight": min_weight
    }


graph = Graph.creategraph(5, 1.0, directed=False)
cities = graph.vertex
cities_bartered = barter(cities)
result = search_min(cities_bartered)

print("Total: ", len(result["routes_valid"]))
print("Route min: ", result["min_route"])
print("Weight min: ", result["min_weight"])

graph.draw()
