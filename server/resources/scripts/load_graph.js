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

async function load_graph_and_incremental_edge(num_nodes, pro_edges, directed) {
  return $.ajax({
      method: "POST",
      url: "/graph/create-incremental-edge",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({
         "num_nodes": parseInt(num_nodes),
         "probability_edges": parseFloat(pro_edges),
         directed
      })
  });
}

async function processs_lab(num_nodes, pro_edges, directed, epoch, algorithm) {
  return $.ajax({
      method: "POST",
      url: "/graph/process-lab",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({
         "num_nodes": parseInt(num_nodes),
         "probability_edges": parseFloat(pro_edges),
         directed,
         epoch,
         algorithm
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

function load_graph_decrease_random_edge(values) {
  return $.ajax({
      method: "POST",
      url: "/graph/dynamic/decrease-edge",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({ "values": values })
  });
}

function load_graph_update_random_edge(values) {
  return $.ajax({
      method: "POST",
      url: "/graph/dynamic/update-edge",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({ "values": values })
  });
}
