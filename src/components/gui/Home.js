import React, { Component } from 'react'
import styles from "./home.module.css"
import Axios from 'axios';

export default class Home extends Component {

    constructor(props) {
        super(props)

        this.state = {
            name: "",
            color: "#A2C662"
        }
    }

    onNameChange(name) {
        this.setState({ name: name })
    }

    onColorChange(color) {
        this.setState({ color: color })
    }

    submit() {
        // TODO: handle errors
        if (this.state.name) {
            const data = new FormData()
            data.append("name", this.state.name)
            data.append("color", this.state.color)
            Axios.post(
                "/login",
                data
            ).then(res => {
                if(res.data.success){
                    this.props.onLogin(res.data.id)
                }
            })
        }
    }


    render() {
        return (
            <div id={styles.registerwindow}>
                <h1>Space Game</h1>
                <h2>Enter a name and choose a color</h2>
                <input
                    type="text"
                    placeholder="name"
                    value={this.state.name}
                    onChange={evt => this.onNameChange(evt.target.value)}
                />
                <input
                    type="color"
                    value={this.state.color}
                    onChange={evt => this.onColorChange(evt.target.value)}
                />
                <button onClick={evt => this.submit()}>Start</button>
            </div>
        )
    }
}
