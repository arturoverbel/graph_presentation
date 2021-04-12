import os
import sys
import json
from module.lab_real import LabReal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from algorithms.Algorithm import Algorithm


class CalculateLabReal(LabReal):
    def __init__(self, testing=False):
        LabReal.__init__(self, testing)

    def create_graph_and_calculate(self, file="", attempt=2):
        print("-----------------------")
        print("Filename: ", file)

        # file_stream = open(file, "r")
        # print(type(file_stream))

        json_file = open(file)
        data_json = json.load(json_file)

        calculate = Algorithm(data_json['graph'])
        calculate.attempt = attempt

        results = []
        for algorithm_name in calculate.list()['incremental']:
            times = calculate.run_algorithm(algorithm_name, LabReal.import_matrix(data_json['dist']))
            for time_insta in times:
                results.append({
                    "algorithm": algorithm_name,
                    "time": time_insta,
                    "nodes": len(calculate.graph.nodes),
                    "edges": len(calculate.graph.source),
                    "density": data_json['graph']['density'],
                    "type": data_json['type_incremental']
                })

        return self.export_results(results, file)

    def export_results(self, results: [], filename: str):

        name = filename.replace(self.baseExportedPath, self.baseResultsPath)
        print(f'Exporting {name} ...')

        with open(name, 'w') as fp:
            json.dump(results, fp)
            print(f'File {name} exported')

    def calculate(self):
        self.import_all_files(path=self.baseExportedPath, extension=".json")

        for filename in self.files:
            self.create_graph_and_calculate(filename, attempt=2)
