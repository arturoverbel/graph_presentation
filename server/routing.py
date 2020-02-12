from server.GraphServices import GraphServices
from flask import Blueprint, render_template, request
from flask import Response
import json

graph_routing = Blueprint('graph', __name__,
                          template_folder='templates')
graphServices = GraphServices()


@graph_routing.route('/')
def main():
    return render_template('index.html')


@graph_routing.route('/graph/create', methods=['POST'])
def graph_create():
    req_data = request.get_json()

    num_nodes = req_data['num_nodes']
    probability_edges = req_data['probability_edges']

    graph_result = graphServices.create_graph(num_nodes, probability_edges)
    return Response(json.dumps(graph_result), mimetype='application/json')
