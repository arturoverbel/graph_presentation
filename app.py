from flask import Flask, send_from_directory
from server.routing import graph_routing

app = Flask(__name__)
app.register_blueprint(graph_routing)


@app.route('/resources/<path:path>')
def send_resources(path):
    return send_from_directory('server/resources', path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int("80"))
