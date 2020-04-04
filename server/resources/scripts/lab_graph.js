async function lab_graph_faster(
  start_num_nodes,
  end_num_nodes,
  pro_edges,
  directed,
  epoch,
  step,
  type,
  algorithms,
  info_container,
  chart_container,
  box_container
) {

  var result_lab = { nodes: [], algorithms };

  indexing = -1;
  for (var num_nodes = start_num_nodes; num_nodes <= end_num_nodes; num_nodes+=step) {
    indexing++;

    result_lab.nodes.push(num_nodes);
    algorithms.map(function(x){x.times.push(0); return x} );

    $('#' + info_container).html(`Num NODES: ${num_nodes}. Repeticiones (${epoch})`);
    for(var algorithm_index = 0; algorithm_index < algorithms.length; algorithm_index++) {
      var algorithm = algorithms[algorithm_index];
      if (!algorithm.checked) continue;

      var response = await processs_lab(num_nodes, pro_edges, directed, epoch, type, algorithm.name);
      algorithms[algorithm_index].times[indexing] = response.mean;

    }

    draw_chart(result_lab, chart_container, box_container)
  }

  return result_lab;
}
