from server.Services import Services
from server.GraphAlgorithms import GraphAlgorithms
from server.GraphServices import GraphServices
import statistics


class GraphLab(Services):

    def __init__(
        self,
        graphServices=GraphServices(),
        graphAlgorithms=GraphAlgorithms()
    ):
        Services.__init__(self)
        self.graphAlgorithms = graphAlgorithms
        self.graphServices = graphServices

    def process(self, num_nodes, probability_edges, directed, epoch, type, algorithm):
        print("Process Lab. NumNodes [" + str(num_nodes) + "]")
        print("Algorithm ["+algorithm+"] Repeticiones[" + str(epoch) + "]")

        time_list = []

        for i in range(epoch):
            result_graph = self.incremental_process(num_nodes, probability_edges, directed, type)

            result_matrix = self.run_algorithm(result_graph, algorithm)
            time_list.append(result_matrix['time'])

        return {
            "mean": statistics.mean(time_list),
            "num_nodes": num_nodes,
            "epoch": epoch
        }

    def incremental_process(
        self,
        num_nodes,
        probability_edges,
        directed,
        type="insert_random_edge"
    ):
        if type == 'insert_random_edge':
            return self.graphServices.create_graph_and_insert_random_edge(
                num_nodes,
                probability_edges,
                directed)

        if type == 'insert_random_node':
            return self.graphServices.create_graph_and_insert_random_node(
                num_nodes,
                probability_edges,
                directed)

        if type == 'decrease_random_weight':
            return self.graphServices.create_graph_and_decrease_random_weight(
                num_nodes,
                probability_edges,
                directed)


    def run_algorithm(self, data, algorithm):

        if algorithm == 'dijkstra-apsp':
            return self.graphAlgorithms.run_algorithm_dijkstra_apsp(data['graph']['values'])

        if algorithm == 'floyd-warshall':
            return self.graphAlgorithms.run_algorithm_floyd_warshall(data['graph']['values'])

        if algorithm == 'rr-bfs-truncated':
            return self.graphAlgorithms.run_algorithm_rr_bfs_truncated(data['graph']['values'], data['dist'])

        if algorithm == 'even-gazit':
            return self.graphAlgorithms.run_algorithm_eg(data['graph']['values'], data['dist'])

        if algorithm == 'quinca':
            return self.graphAlgorithms.run_algorithm_quinca(data['graph']['values'], data['dist'])

        if algorithm == 'owner':
            return self.graphAlgorithms.run_algorithm_owner(data['graph']['values'], data['dist'])

        if algorithm == 'forest':
            return self.graphAlgorithms.run_algorithm_forest(data['graph']['values'], data['dist'])
