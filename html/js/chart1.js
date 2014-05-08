d3.csv("data/chart1.txt", 
	function(d) {
		return [d.funny, d.cool, d.useful];
	}, function(error, data) {
		data = d3.transpose(data);
		console.log(data);
		var n = 7, // number of samples
			m = 3; // number of series

		var margin = {top: 20, right: 30, bottom: 30, left: 60},
			width = 640 - margin.left - margin.right,
			height = 400 - margin.top - margin.bottom;

		var y = d3.scale.linear()
			.domain([0, 270000])
			.range([height, 0]);

		var x0 = d3.scale.ordinal()
			.domain(d3.range(n))
			.rangeBands([0, width], .2,0);

		var x1 = d3.scale.ordinal()
			.domain(d3.range(m))
			.rangeBands([0, x0.rangeBand()]);

		var z = d3.scale.category20c();

		var xAxis = d3.svg.axis()
			.scale(x0)
			.orient("bottom");

		var yAxis = d3.svg.axis()
			.scale(y)
			.orient("left");

		var svg = d3.select("#chart1").append("svg")
			.attr("width", width + margin.left + margin.right)
			.attr("height", height + margin.top + margin.bottom)
		  .append("svg:g")
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
		
		
		// Make axes
		svg.append("g")
			.attr("class", "y axis")
			.call(yAxis);

		svg.append("g")
			.attr("class", "x axis")
			.attr("transform", "translate(0," + height + ")")
			.call(xAxis);
		
		// Draw bars
		svg.append("g").selectAll("g")
			.data(data)
		  .enter().append("g")
			.style("fill", function(d, i) { return z(i); })
			.attr("transform", function(d, i) { return "translate(" + x1(i) + ",0)"; })
		  .selectAll("rect")
			.data(function(d) { return d; })
		  .enter().append("rect")
			.attr("width", x1.rangeBand())
			.attr("height", function(d) { return height - y(d); })
			.attr("x", function(d, i) { return x0(i); })
			.attr("y", function(d) { return y(d); });
			
		// Ad legend
		var legend = svg.selectAll(".legend")
			.data(['funny','cool','useful'])
		.enter().append("g")
			.attr("class", "legend")
			.attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

		legend.append("rect")
			.attr("x", width - 18)
			.attr("width", 18)
			.attr("height", 18)
			.style("fill", function(d, i) { return z(i); });

		legend.append("text")
			.attr("x", width - 24)
			.attr("y", 9)
			.attr("dy", ".35em")
			.style("text-anchor", "end")
			.text(function(d) { return d; });
});