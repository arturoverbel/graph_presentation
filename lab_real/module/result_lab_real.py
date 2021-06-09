import os
import sys
import json
import numpy as np
from module.lab_real import LabReal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')


class ResultLabReal(LabReal):
    def __init__(self):
        LabReal.__init__(self)

        self.files = []
        self.all_data = {}

        self.import_results(self.baseResultsPath)
        self.read_files()

    def read_files(self):
        for f in self.files:
            json_file = open(f)
            f_split = f.split("/")
            dataset = f_split[-2]
            dd = f_split[-1]
            dd_split = dd.split("__")
            algorithm = dd_split[0]
            type_incremental = dd_split[1]

            data = json.load(json_file)

            if dataset not in self.all_data:
                self.all_data[dataset] = {}

            if type_incremental not in self.all_data[dataset]:
                self.all_data[dataset][type_incremental] = {}

            if algorithm not in self.all_data[dataset][type_incremental]:
                self.all_data[dataset][type_incremental][algorithm] = 0

            times = np.array([])
            for d in data:
                times = np.append(times, d['time'])

            self.all_data[dataset][type_incremental][algorithm] = np.mean(times)

    def import_results(self, path, extension=".json"):
        if not path.endswith("/"):
            path += "/"

        for f in os.listdir(path):
            item = os.path.join(path, f)
            if os.path.isfile(item) and f.endswith(extension):
                self.files.append(path + f)
            if os.path.isdir(item):
                self.import_results(item)

        return self.files

    def stats(self):
        print(self.all_data)

