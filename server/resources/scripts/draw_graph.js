function create_graph(data_for_load_graph, graph_container, graph_draw_flag) {
  if (graph_draw_flag == false) return;

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

  return cytoscape({
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

function graph_update(render, values) {
  if( values.last_vertex_action == "ADD" ) {
    var source = values.last_vertex_modified[0];
    var target = values.last_vertex_modified[1];

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

    render.add([
      {
        "selector": ".added",
        "style": {
          'color': '#FF0000',
        }
      },

      {
        group: "edges",
        data: {
          id: source+"-"+target,
          source,
          targe,
          label: values.last_vertex_modified[2]
        },
        "clasess": "autorotate added"
      }

    ])
  }
}
