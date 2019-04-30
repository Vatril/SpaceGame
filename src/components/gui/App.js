import React, { Component } from 'react'
import Home from './Home';
import GameCanvas from './../game/GameCanvas'

export default class App extends Component {

  constructor(props) {
    super(props)

    this.state = {
      id: ""
    }
  }

  login(id) {
    this.setState({ id: id })
  }

  render() {
    return (
      <div id="wrapper">
        <HomeOrGame
          id={this.state.id}
          onLogin={id => this.login(id)}
        />
      </div>
    )
  }
}

const HomeOrGame = props => {
  if (props.id) {
    return <GameCanvas />
  } else {
    return <Home onLogin={id => props.onLogin(id)} />
  }
}