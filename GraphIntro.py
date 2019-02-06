
from graph.Graph import Graph

sources = [1, 2, 3, 0, 5, 1, 2, 1, 3]
targets = [0, 0, 0, 5, 0, 2, 1, 3, 1]
weights = [2, 2, 4, 1, 1, 3, 3, 2, 2]

graph = Graph(sources, targets, weights)

print('------')
graph.print_r()
graph.dynamic_decreasing_node(5)

graph.draw()

exit()

print("<--------Test Create------->\n")

graph = Graph.creategraph(6, .75)
graph.print_r()

print("-------Incremental-----")
data = graph.dynamic_incremental_random_edge()
graph.print_r()

print("-------Decreasing-----")
data = graph.dynamic_decreasing_random_edge()
graph.print_r()

print("-------Update Vertex-----")
data = graph.vertex_update_random()
print(data)
graph.print_r()

graph.draw()
print()
print("------------------------")
