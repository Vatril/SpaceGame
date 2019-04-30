import React, { Component } from 'react'
import styles from "./home.module.css"

export default class Home extends Component {
    render() {
        return (
            <div id={styles.registerwindow}>
                <h1>Space Game</h1>
                <h2>Enter a name and choose a color</h2>
                <input
                    type="text"
                    placeholder="name"
                />
                <input
                    type="color"
                />
                <button>Start</button>
            </div>
        )
    }
}
