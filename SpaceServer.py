from flask import Flask, jsonify, request, session, render_template, redirect
from game_logic.Game import Game
import secrets

app = Flask(__name__)

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
    if ship["w"]:
        print("W pressed")
    if ship["a"]:
        print("A pressed")
    if ship["d"]:
        print("D pressed")
    if ship["space"]:
        print("SPACE pressed")
    if ship["v"]:
        print("V pressed")

    for aShip in game.ships:
        if aShip.id == session['user_id']:
            aShip.update(data)

    return jsonify(ship)


@app.route('/login', methods=["POST"])
def login():
    session.clear()
    session['key_presses'] = 0
    session['user_id'] = game.add(request.form["name"], request.form["color"])
    return redirect("/game")


@app.route("/state")
def state():
    ships, bullets = game.get()

    return jsonify({
        "shots": 3,
        "supermeter": 2.7,
        "thrust": 140,
        "ships":
            [{
                "x": ship.pos.x,
                "y": ship.pos.y,
                "angle": ship.angle,
                "color": ship.color,
                "name": ship.name
            } for ship in ships]
        ,
        "bullets": None
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
