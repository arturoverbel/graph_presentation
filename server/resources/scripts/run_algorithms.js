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
