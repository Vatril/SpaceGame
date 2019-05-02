from flask import Flask, jsonify, request
from Bullets import Bullet
from Ships import Ship
from Game import Game

app = Flask(__name__)

W_KEY = 1 << 0
A_KEY = 1 << 1
D_KEY = 1 << 2
SPACE_KEY = 1 << 3
V_KEY = 1 << 4

game = Game()


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

    return jsonify(ship)


@app.route('/login', methods=["POST"])
def login():
    return jsonify({
        "success": True,
        "id": game.add(request.form["name"], request.form["color"])
    })


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
        "bullets" : None
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3001)
