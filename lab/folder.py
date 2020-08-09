import os

def get_folder(folder, type_incremental, num_nodes, probability_edges=0):

    dirType = folder + "/" + type_incremental + "/"
    if not os.path.exists(dirType):
        os.mkdir(dirType)

    dirNode = dirType + str(num_nodes) + "/"
    if not os.path.exists(dirNode):
        os.mkdir(dirNode)

    if probability_edges == 0:
        return dirNode

    dirEdge = dirNode + str(probability_edges) + "/"
    if not os.path.exists(dirEdge):
        os.mkdir(dirEdge)

    return dirEdge
