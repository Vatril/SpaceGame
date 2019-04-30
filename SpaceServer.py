from flask import Flask, jsonify, request

app = Flask(__name__)

W_KEY = 1 << 0
A_KEY = 1 << 1
D_KEY = 1 << 2
SPACE_KEY = 1 << 3
V_KEY = 1 << 4


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
    print(request.form["name"])
    print(request.form["color"])
    return jsonify({
        "success":True,
        "id":"some_uuid"
    })


@app.route("/state")
def state():
    return jsonify({
        "shots": 3,
        "supermeter": 2.7,
        "thrust": 140,
        "ships": [{
            "name": "abc",
            "color": "#FF00FF",
            "x": 100,
            "y": 50,
            "angle": 0
        },
        {
            "name": "huhu",
            "color": "#00FF00",
            "x": 100,
            "y": 50,
            "angle": 3.1415
        }]


    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3001)
