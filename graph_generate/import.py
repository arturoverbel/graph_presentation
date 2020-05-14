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

file = "synthetics/" + filename


print("Filename: ", file)

data_import = {}
with open(file) as json_file:
    data_import = json.load(json_file)

print(data_import)

#graph = Graph.import_values(data_import)

#graph.insert_random_edge()


#graph.stats()
