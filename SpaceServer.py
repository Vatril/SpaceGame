from flask import Flask, jsonify, request, session, render_template, redirect
from game_logic.Game import Game
from time import time
import secrets
import logging


app = Flask(__name__)


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

W_KEY = 1 << 0
A_KEY = 1 << 1
D_KEY = 1 << 2
SPACE_KEY = 1 << 3
V_KEY = 1 << 4

game = Game()

app.secret_key = secrets.token_bytes(8)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/game')
def gameview():
    if 'user_id' in session:
        return render_template("game.html")
    return redirect("/")


@app.route('/player/<data>')
def latest(data):
    data = int(data)
    ship = {
        "w": True if (data & W_KEY) else False,
        "a": True if (data & A_KEY) else False,
        "d": True if (data & D_KEY) else False,
        "space": True if (data & SPACE_KEY) else False,
        "v": True if (data & V_KEY) else False
    }

    for aShip in game.ships:
        if aShip.ship_id == session['user_id']:
            aShip.key_presses = data

    return jsonify(ship)


@app.route('/login', methods=["POST"])
def login():
    session.clear()
    session['key_presses'] = 0
    session['user_id'] = game.add(request.form["name"], request.form["color"])
    print("client \"" + session['user_id'] + "\" connected with name \"" + request.form["name"] + "\"")
    return redirect("/game")


@app.route("/state")
def state():
    ships, bullets = game.get()

    this_ship = None

    if "user_id" not in session:
        return jsonify({"error": "no ship"})

    for aShip in ships:
        if aShip.ship_id == session['user_id']:
            this_ship = aShip
            break

    if this_ship is None:
        return jsonify({"error": "no ship"})

    this_ship.last_requested = time()

    return jsonify({
        "gui":
            {
                "shots": this_ship.ammo_counter,
                "supermeter": this_ship.super_meter,
                "thrust": this_ship.thrust_meter,
            },
        "ships":
            [{
                "x": ship.pos.x,
                "y": ship.pos.y,
                "angle": ship.angle,
                "color": ship.color,
                "name": ship.name
            } for ship in ships]
        ,
        "bullets":
            [{
                "x": bullet.pos.x,
                "y": bullet.pos.y,
                "id": bullet.bullet_id
            } for bullet in bullets]
    })


@app.route('/scoreboard')
def score_state():
    ships, _ = game.get()
    ships.sort(key=lambda s: s.score, reverse=True)
    return jsonify(
        [{
            "name": ship.name,
            "color": ship.color,
            "score": ship.score
        }for ship in ships]
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
