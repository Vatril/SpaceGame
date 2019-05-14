const setup = () => {
    let r = 0
    let g = 0
    let b = 0

    while(r+g+b<200){
        r = Math.floor(Math.random() * 255)
        g = Math.floor(Math.random() * 255)
        b = Math.floor(Math.random() * 255)
    }

    d3
    .select("#color")
    .attr("value", `#${r.toString(16)}${g.toString(16)}${b.toString(16)}`)
    // TODO Fix formating when below 0x10
}