data= [
	{word:'hi', funny:0, cool:1, useful:0},
	{word:'bye', funny:1, cool:0, useful:0},
	{word:'yo', funny:1, cool:0, useful:0},
	{word:'dude', funny:0, cool:0, useful:1},
	{word:'dude', funny:0, cool:0, useful:1},
	{word:'bob', funny:0, cool:1, useful:0},
	{word:'sugfdgfdsgfp?', funny:1, cool:0, useful:0},
	{word:'middle', funny:1, cool:1, useful:1},
	{word:'hi', funny:1, cool:1, useful:0},
	{word:'bye', funny:1, cool:0, useful:1},
	{word:'bye', funny:1, cool:0, useful:1},
	{word:'yo', funny:1, cool:1, useful:0},
	{word:'dude', funny:0, cool:1, useful:1},
	{word:'dude', funny:0, cool:1, useful:1},
	{word:'bob', funny:1, cool:1, useful:1},
	{word:'middle', funny:1, cool:1, useful:1},
];

var w = 960,
    h = 600;
	
var foci = {
	"001": {x:633,y:146},
	"010": {x:263,y:156},
	"100": {x:455,y:480},
	"101": {x:545,y:331},
	"011": {x:445,y:145},
	"110": {x:330,y:337},
	"111": {x:450,y:275},
};
 
var svg = d3.select("#chart5").append("svg:svg")
    .attr("width", w)
    .attr("height", h);
 
svg.append("svg:circle")
    .attr("cx", 350)
    .attr("cy", 200)
    .attr("r", 200)
    .style("fill", "yellow")
    .style("fill-opacity", ".5");
 
svg.append("svg:circle")
    .attr("cx", 550)
    .attr("cy", 200)
    .attr("r", 200)
    .style("fill", "steelblue")
    .style("fill-opacity", ".5");
 
svg.append("svg:circle")
    .attr("cx", 450)
    .attr("cy", 400)
    .attr("r", 200)
    .style("fill", "green")
    .style("fill-opacity", ".5");
	
svg.append("text")
	.style("font-weight", "bold")
	.style("font-size", "20pt")
	.attr("x",705)
	.attr("y",40)
	.text("Useful");

svg.append("text")
	.style("font-weight", "bold")
	.style("font-size", "20pt")
	.attr("x",155)
	.attr("y",40)
	.text("Cool");	

svg.append("text")
	.style("font-weight", "bold")
	.style("font-size", "20pt")
	.attr("x",600)
	.attr("y",575)
	.text("Funny");
	
var force = d3.layout.force()
    .nodes(data)
	.gravity(0)
	.charge(-100)
	.links([])
    .size([width, height])
    .on("tick", tick)
    .start();

var node = svg.selectAll(".node")
    .data(data)
  .enter().append("text")
    .attr("class", "node")
    .attr("x", function(d) { return d.x; })
    .attr("y", function(d) { return d.y; })
	.text(function(d) {return d.word})
	.style("fill","black")
    .call(force.drag);



	
function tick(e) {
  // Push different nodes in different directions for clustering.
  var k = 0.1 * e.alpha;
  data.forEach(function(o, i) {
	o.y += (foci[o.funny+''+o.cool+''+o.useful].y - o.y) * k;
    o.x += (foci[o.funny+''+o.cool+''+o.useful].x - o.x) * k;
  });

  node.attr("x", function(d) { return d.x; })
      .attr("y", function(d) { return d.y; });
}