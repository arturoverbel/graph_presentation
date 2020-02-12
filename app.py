from flask import Flask
from server.routing import graph_routing

app = Flask(__name__)
app.register_blueprint(graph_routing)

if __name__ == '__main__':
    app.run()
