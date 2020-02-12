from graph.Graph import Graph


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
