import os
import sys
import json
import numpy as np
from module.lab_real import LabReal
from algorithms.Algorithm import get_incremental_action

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from algorithms.Algorithm import Algorithm


class CalculateLabRealDist(LabReal):
    def __init__(self, filename="", testing=False):
        LabReal.__init__(self, testing)

        files = self.import_all_files(filename)
        self.filename = files[0]
        self.graph = self.import_graph(self.filename)

        fileJson = self.filename.replace("txt", "json")
        json_file = open(fileJson)
        self.data_info = json.load(json_file)
        self.density = self.data_info['edges'] / self.data_info['nodes'] * self.data_info['nodes']

    def calculate_action_incremental(self, action="insert_edge", attempt=2):
        calculate = Algorithm()
        calculate.set_graph(self.graph)

        if not self.check_action_exist(action):
            self.graph.action_incremental(action, set_action_to_graph=True)
        else:
            action_incremental = self.import_action_incremental(action)
            self.use_action_incremental(action_incremental)

        list_algorithms = ['dijkstra-apsp']

        for algorithm_name in list_algorithms:
            results = []

            calculate.attempt = attempt
            calculate.attempt = 1

            times = calculate.run_algorithm(algorithm_name)
            for time_insta in times:
                results.append({
                    "algorithm": algorithm_name,
                    "time": time_insta,
                    "nodes": len(calculate.graph.nodes),
                    "edges": len(calculate.graph.source),
                    "density": self.density,
                    "type": action
                })

            self.export_results(results, algorithm_name, action)

    def use_action_incremental(self, action):
        if action['last_edge_action'] == "ADD":
            self.graph.insert_edge(
                action['last_edge_updated'][0],
                action['last_edge_updated'][1],
                action['last_edge_updated'][2]
            )

        elif action['last_edge_action'] == "DECREASE":
            self.graph.decrease_weight(
                action['last_edge_updated'][0],
                action['last_edge_updated'][1],
                action['last_edge_updated'][2]
            )

    def import_action_incremental(self, action="insert_edge"):
        folder = self.get_folder_results(self.filename)

        file_incremental = f'{folder}/incremental_{action}.json'

        json_file = open(file_incremental)
        data_info = json.load(json_file)

        return data_info

    def check_action_exist(self, action: str):
        folder = self.get_folder_results(self.filename)
        file_incremental = f'{folder}/incremental_{action}.json'

        return os.path.exists(file_incremental)

    def export_results(self, results: [], algorithm_name: str, action: str):

        folder = self.get_folder_calculated(self.filename)
        file_to_save = f'{folder}/{algorithm_name}__{action}.json'
        print(f'Exporting {file_to_save} ...')

        with open(file_to_save, 'w') as fp:
            json.dump(results, fp)
            print(f'File {file_to_save} exported')

    def calculate(self, attempt=2):
        for action in get_incremental_action():
            self.calculate_action_incremental(action=action, attempt=attempt)

