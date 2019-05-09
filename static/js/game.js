let key = 0

const startGame = () => {

    d3
        .select("body")
        .on("keydown", () => {
            key |= 1 << keyToShift(d3.event.keyCode)
            sendUpdate()
        })
        .on("keyup", () => {
            key &= ~(1 << keyToShift(d3.event.keyCode))
            sendUpdate()
        })

    setInterval(() => {
        axios.get("/state").then(res => {
            const groups = d3
                .select("#svg")
                .selectAll("g")
                .data(res.data.ships)


            const g = groups.enter()
                .append("g")


            g
                .append("circle")
                .attr("cx", ship => ship.x)
                .attr("cy", ship => ship.y)
                .attr("fill", ship => ship.color)
                .attr("r", 30)

            g
                .append("text")
                .attr("text-anchor", "middle")
                .attr("x", ship => ship.x)
                .attr("y", ship => ship.y)
                .text(ship => ship.name)

            groups
                .select("circle")
                .transition(
                    d3.transition()
                        .ease(d3.easeLinear)
                        .duration(200)
                )
                .attr("cx", ship => ship.x)
                .attr("cy", ship => ship.y)

            groups
                .select("text")
                .transition(
                    d3.transition()
                        .ease(d3.easeLinear)
                        .duration(200)
                )
                .attr("x", ship => ship.x)
                .attr("y", ship => ship.y)

        })
    }, 200)
}

const keyToShift = key => {
    switch (key) {
        case 'w': return 0
        case 'a': return 1
        case 'd': return 2
        case ' ': return 3
        case 'v': return 4
        default: return 0xFFFFFF
    }
}


const sendUpdate = () => {
    axios.get("/player/" + key)
}