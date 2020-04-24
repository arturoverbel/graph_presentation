import os
import sys
import json
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

limit_to_calc = 20

from algorithms.Algorithms import Algorithm

folder = "graph_generate/synthetics/"
file_result = "server/resources/results/result.json"

def times_from_file(path):
    with open(path) as json_file:
        data_values = json.load(json_file)

    algorithm = Algorithm(data_values)
    algorithm_list = algorithm.list()

    data_result = {}

    result = algorithm.run_algorithm('floyd-warshall')
    dist = result['matrix']

    for algorithm_name in algorithm_list['incremental']:
        result = algorithm.run_algorithm(algorithm_name, dist)
        data_result[algorithm_name] = result['time']

    return data_result


if len(sys.argv) == 2:
    filename = sys.argv[1]
    path = folder + filename
    result = times_from_file(path)
    print(result)
    exit()

files = os.listdir(folder)
files.sort()

data_result = {}

counter = 0
for file in files:
    path = folder + file
    print("Calculating " + file + " ...")
    result = times_from_file(path)
    data_result[file] = result

    counter += 1
    if counter > limit_to_calc:
        break

with open(file_result, 'w') as outfile:
    json.dump(data_result, outfile)
