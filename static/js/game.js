const startGame = () => {

    setInterval(() => {
        axios.get("/state").then(res => {
            const svg = d3
                .select("#svg")
                .selectAll("g")
                .data(res.data.ships)


            svg.enter()
                .append("g")
                .append("circle")
                .attr("cx", ship => ship.x)
                .attr("cy", ship => ship.y)
                .attr("fill", ship => ship.color)
                .attr("r", 30)

            svg
                .select("circle")
                .transition(
                    d3.transition()
                .duration(500)
                )
                .attr("cx", ship => ship.x)
                .attr("cy", ship => ship.y)

        })
    }, 500)
}