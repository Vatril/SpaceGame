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
                .select("#ships")
                .selectAll("g")
                .data(res.data.ships)

            d3
                .select("#thrust")
                .datum(res.data.gui.thrust)
                .transition(d3.transition()
                    .ease(d3.easeLinear)
                    .duration(100))
                .attr("width", thrust => thrust)

            const g = groups.enter()
                .append("g")
                .attr("transform", ship => `translate(${ship.x}, ${ship.y})
                 rotate(${(ship.angle / (2 * Math.PI)) * 360})`)

            g
                .append("path")
                .attr("fill", ship => ship.color)
                .attr("d", "M 20 0 L 40 40 L 0 40")

            g
                .append("text")
                .attr("text-anchor", "middle")
                .text(ship => ship.name)

            groups
                .transition(d3.transition()
                    .ease(d3.easeLinear)
                    .duration(100))
                .attr("transform", ship => `translate(${ship.x}, ${ship.y})
                 rotate(${(ship.angle / (2 * Math.PI)) * 360})`)

        })
    }, 100)
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