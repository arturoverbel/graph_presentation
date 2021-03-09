import os
import sys
import json

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from graph.Graph import Graph

LAB_BASE_PATH = "data/"
LAB_BASE_EXPORTED_PATH = "graph_exported/"


class LabReal:
    def __init__(self):
        self.basePath = LAB_BASE_PATH
        self.baseExportedPath = LAB_BASE_EXPORTED_PATH
        self.files = []

    def import_file_to_graph(self, file="", incremental="random"):
        print("---------------------------------------------")
        fileJson = file.replace("txt", "json")

        print("Filename: ", file)

        file_stream = open(file, "r")
        print(type(file_stream))

        graph = self.create_graph(file_stream)
        if incremental == "worst":
            print("Inserting worst edge .... ")
            graph.insert_worst_edge()
            print("Inserted worst edge")
        else:
            print("Inserting random edge .... ")
            graph.insert_random_edge()
            print("Inserted random edge")

        json_file = open(fileJson)
        data_json = json.load(json_file)

        self.export_graph(graph, data_json, fileJson, incremental)

    @staticmethod
    def create_graph(file_stream):
        sources = []
        targets = []

        for line in file_stream:
            points = line.split()
            sources.append(int(points[0]))
            targets.append(int(points[1]))

        return Graph(sources, targets)

    def export_graph(self, graph: Graph, data_info: dict, filename="filename.json",
                     incremental="random"):
        data_info.update(graph.export_values())

        name = self.baseExportedPath + "_" + \
               "insertion_edge=" + incremental + "_" + \
               filename.replace("/", "_")

        print("Exporting ", name, "...")

        with open(name, 'w') as fp:
            json.dump(data_info, fp)
            print("File " + name + " exported")

    def import_all_files(self, path=""):
        if path == "":
            path = self.basePath

        if not path.endswith("/"):
            path += "/"

        for f in os.listdir(path):
            item = os.path.join(path, f)
            if os.path.isfile(item) and f.endswith(".txt"):
                self.files.append(path + f)
            if os.path.isdir(item):
                self.import_all_files(item)

    def run_lab_real(self):
        self.import_all_files()

        for filename in self.files:
            self.import_file_to_graph(filename, incremental="random")
            self.import_file_to_graph(filename, incremental="worst")
