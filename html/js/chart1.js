 // First, we define sizes and colours...
var outerW = 640; // outer width
var outerH = 480; // outer height
var padding = { t: 0, r: 0, b: 0, l: 0 };
var w = outerW - padding.l - padding.r; // inner width
var h = outerH - padding.t - padding.b; // inner height
var c = [ "#E41A1C", "#377EB8", "#4DAF4A" ]; // ColorBrewer Set 1

// Second, we define our data...
var numberGroups = 7; // groups
var numberSeries = 3;  // series in each group
d3.csv("data/votecounts.txt", 
	function(d) {
		return [d.funny, d.cool, d.useful];
	}, function(error, data) {
		data = d3.transpose(data);

		// Third, we define our scales...
		// Groups scale, x axis
		var x0 = d3.scale.ordinal()
			.domain(d3.range(numberGroups))
			.rangeBands([0, w],0.2,0);

		// Series scale, x axis
		// It might help to think of the series scale as a child of the groups scale
		var x1 = d3.scale.ordinal()
			.domain(d3.range(numberSeries))
			.rangeBands([0, x0.rangeBand()]);

		// Values scale, y axis
		var y = d3.scale.linear()
			.domain([0, 270000]) // Because Math.random returns numbers between 0 and 1
			.range([0, h]);

		// Visualisation selection
		var vis = d3.select("#chart1")
			.append("svg:svg")
			.attr("width", outerW)
			.attr("height", outerH);

		// Series selection
		// We place each series into its own SVG group element. In other words,
		// each SVG group element contains one series (i.e. bars of the same colour).
		// It might be helpful to think of each SVG group element as containing one bar chart.
		var series = vis.selectAll("g.series")
			.data(data)
		.enter().append("svg:g")
			.attr("class", "series") 
			.attr("fill", function (d, i) { return c[i]; })
			.attr("transform", function (d, i) { return "translate(" + x1(i) + ")"; });

		// Groups selection
		var groups = series.selectAll("rect")
			.data(Object) // The second dimension in the two-dimensional data array
		.enter().append("svg:rect")
			.attr("x", 0)
			.attr("y", function (d) { return h - y(d); })
			.attr("width", x1.rangeBand())
			.attr("height", y)
			.attr("transform", function (d, i) { return "translate(" + x0(i) + ")"; });
});