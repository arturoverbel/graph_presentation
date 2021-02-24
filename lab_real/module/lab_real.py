import os
import sys
import json
import numpy as np
import pandas as pd

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from graph.Graph import Graph
from algorithms.Algorithm import Algorithm


class LabReal:
    def __init__(self, base_path="data/"):
        self.basePath = base_path
        self.files = []

    def import_file_to_graph(self, filename=""):
        file = self.basePath + filename
        fileJson = self.basePath + filename.replace("txt", "json")

        print("Filename: ", file)

        file_stream = open(file, "r")
        for line in file_stream:
            points = line.split()

        json_file = open(fileJson)
        data_json = json.load(json_file)
        print(data_json)

        return "ads"

    def import_all_files(self, path=""):
        if path == "":
            path = self.basePath

        for f in os.listdir(path):
            item = os.path.join(path, f)
            if os.path.isfile(item) and f.endswith(".txt"):
                self.files.append(f)
            if os.path.isdir(item):
                self.import_all_files(item)

    def run_lab_real(self):
        self.import_all_files()

        for filename in self.files:
            data_import = self.import_file_to_graph(filename)

            print("----------------------------------------")
