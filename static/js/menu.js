const setup = () => {
    
    d3
    .select("#color")
    .attr("value", d3.color(d3.interpolateRainbow(Math.random())).hex())
    // TODO Fix formatting when below 0x10
}