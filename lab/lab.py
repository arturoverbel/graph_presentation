from generate_and_result import run
from export_fig import draw_all_plot, draw_group_plot
import pandas as pd

def read_files(files=[]):
    datas = pd.DataFrame()

    for filename in files:
        data_import = pd.read_csv(filename)
        datas = pd.concat([datas, data_import])

    #datas['density'] = round(datas['density'], 2)

    return datas


def exec(
    num_graphs_random=30,
    try_exec_each_graph=10
):
    types = [
        'insert_edge',
        'decrease_edge',
        'insert_worst_edge',
        'decrease_worst_edge'
    ]

    num_nodes = [
        100,
        1000,
        10000
    ]

    probability_edges = [
        0.1,
        0.2,
        0.3,
        0.4,
        0.5,
        0.01,
        0.02,
        0.03,
        0.04,
        0.05
    ]

    files = []

    for type in types:
        for num_node in num_nodes:
            for pp in probability_edges:
                # Dataframe
                result = run(
                    type,
                    num_node,
                    pp,
                    num_try = num_graphs_random,
                    attempt = try_exec_each_graph,
                    saveFileExec = True,
                    labExec=True
                )

                files.append(result['filename'])

    df = read_files(files)

    for type in types:
        for num_node in num_nodes:
            draw_all_plot(df, num_node, type, densityTypes=0)
            draw_group_plot(df, num_node, type, densityTypes=0)

            draw_all_plot(df, num_node, type, densityTypes=1)
            draw_group_plot(df, num_node, type, densityTypes=1)



exec()
