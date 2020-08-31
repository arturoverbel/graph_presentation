from generate_and_result import run
from export_fig import draw_all_plot, draw_group_plot
from folder import get_folder
import pandas as pd
import sys
from os import listdir
from os.path import isfile, join

types = ['insert_edge', 'decrease_edge', 'insert_worst_edge', 'decrease_worst_edge']
num_nodes = [100,1000,10000]
probability_edges = [0.1, 0.2, 0.3, 0.4, 0.5, 0.01, 0.02, 0.03, 0.04, 0.05]


def read_files(files=[]):
    datas = pd.DataFrame()

    for filename in files:
        data_import = pd.read_csv(filename)
        datas = pd.concat([datas, data_import])

    #datas['density'] = round(datas['density'], 2)

    return datas

def draw():
    files = []
    to_draw = []

    for type in types:
        for num_node in num_nodes:
            found = False
            for pp in probability_edges:
                dir_results = get_folder("results", type, num_node, pp)
                onlyfiles = [dir_results + f for f in listdir(dir_results) if isfile(join(dir_results, f))]

                found = len(onlyfiles) > 0
                files = files + onlyfiles

            if found:
                to_draw.append({'type': type, 'nodes': num_node})

    df = read_files(files)

    for ff in to_draw:
        type_to_draw = ff['type']
        num_node_draw = ff['nodes']

        print("--------------------------------------------------")
        print('To Draw [' + type_to_draw + '][' + str(num_node_draw) + ']')
        draw_all_plot(df, num_node_draw, type_to_draw, densityTypes=0)
        draw_group_plot(df, num_node_draw, type_to_draw, densityTypes=0)

        draw_all_plot(df, num_node_draw, type_to_draw, densityTypes=1)
        draw_group_plot(df, num_node_draw, type_to_draw, densityTypes=1)


draw()
