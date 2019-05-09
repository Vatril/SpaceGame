let key = 0

const startGame = () => {

    d3
        .select("body")
        .on("keydown", () => {
            key |= 1 << keyToShift(d3.event.key)
            sendUpdate()
        })
        .on("keyup", () => {
            key &= ~(1 << keyToShift(d3.event.key))
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
                .attr("transform", ship => `translate(${ship.x}, ${ship.y})`)

            g
                .append("path")
                .attr("fill", ship => ship.color)
                .attr("d", "M 5 0 L 10 10 L 0 10")

            g
                .append("text")
                .attr("text-anchor", "middle")
                .text(ship => ship.name)

            groups
                .transition(
                    d3.transition()
                        .ease(d3.easeLinear)
                        .duration(200)
                )
                .attr("transform", ship => `translate(${ship.x}, ${ship.y})`)

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