function refresh_graph(graph_container, draw_container) {
  $('#' + graph_container).remove();
  $('#' + draw_container).html('<div id="'+graph_container+'"></div>');
}

function create_graph(data_for_load_graph, graph_container, draw_container) {
  refresh_graph(graph_container,  draw_container);

  style_seted = {
    'width': 2,
    'label': 'data(label)',
    'line-color': '#3a7ecf',
    'opacity': 0.5
  }

  if (data_for_load_graph.values.directed == 'true') {
    style_seted['curve-style'] ='bezier';
    style_seted['target-arrow-shape'] ='triangle';
  }

  graph_render = cytoscape({
    container: document.getElementById(graph_container),
    elements: data_for_load_graph.elements,
    style: [
      {
        "selector": ".autorotate",
        "style": {
          "edge-text-rotation": "autorotate",
          "text-background-opacity": 1
        }
      },
      {
        selector: 'node',
        style: {
          'label': 'data(id)',
          'text-valign': 'center',
          'color': '#000000',
          'background-color': '#3a7ecf'
        }
      },

      {
        selector: 'edge',
        style: style_seted
      }
    ]
  });
}
