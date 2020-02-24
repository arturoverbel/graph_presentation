from graph.Graph import Graph


print("<--------Test Create------->\n")

graph = Graph.creategraph(6, .75)
graph.print_r()

print("-------Incremental-----")
data = graph.dynamic_incremental_random_edge()
graph.print_r()
print(data)

print(graph.export_values())

print("-------Decreasing-----")
data = graph.dynamic_decreasing_random_edge()
graph.print_r()
print(data)

print("-------Update Edge-----")
data = graph.edge_update_random()
graph.print_r()
print(data)

#graph.draw()
print()
print("------------------------")
