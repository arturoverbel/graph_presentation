function run_algorithm_floyd_warshall(graph_values) {
  return $.ajax({
      method: "POST",
      url: "/graph/algorithms/floyd-warshall",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({
         "values": graph_values
      })
  });
}

function run_algorithm_dijkstra(graph_values, source) {
  return $.ajax({
      method: "POST",
      url: "/graph/algorithms/dijkstra",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({
         "values": graph_values,
         "source": source
      })
  });
}

function run_algorithm_dijkstra_apsp(graph_values) {
  return $.ajax({
      method: "POST",
      url: "/graph/algorithms/dijkstra-apsp",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({
         "values": graph_values
      })
  });
}
