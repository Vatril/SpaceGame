import React, { Component } from 'react'
import Axios from 'axios';

export default class GameCanvas extends Component {

    constructor(props) {
        super(props)

        this.key = 0

        this.state = {

        }
    }


    componentDidMount() {
        this.context2D.fillStyle = 'grey'
        this.context2D.fillRect(0, 0, 800, 800)
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

    sendUpdate(){
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
