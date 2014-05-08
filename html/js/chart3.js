var dataset = [
	{key:'cool', value: [ 238,354,1107,3559,4126]},
	{key:'cool, useful', value:  [1525,2219,4386,13533,14988]},
	{key:'none', value:  [9813,10023,18766,44494,51628]},
	{key:'funny, cool, useful', value: [4706,6228,10968,24573,21791]},
	{key:'funny, cool', value:  [153,166,252,608,609]},
	{key:'useful', value:  [7571,7288,9037,18571,21120]},
	{key:'funny', value:  [1595,1164,1406,2261,2802]},
	{key:'funny, useful', value:  [2983,2193,1678,2215,2325]}
];

var labels = [
	'cool',
	'cool, useful',
	'none',
	'funny, cool, useful',
	'funny, cool',
	'useful',
	'funny',
	'funny, useful'
];


var width = 600,
    height = 560,
    cwidth = 25,
	hole = 60;

var color = d3.scale.category20();

var pie = d3.layout.pie()
    .sort(null);

var arc = d3.svg.arc();

var arc2 = d3.svg.arc()
  .innerRadius(function(d,i){return 10+hole+cwidth*i;})
  .outerRadius(function(d,i){return hole+cwidth*(i+1);})
  .startAngle(0)
  .endAngle(2 * Math.PI);

var svg = d3.select("#chart3").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var gs = svg.selectAll("g").data(dataset).enter().append("g");
var path = gs.selectAll("path")
    .data(function(d) { return pie(d.value); })
  .enter().append("path")
    .attr("fill", function(d, i) { return color(i); })
    .attr("d", function(d, i, j) { return arc.innerRadius(10+hole+cwidth*j).outerRadius(hole+cwidth*(j+1))(d); });
	
// DRAW SLICE LABELS

var circles = svg.selectAll("g").append("path")
  .attr("fill","red")
  .attr("opacity","0")
  .attr("transform", "rotate(90)")
  .attr("id", function(d,i){return "s"+i;})
  .attr("d",arc2);

 var dxs = [120,135,195,190,255,310,350,370];
  svg.selectAll("g").append("text")
	.attr("dx",function(d,i) {return dxs[i];})
	.append("textPath")
	.attr("alignment-baseline", "hanging")
	.attr("fill","white")
	//.attr("startOffset","50%")
	.attr("xlink:href",function(d,i){ return "#s"+i;})
	.text(function(d,i) {return d.key;});
	
// Add legend
var legend = svg.selectAll(".legend")
	.data([1,2,3,4,5])
.enter().append("g")
	.attr("class", "legend")
	.attr("transform", function(d, i) { console.log(i); return "translate(-" + width / 2 +",-" + (height / 2 - i * 20 ) + ")"; });

legend.append("rect")
	.attr("x", width - 18)
	.attr("width", 18)
	.attr("height", 18)
	.style("fill", function(d, i) { return color(i); });

legend.append("text")
	.attr("x", width - 24)
	.attr("y", 9)
	.attr("dy", ".35em")
	.style("text-anchor", "end")
	.text(function(d) { return d; });
	