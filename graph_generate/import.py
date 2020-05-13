import os
import sys
import json
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from graph.Graph import Graph

filename = "graph.json"

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Faltan argumentos")
    exit()

print("Filename: ", filename)
data_import = {}
with open(filename) as json_file:
    data_import = json.load(json_file)

graph = Graph.import_values(data_import)

graph.insert_random_edge()


graph.stats()
