import matplotlib.pyplot as plt
from matplotlib import colors
from folder import get_folder
import seaborn as sns
import numpy as np

def return_colors(algorithms=[]):
    colors = {
        'rr-bfs-truncated': "#0000FF",
        'even-gazit': "#808000",
        'quinca': "#FFFF00",
        'abm': "#FF0000",
        'forest': "#008080"
    }
    colors_return = []
    if algorithms:
        for al in algorithms:
            colors_return.append(colors[al])
    else:
        for c in colors:
            colors_return.append(colors[c])

    return colors

def sortListByIndexing(data, sorted):
    newD = []
    for iS in sorted:
        newD.append(data[iS])

    return newD

def calcLimit(totalTimes):
    timesByAlgoritmhs=[]
    for ii in range(len(totalTimes[0])):
        timesByAlgoritmhs.append([])

    for jj in range(len(totalTimes)):
        for ii in range(len(totalTimes[jj])):
            timesByAlgoritmhs[ii].append(totalTimes[jj][ii])

    max = 0
    maxOtherLine = 0
    min = np.inf
    indexMax = -1

    for ii in range(len(timesByAlgoritmhs)):
        #print(timesByAlgoritmhs[ii])
        for value in timesByAlgoritmhs[ii]:
            if value > max:
                max = value
                indexMax = ii

    maxOtherLineRead = []
    count = 0
    minDefined = False
    while True:
        for ii in range(len(timesByAlgoritmhs)):

            if ii == indexMax:
                if not minDefined:
                    for value in timesByAlgoritmhs[ii]:
                        if value < min:
                            min = value
                continue
            for value in timesByAlgoritmhs[ii]:
                if value > maxOtherLine and value not in maxOtherLineRead:
                    maxOtherLine = value

        if maxOtherLine > min:
            count = count + 1
            if count == 5:
                break
            min = maxOtherLine
            minDefined = True
            maxOtherLineRead.append(maxOtherLine)
            maxOtherLine = 0
        else:
            break

    return [maxOtherLine, min, max]

def algorithms_faster(data, fasterNum=3):

    algoritms_selected = []

    while True:
        dd = data.groupby('algorithm')['time'].mean().to_frame().sort_values(by=['time'])
        algoritms_selected = dd.index.tolist()[:fasterNum]

        if 'abm' in algoritms_selected:
            break

        fasterNum += 1


    return algoritms_selected

def draw_all_plot(data, num_nodes, type_incremental, densityTypes = 0):
    data_filter = data.loc[ (data['nodes'] == num_nodes) & (data['type'] == type_incremental)]

    data_filter_one_calc = data_filter.groupby('algorithm')['time'].mean().to_frame()
    data_filter_one_calc['algorithm'] = data_filter_one_calc.index.values

    #PLOT
    draw_plot_seaborn_bar(
        data_filter,
        num_nodes=num_nodes,
        type_incremental=type_incremental,
        densityGroup=False,
        densityTypes=densityTypes
    )


# Draw Group Density
def draw_group_plot(data, num_nodes, type_incremental, densityTypes=0):
    data_filter = data.loc[ (data['nodes'] == num_nodes) & (data['type'] == type_incremental)]

    data_filter_one_calc = data_filter.groupby('algorithm')['time'].mean().to_frame()
    data_filter_one_calc['algorithm'] = data_filter_one_calc.index.values

    draw_plot_seaborn_bar(
        data_filter,
        num_nodes=num_nodes,
        type_incremental=type_incremental,
        densityGroup=True,
        densityTypes=densityTypes
    )


