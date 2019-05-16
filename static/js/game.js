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
        axios.get("/scoreboard").then(res => {
            const lis = d3
                .select("#scoreboard")
                .selectAll("li")
                .data(res.data)

            lis
                .enter()
                .append("li")
                .style("color", player => player.color)
                .text(player => `${player.score} | ${player.name}`)

            lis
                .text(player => `${player.score} | ${player.name}`)
                .style("color", player => player.color)

            lis.exit().remove()
        })
    }, 1000)

    setInterval(() => {
        axios.get("/state").then(res => {
            const groups = d3
                .select("#ships")
                .selectAll("g")
                .data(res.data.ships)

            const b_groups = d3
                .select("#bullets")
                .selectAll("circle")
                .data(res.data.bullets, b => b.id)

            b_groups
                .enter()
                .append("circle")
                .attr("id", b => `bullet_${b.id}`)
                .attr("cx", s => s.x)
                .attr("cy", s => s.y)
                .attr("r", "5")

            b_groups
                .transition(d3.transition()
                    .ease(d3.easeLinear)
                    .duration(100))
                .attr("cx", s => s.x)
                .attr("cy", s => s.y)

            b_groups
                .exit()
                .remove()

            d3
                .select("#thrust")
                .datum(res.data.gui.thrust)
                .transition(d3.transition()
                    .ease(d3.easeLinear)
                    .duration(100))
                .attr("width", thrust => thrust)

            d3
                .select("#supermeter")
                .datum(res.data.gui.supermeter)
                .attr("r", d => d * 6)

            d3
                .select("#shots")
                .datum(res.data.gui.shots)
                .each(shots => {

                    d3
                        .select("#shots")
                        .selectAll("circle")
                        .remove()
                    for (let i = 0; i < shots; i++) {
                        d3
                            .select("#shots")
                            .append("circle")
                            .attr("r", "6")
                            .attr("cy", 15 + Math.floor(i / 4) * 20)
                            .attr("cx", i * 40 + 710 + (Math.floor(i / 4) * -160))
                    }
                })

            const g = groups.enter()
                .append("g")
                .attr("transform", ship => `translate(${ship.x}, ${ship.y})
                 rotate(${(ship.angle / (2 * Math.PI)) * 360})`)

            g
                .append("path")
                .attr("stroke", "none")
                .attr("fill", ship => ship.color)
                .attr("d", "M 20 -20 L 40 20 L 0 20")

            g
                .append("text")
                .attr("text-anchor", "middle")
                .attr("transform", "translate(20, -30)")
                .text(ship => ship.name)

            const tgroup = groups
                .transition(d3.transition()
                    .ease(d3.easeLinear)
                    .duration(100))
                .attr("transform", ship => `translate(${ship.x}, ${ship.y})
                 rotate(${(ship.angle / (2 * Math.PI)) * 360})`)

            tgroup
                .select("path")
                .attr("fill", ship => ship.color)

            tgroup
                .select("text")
                .text(ship => ship.name)



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