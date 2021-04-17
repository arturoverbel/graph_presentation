import os
import sys
import json
from module.lab_real import LabReal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from graph.Graph import Graph
from algorithms.dijkstra import *
from algorithms.floyd_warshall import *
from algorithms.Algorithm import get_incremental_action


class ExportLabReal(LabReal):
    def __init__(self, testing=False):
        self.export_only_new = False
        LabReal.__init__(self, testing)

    def return_name_file_exported(self, filename):
        filename = filename.replace("txt", "json")
        return f'{self.baseExportedPath}graph,file={filename.replace("/", "_")}'

    def check_file_exist(self, filename):
        if not self.export_only_new:
            return False

        name_file = self.return_name_file_exported(filename)

        if os.path.exists(name_file):
            print(name_file, " Already exists.")
            return True

        print(name_file, " Is new!")
        return False

    def import_file(self, file=""):
        print("---------------------------------------------")
        print("Filename: ", file)

        file_stream = open(file, "r")

        print("Creating graph ... ")
        graph = self.create_graph(file_stream)

        print("Calculating matrix distances ... ")
        dist_before = Dijkstra_apsp(graph)

        return graph, dist_before

    def calculate_action_incremental(self, graph: Graph, incremental: str):

        # graph.print_r()
        print(f'Action incremental {incremental} ... ')
        data_update = graph.action_incremental(incremental, set_action_to_graph=False)
        print("Added ", data_update)

        return data_update

    def export_graph(self, graph: Graph, dist_before: list, filename: str, actions_incremental: []):

        fileJson = filename.replace("txt", "json")
        json_file = open(fileJson)
        data_info = json.load(json_file)

        data_info.update(graph.export_values())
        print("Preparing exportation ...")
        name = self.return_name_file_exported(filename)

        graph_values = {
            "graph": data_info,
            "actions_incremental": actions_incremental,
            "dist": LabReal.export_matrix(dist_before)
        }

        print(graph_values)

        print("Exporting ", name, "...")

        with open(name, 'w') as fp:
            json.dump(graph_values, fp)
            print("File " + name + " exported")

    def export_data(self, dist_before: list, filename: str, file_result: str):

        folder = self.get_folder_results(filename)
        print(f'Exporting {file_result} ...')
        name_dist_result = f'{folder}/{file_result}.json'

        with open(name_dist_result, 'w') as fp:
            json.dump(dist_before, fp)
            print(f'file {file_result} exported')

    def export_lab_real(self, filename=""):
        # self.delete_file_testing()
        incremental_actions = get_incremental_action()
        self.import_all_files(filename=filename)

        for filename in self.files:
            if self.check_file_exist(filename):
                continue

            graph, dist = self.import_file(filename)
            self.export_data(dist.tolist(), filename, "dist")

            actions_incremental = []

            for action_incremental in incremental_actions:
                action = self.calculate_action_incremental(graph, action_incremental)
                self.export_data(action, filename, f'incremental_{action_incremental}')
