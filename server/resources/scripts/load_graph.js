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
