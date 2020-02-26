async function lab_graph(start_num_nodes, end_num_nodes, pro_edges, directed, epoch, algorithms, info_container) {

  var result_lab = { nodes: [], algorithms };

  for (var num_nodes = start_num_nodes; num_nodes <= end_num_nodes; num_nodes++) {
    result_lab.nodes.push(num_nodes);
    algorithms.map(function(x){x.times.push(0); return x} );
  }

  for (var num_nodes = start_num_nodes; num_nodes <= end_num_nodes; num_nodes++) {
    var indexing = num_nodes - start_num_nodes;

    total_time_mean = 0;

    for(var i = 0; i < epoch; i++) {
      $('#' + info_container).html("Num NODES: " + num_nodes + ". Epoch (" + i + ")");
      var response = await load_graph_and_incremental_edge(num_nodes, pro_edges, directed);

      var graph = response.graph
      var dist_bafore = response.dist

      for(var algorithm_index = 0; algorithm_index < algorithms.length; algorithm_index++) {
        var algorithm = algorithms[algorithm_index];
        if (!algorithm.checked) continue;

        var dist = null;
        if (algorithm.name == 'dijkstra-apsp')
          var dist = await run_algorithm_dijkstra_apsp(graph.values);

        if (algorithm.name == 'floyd-warshall')
          var dist = await run_algorithm_floyd_warshall(graph.values);

        if (algorithm.name == 'rr-bfs-truncated')
          var dist = await run_algoritm_rr_bfs_truncated(graph.values, dist_bafore);


        algorithms[algorithm_index].times[indexing] += dist.time;
      }

    }

    algorithms.map(function(algorithm){
      algorithm.times.map(x => x / epoch)
    });
    //result_lab.times.push(total_time_mean);
  }

  return result_lab;
}
