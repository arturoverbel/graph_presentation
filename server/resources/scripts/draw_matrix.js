function draw_matrix(matrix, matrix_container, graph_draw_matrix_flag) {
  if (graph_draw_matrix_flag == false) return;

  var htmlBODY = "<tbody>";
  var htmlHEAD = "<thead>";

  var vertexes = graph_values.vertex;

  htmlBODY += "<tr><td></td>";
  htmlHEAD += "<tr><td></td>";
  for (index_vv = 0; index_vv < vertexes.length; index_vv++) {
    htmlBODY += "<td><b>" + vertexes[index_vv] + "</b></td>";
    htmlHEAD += "<td></td>";
  }
  htmlBODY += "</tr>";
  htmlHEAD += "</tr>";


  for (index_row = 0; index_row < matrix.length; index_row++) {
    row = matrix[index_row];
    htmlBODY += "<tr>";
    htmlBODY += "<td><b>" + vertexes[index_row] + "</b></td>";

    for (index = 0; index < row.length; index++) {
      cell = row[index]
      htmlBODY += "<td>" + cell + "</td>";
    }

    htmlBODY += "</tr>";
  }

  htmlBODY += "</tbody>";
  htmlFULL = htmlHEAD + htmlBODY;

  $('#' + matrix_container).html(htmlFULL);

  if ( $.fn.dataTable.isDataTable( '#' + matrix_container ) ) {
    $('#' + matrix_container).DataTable();
  }
  else {
    $('#' + matrix_container).DataTable({
      "paging":   false,
      "ordering": false,
      "info":     false,
      "searching": false,
      "drawCallback": function( settings ) {
        $("#" + matrix_container + " thead").remove();
      }
    });
  }

}
