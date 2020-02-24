/*
===========================================================
graph_render
===========================================================
It's a var global with graph renderizong

*/
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
    layout: {'name': 'circle'},
    style: [
      {
        selector: ".autorotate",
        style: {
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
        selector: "edge",
        style: style_seted
      },
      {
        selector: ".added",
        style: {
          'color': '#FF0000',
          'line-color': '#FF0000',
          'opacity': 0.5
        }
      }],
    elements: data_for_load_graph.elements,
  });
}

function graph_update(values) {
  if( values.last_vertex_action == "ADD" ) {
    console.log(values.last_vertex_modified);
    var source = values.last_vertex_modified[0];
    var target = values.last_vertex_modified[1];

    return graph_render.add([
      {
        group: "edges",
        data: {
          id: source+"-"+target,
          source,
          target,
          label: values.last_vertex_modified[2]
        },
        clasess: "added",
        style: {
          'color': '#FF0000',
          'line-color': '#FF0000',
          'opacity': 1.0
        }
      }

    ]);
  }

  else if( values.last_vertex_action == "DELETE" ) {
    console.log(values.last_vertex_modified);
    var source = values.last_vertex_modified[0];
    var target = values.last_vertex_modified[1];

    return graph_render.remove("#" + source + "-" + target);
  }

  else if( values.last_vertex_action == "UPDATE" ) {
    console.log(values.last_vertex_modified);
    var source = values.last_vertex_modified[0];
    var target = values.last_vertex_modified[1];
    var weight = values.last_vertex_modified[2];

    return graph_render.$("#" + source + "-" + target).data("label", weight);
  }

}