def draw_plot_seaborn_bar(
    data,
    num_nodes=100,
    type_incremental='insert_edge',
    densityGroup=True,
    densityTypes = 0
):
    width = 0.85
    colors_g = sns.xkcd_palette(['windows blue', 'amber', 'greyish',  'faded green', 'dusty purple'])

    dir = get_folder("figs", type_incremental, num_nodes)
    groupF = 'density' if densityGroup else 'algorithms'
    densityF = 'small' if densityTypes == 0 else 'large'

    densityValues = list(dict.fromkeys(data['density'].values.tolist()))
    if densityTypes == 0:
        densityValues = [i for i in densityValues if i < 0.08]
    else:
        densityValues = [i for i in densityValues if i > 0.08]

    if densityValues:
        data = data.loc[data['density'].isin(densityValues)]

    filename = dir + "fig_" + type_incremental + "_" + str(num_nodes) + "_" + groupF + "_" + densityF
    dataToPrint = None
    #colors_g = [(0.21568627450980393, 0.47058823529411764, 0.7490196078431373), '#fb5607', '#8a5a44', '#8338ec', '#edc4b3']

    """
    blabla = data.groupby('density')['time'].mean().to_frame()
    #print(data.loc[(data['density'] == 0.01) & (data['algorithm'] == 'abm')])
    print(blabla)
    """

    if densityGroup:
        ### Print FIG Times vs Density, group Algorithms)
        faster_al = algorithms_faster(data, fasterNum=4)
        data_filter = data.loc[data['algorithm'].isin(faster_al)]

        dataToPrint = data_filter
        ax = sns.barplot(y='time', x='density', data=data_filter, hue="algorithm", capsize=.2, palette=return_colors())
        ax.set(xlabel='Edge Density', ylabel='Time (Miliseconds)')
    else:
        ### Print FIG Times vs Algorithms (Group Density)
        fig, ax = plt.subplots()
        data_gg = data.groupby('algorithm')['time'].mean().to_frame()

        densitySorted = sorted(densityValues)

        totalLabels = []
        totalTimes = []
        totalDensity =[]
        totalColor = []

        valuesABM = []

        dataToPrint = data

        for index_d in range(len(densityValues)):
            xLabels = data_gg.index.to_list()
            density = densityValues[index_d]

            indexForColor = densitySorted.index(densityValues[index_d])

            color = colors_g[indexForColor]

            data_filtered = data.loc[data['density'] == density]
            data_filtered_g = data_filtered.groupby('algorithm')['time'].mean().to_frame()
            listed = data_filtered_g['time'].to_list()
            #listed, xLabels = [ list(tuple) for tuple in  zip(*sorted(zip(listed, xLabels), reverse=True))]

            totalDensity.append(density)
            totalLabels.append(xLabels)
            totalTimes.append(listed)
            totalColor.append(color)

            for jj in range(len(xLabels)):
                if xLabels[jj] == 'abm':
                    valuesABM.append(listed[jj])

        ABMsorted = sorted(range(len(valuesABM)), key=lambda k: valuesABM[k])
        ABMsorted.reverse()

        """
        for times in totalTimes:
            print(times)
        for label in totalLabels:
            print(label)
        """

        limit = calcLimit(totalTimes)
        #if filename == "figs/insert_worst_edge/100/fig_insert_worst_edge_100_algorithms_small":

        ### Start to Draw

        fig, (ax1,ax2) = plt.subplots(2,1,sharex=True, figsize=(5,6))
        ax1.spines['bottom'].set_visible(False)
        ax1.tick_params(axis='x',which='both',bottom=False)
        ax2.spines['top'].set_visible(False)

        ax2.set_ylim(0, limit[0])
        ax1.set_ylim(limit[1],limit[2])

        for i in ABMsorted:
            density = round(totalDensity[i], 2)

            xLabels = totalLabels[i]
            listed = totalTimes[i]
            color = totalColor[i]

            """
            print("-------------------------------------------------")
            print(xLabels)
            print(listed)
            print(density)
            print(color)
            """
            bars1 = ax1.bar(xLabels, listed, width, label=str(density), color=color)
            bars2 = ax2.bar(xLabels, listed, width, label=str(density), color=color)

            for tick in ax2.get_xticklabels():
                tick.set_rotation(0)
            d = .015
            kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
            ax1.plot((-d, +d), (-d, +d), **kwargs)
            ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
            kwargs.update(transform=ax2.transAxes)
            ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
            ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

            for b1, b2 in zip(bars1, bars2):
                posx = b2.get_x() + b2.get_width()/2.
                if b2.get_height() > limit[0]:
                    ax2.plot((posx-3*d, posx+3*d), (1 - d, 1 + d), color='k', clip_on=False,
                             transform=ax2.get_xaxis_transform())
                if b1.get_height() > limit[1]:
                    ax1.plot((posx-3*d, posx+3*d), (- d, + d), color='k', clip_on=False,
                             transform=ax1.get_xaxis_transform())
        ax1.set_ylabel('Times (Miliseconds)')
        ax1.legend()
        plt.xticks(rotation=45)

    #Export to file

    if True:
        if dataToPrint is not None:
            dataToPrint.to_csv (filename + '.csv', index=False, header=True)
        plt.tight_layout()
        plt.savefig(filename + '.png', dpi=150)
        plt.cla()
        plt.clf()

    #plt.show()
