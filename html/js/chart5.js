data= [
	{word:'habits', funny:0, cool:1, useful:0},
	{word:'brightly', funny:0, cool:1, useful:0},
	{word:'syrupy', funny:0, cool:1, useful:0},
	{word:'transplants', funny:0, cool:1, useful:0},
	{word:'beast', funny:0, cool:1, useful:0},
	{word:'ahhhhh', funny:0, cool:1, useful:0},
	{word:'airplanes', funny:0, cool:1, useful:0},

	{word:'giggle', funny:1, cool:0, useful:0},
	{word:'cleavage', funny:1, cool:0, useful:0},
	{word:'dunk', funny:1, cool:0, useful:0},
	{word:'asshole', funny:1, cool:0, useful:0},
	{word:'dancefloor', funny:1, cool:0, useful:0},
	{word:'ungodly', funny:1, cool:0, useful:0},
	{word:'souls', funny:1, cool:0, useful:0},
	{word:'effing', funny:1, cool:0, useful:0},

	{word:'freaked', funny:0, cool:0, useful:1},
	{word:'artisan', funny:0, cool:0, useful:1},
	{word:'composed', funny:0, cool:0, useful:1},
	{word:'successful', funny:0, cool:0, useful:1},
	{word:'exhausted', funny:0, cool:0, useful:1},
	{word:'classical', funny:0, cool:0, useful:1},
	{word:'helpful', funny:0, cool:0, useful:1},
	{word:'shirtless', funny:0, cool:0, useful:1},
	{word:'shameful', funny:0, cool:0, useful:1},

	{word:'gawd', funny:1, cool:0, useful:1},
	{word:'gulp', funny:1, cool:0, useful:1},
	{word:'asshole', funny:1, cool:0, useful:1},

	{word:'orgasm', funny:1, cool:1, useful:0},
	{word:'performer', funny:1, cool:1, useful:0},
	{word:'participated', funny:1, cool:1, useful:0},

	{word:'meager', funny:0, cool:1, useful:1},
	{word:'beast', funny:0, cool:1, useful:1},
	{word:'dreading', funny:0, cool:1, useful:1},

	{word:'eardrums', funny:1, cool:1, useful:1},
	{word:'striving', funny:1, cool:1, useful:1},
	{word:'porn', funny:1, cool:1, useful:1}
];

var w = 960,
    h = 600;
	
var foci = {
	"001": {x:540,y:200},
	"010": {x:313,y:196},
	"100": {x:430,y:400},
	"101": {x:480,y:300},
	"011": {x:445,y:215},
	"110": {x:380,y:310},
	"111": {x:440,y:265},
};
 
var svg = d3.select("#chart5").append("svg:svg")
    .attr("width", w)
    .attr("height", h);
 
svg.append("svg:circle")
    .attr("cx", 335)
    .attr("cy", 200)
    .attr("r", 200)
    .style("fill", "yellow")
    .style("fill-opacity", ".5");
 
svg.append("svg:circle")
    .attr("cx", 565)
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
	.attr("x",125)
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
	.charge(-130)
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