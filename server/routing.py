from server.GraphServices import GraphServices
from server.GraphAlgorithms import GraphAlgorithms
from flask import Blueprint, render_template, request
from flask import Response
import json

graph_routing = Blueprint('graph', __name__, template_folder='templates')
graphServices = GraphServices()
graphAlgorithms = GraphAlgorithms()

@graph_routing.route('/')
def main():
    return render_template('index.html')


@graph_routing.route('/graph/generates')
def lab_graph_generates():
    return render_template('lab_graph_generates.html')


@graph_routing.route('/graph/create', methods=['POST'])
def graph_create():
    req_data = request.get_json()

    num_nodes = req_data['num_nodes']
    probability_edges = req_data['probability_edges']
    directed = req_data['directed']

    graph_result = graphServices.create_graph(num_nodes, probability_edges, directed)
    return Response(json.dumps(graph_result), mimetype='application/json')

@graph_routing.route('/graph/dynamic/incremental-edge', methods=['POST'])
def dynamic_incremental_random_edge():
    req_data = request.get_json()
    values = req_data['values']
    result = graphServices.dynamic_incremental_random_edge(values)

    return Response(json.dumps(result), mimetype='application/json')

@graph_routing.route('/graph/algorithms/floyd-warshall', methods=['POST'])
def run_algoritm_floyd_warshall():
    req_data = request.get_json()
    values = req_data['values']
    result = graphAlgorithms.run_algoritm_floyd_warshall(values)

    return Response(json.dumps(result), mimetype='application/json')

@graph_routing.route('/graph/algorithms/dijkstra', methods=['POST'])
def run_algoritm_dijkstra():
    req_data = request.get_json()
    values = req_data['values']
    source = req_data['source']
    result = graphAlgorithms.run_algoritm_dijkstra(values, source)

    return Response(json.dumps(result), mimetype='application/json')

@graph_routing.route('/graph/algorithms/dijkstra-apsp', methods=['POST'])
def run_algoritm_dijkstra_apsp():
    req_data = request.get_json()
    values = req_data['values']
    result = graphAlgorithms.run_algoritm_dijkstra_apsp(values)

    return Response(json.dumps(result), mimetype='application/json')
