function load_graph(num_nodes, pro_edges, directed) {
  return $.ajax({
      method: "POST",
      url: "/graph/create",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({
         "num_nodes": parseInt(num_nodes),
         "probability_edges": parseFloat(pro_edges),
         directed
      })
  });
}

function load_graph_incremental_random_edge(values) {
  return $.ajax({
      method: "POST",
      url: "/graph/dynamic/incremental-edge",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({ "values": values })
  });
}