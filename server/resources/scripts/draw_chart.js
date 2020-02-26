function draw_chart(data_for_draw, container, box_container) { //stadistic-container
  $('#' + container).remove(); // this is my <canvas> element
  $('#' + box_container).append('<canvas id="'+container+'"><canvas>');


  var ctx = document.getElementById(container).getContext('2d');

  var chartColors = {
  	red: 'rgb(255, 99, 132)',
  	orange: 'rgb(255, 159, 64)',
  	yellow: 'rgb(255, 205, 86)',
  	green: 'rgb(75, 192, 192)',
  	blue: 'rgb(54, 162, 235)',
  	purple: 'rgb(153, 102, 255)',
  	grey: 'rgb(201, 203, 207)'
  };

  datasets = [];
  for(var algorithm_index = 0; algorithm_index < data_for_draw.algorithms.length; algorithm_index++) {
    var algorithm = data_for_draw.algorithms[algorithm_index];
    if (!algorithm.checked) continue;

    datasets.push({
      label: algorithm.title,
      backgroundColor: chartColors[algorithm.color],
      borderColor: chartColors[algorithm.color],
      data: algorithm.times,
      fill: false,
    });
  }

  var X = data_for_draw.nodes;
  var config = {
		type: 'line',
		data: {
			labels: X.map(x => x.toString()),
			datasets
		},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'Labs'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Num Nodes'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Time'
					}
				}]
			}
		}
	};

  var theChart = new Chart(ctx, config);

}
