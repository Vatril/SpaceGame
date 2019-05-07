import React, { Component } from 'react'
import Axios from 'axios';

export default class GameCanvas extends Component {

    DRAWTICKS = 10
    NETWORKTICKS = 500

    constructor(props) {
        super(props)

        this.key = 0
        this.drawInterval = 0
        this.getInterval = 0

        this.aniprogress = 0

        this.logicstate = {
            ships: [],
            supermeter: 0,
            thrust: 0,
            shots: 0
        }

        this.lastlogicstate = {
            ships: [],
            supermeter: 0,
            thrust: 0,
            shots: 0
        }
    }


    componentDidMount() {
        this.context2D.fillStyle = 'black'
        this.context2D.fillRect(0, 0, 800, 800)
        this.drawShips()
        this.drawInterval = setInterval(() => {
            this.drawShips()
        }, this.DRAWTICKS)
        this.getInterval = setInterval(() => {
            this.updateState()
        }, this.NETWORKTICKS)
    }

    componentWillUnmount() {
        clearInterval(this.drawInterval)
        clearInterval(this.getInterval)
    }

    updateState() {
        Axios.get("/state").then(res => {
            this.lastlogicstate = this.logicstate
            this.logicstate = res.data
            this.aniprogress = 0
        })
    }

    drawShips() {
        this.context2D.fillStyle = 'black'
        this.context2D.fillRect(0, 0, 800, 800)
        this.context2D.font = "20pt sans"
        for (const ship of this.logicstate.ships) {
            let oldship = this.lastlogicstate.ships.find(sh => sh.id === ship.id)
            if (!oldship) {
                oldship = {
                    x: 0,
                    y: 0,
                    angle: 0
                }//TODO: make this better
            }
            this.context2D.translate(ship.x, ship.y)
            this.context2D.rotate(-ship.angle)
            this.context2D.translate(-ship.x, -ship.y)
            this.context2D.fillStyle = ship.color
            this.context2D.beginPath()
            this.context2D.moveTo(oldship.x, oldship.y - 20)
            this.context2D.lineTo(oldship.x - 20, oldship.y + 20)
            this.context2D.lineTo(oldship.x + 20, oldship.y + 20)
            this.context2D.fill()
            this.context2D.fillStyle = 'white'
            this.context2D.strokeStyle = 'black'
            this.context2D.fillText(ship.name, ship.x - 20, ship.y + 20)
            this.context2D.strokeText(ship.name, ship.x - 20, ship.y + 20)
            this.context2D.translate(ship.x, ship.y)
            this.context2D.rotate(ship.angle)
            this.context2D.translate(-ship.x, -ship.y)
        }

        this.context2D.fillStyle = 'grey'
        this.context2D.arc(670, 25, 20, 0, 2 * Math.PI)


        for (let i = 0; i < 5; i++) {
            this.context2D.beginPath()
            this.context2D.arc((20 * i) + 700, 10, 5, 0, 2 * Math.PI)
            this.context2D.fill()
        }

        this.context2D.beginPath()
        this.context2D.moveTo(670, 25)
        this.context2D.lineTo(695, 25)
        this.context2D.arc(670, 25, 20, 0, 2 * Math.PI)
        this.context2D.fill()

        this.context2D.fillRect(695, 20, 90, 20)

        this.context2D.fillStyle = 'white'


        for (let i = 0; i < this.logicstate.shots; i++) {
            this.context2D.beginPath()
            this.context2D.arc((20 * i) + 700, 10, 5, 0, 2 * Math.PI)
            this.context2D.fill()
        }

        this.context2D.beginPath()
        this.context2D.moveTo(670, 25)
        this.context2D.lineTo(695, 25)
        this.context2D.arc(670, 25, 20, 0, 2 * Math.PI * (this.logicstate.supermeter / 4))
        this.context2D.fill()

        this.context2D.fillRect(695, 20, 90 * (this.logicstate.thrust / 150), 20)

        this.aniprogress += this.DRAWTICKS / this.NETWORKTICKS

    }

    keyToShift(key) {
        switch (key) {
            case 'w': return 0
            case 'a': return 1
            case 'd': return 2
            case ' ': return 3
            case 'v': return 4
            default: return 0xFFFFFF
        }
    }

    onKeyDown(key) {
        this.key |= 1 << this.keyToShift(key)
        this.sendUpdate();
    }

    onKeyUp(key) {
        this.key &= ~(1 << this.keyToShift(key))
        this.sendUpdate();
    }

    sendUpdate() {
        Axios.get("/player/" + this.key)
    }

    render() {
        return <canvas
            onKeyDown={evt => this.onKeyDown(evt.key)}
            onKeyUp={evt => this.onKeyUp(evt.key)}
            width="800"
            height="800"
            tabIndex="0"
            ref={(c) => this.context2D = c.getContext('2d')}
        />
    }
}
