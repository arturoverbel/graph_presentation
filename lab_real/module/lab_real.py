import os
import sys
import numpy as np
import json

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from graph.Graph import Graph

LAB_BASE_PATH = "data/"
LAB_BASE_RESULTS_PATH = "results/"
LAB_BASE_EXPORTED_PATH = "graph_exported/"


class LabReal:
    def __init__(self, testing=False):
        self.basePath = LAB_BASE_PATH
        self.baseExportedPath = LAB_BASE_EXPORTED_PATH
        self.baseResultsPath = LAB_BASE_RESULTS_PATH
        self.files = []

        self.testing = testing

    @staticmethod
    def export_matrix(matrix_result):
        matrix_to_export = []
        for row in matrix_result:
            matrix_to_export.append([
                str(a) if a == np.inf else str(int(a))
                for a in row
            ])

        return matrix_to_export

    @staticmethod
    def create_graph(file_stream):
        sources = []
        targets = []

        for line in file_stream:
            points = line.split()
            sources.append(int(points[0]))
            targets.append(int(points[1]))

        return Graph(sources, targets)

    @staticmethod
    def import_matrix(matrix_result):
        matrix_to_import = []
        for row in matrix_result:
            matrix_to_import.append([
                np.inf if a == "inf" else int(a)
                for a in row
            ])

        return np.array(matrix_to_import)

    def delete_file_testing(self, extension="test.json"):
        if not self.testing:
            return

        path = self.baseExportedPath

        for f in os.listdir(path):
            item = os.path.join(path, f)
            if os.path.isfile(item) and f.endswith(extension):
                os.remove(item)

    def import_all_files(self, filename="", extension=".txt"):
        self.files = []
        path = self.basePath

        if not path.endswith("/"):
            path += "/"

        if filename != "":
            file = path + filename
            self.files.append(file)

            return self.files

        for f in os.listdir(path):
            item = os.path.join(path, f)
            if os.path.isfile(item) and f.endswith(extension):
                self.files.append(path + f)
            if os.path.isdir(item):
                self.import_all_files(item)

        return self.files

    def get_folder_results(self, filename: str):
        filename = filename.replace(".txt", "")
        filename = filename.replace(".json", "")

        filename = filename.replace("/", "_")

        folder_name = f'{self.baseExportedPath}{filename}'

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        return folder_name

    def get_folder_calculated(self, filename: str):
        filename = filename.replace(".txt", "")
        filename = filename.replace(".json", "")

        filename = filename.replace("/", "_")

        folder_name = f'{self.baseResultsPath}{filename}'

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        return folder_name

    def import_graph_and_dist(self, filename):
        print("-----------------------")
        print("Filename: ", filename)

        file_stream = open(filename, "r")
        print("Creating graph ... ")
        graph = self.create_graph(file_stream)

        dist = self.get_dist_by_filename(filename)

        return graph, dist

    def get_dist_by_filename(self, filename: str):
        folder = self.get_folder_results(filename)
        file = f'{folder}/dist.json'

        json_file = open(file)
        dist = json.load(json_file)

        return dist
