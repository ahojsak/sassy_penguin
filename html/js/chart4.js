
data = {
	'funny, useful':	2.886431455,
	'funny':	3.380472475,
	'useful':	3.60359822,
	'funny, cool':	3.757270694,
	'funny, cool, useful':	3.769270208,
	'none':	3.876614412,
	'cool, useful':	4.043354888,
	'cool': 	4.170183291
};
var n = 1, // number of samples
	m = 8; // number of series

var margin = {top: 20, right: 30, bottom: 30, left: 60},
	width = 700 - margin.left - margin.right,
	height = 350 - margin.top - margin.bottom;

var y = d3.scale.linear()
	.domain([0, 5])
	.range([height, 0]);

var x0 = d3.scale.ordinal()
	.domain(Object.keys(data))
	.rangeBands([width, 0], .2,0);

var x1 = d3.scale.ordinal()
	.domain([0,1,2,3,4,5,6,7])
	.rangeBands([width, 0], .2,0);

var z = d3.scale.category20();

var xAxis = d3.svg.axis()
	.scale(x0)
	.orient("bottom");

var yAxis = d3.svg.axis()
	.scale(y)
	.orient("left");

var svg = d3.select("#chart4").append("svg")
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
var values = Object.keys(data).map(function(key){
    return data[key];
});
// Draw bars
svg.append("g").selectAll("g")
	.data(values)
  .enter().append("g")
	.style("fill", function(d, i) { return z(i); })
	.attr("transform", function(d, i) { return "translate(" + x0(i) + ",0)"; })
  .append("rect")
	.attr("width", x1.rangeBand())
	.attr("height", function(d) {  return height - y(d); })
	.attr("x", function(d, i) { return x1(i); })
	.attr("y", function(d) { return y(d); });