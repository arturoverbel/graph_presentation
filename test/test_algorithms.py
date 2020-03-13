from graph.Graph import Graph


class TestClass:

    def define_graph(self):
        sources = [1, 2, 3, 0, 4, 1, 2, 1, 3]
        targets = [0, 0, 0, 4, 0, 2, 1, 3, 1]
        weights = [2, 2, 4, 1, 1, 3, 3, 2, 2]

        graph = Graph(sources, targets, weights)

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")