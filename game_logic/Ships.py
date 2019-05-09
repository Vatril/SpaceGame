from game_logic.Vectors import Vector2
import game_logic.Game
import math



class Ship:
    center = Vector2(400, 400)
    W_KEY = 1 << 0
    A_KEY = 1 << 1
    D_KEY = 1 << 2
    SPACE_KEY = 1 << 3
    V_KEY = 1 << 4

    """
    constructor for ship object
    """

    def __init__(self, ship_id, name, color):
        self.name = name
        self.color = color
        self.pos = Vector2(250.0, 200.0)
        self.vel = Vector2(0.5, 0.25)
        self.velFactor = 1.0
        self.angle = 0.0

        self.super_meter = 0
        self.thrust_meter = 150
        self.ammo_counter = 8
        self.ship_id = ship_id
        self.score = 0

        self.key_presses = 0

    """
    reset func for ship attributes
    """

    def setup(self):
        self.pos = Vector2(250.0, 200.0)
        self.vel = Vector2(0.5, 0.25)
        self.velFactor = 1.0
        self.super_meter = 0
        self.thrust_meter = 150
        self.ammo_counter = 4
        self.score = 0

    """
    update the ship's position as well as the keystrokes
    """

    def update(self):
        if self.thrust_meter < 150:
            self.thrust_meter += 1

        # update the keystrokes
        if self.key_presses & Ship.W_KEY:
            self.thrust()
        if self.key_presses & Ship.A_KEY:
            self.rotate(-1)
        if self.key_presses & Ship.D_KEY:
            self.rotate(1)
        if self.key_presses & Ship.SPACE_KEY:
            self.shoot()
        if self.key_presses & Ship.V_KEY:
            self.super_shoot()

        # calculate the gravity
        direction = Vector2(800 / 2 - self.pos.x, 800 / 2 - self.pos.y)
        direction = direction.normalize()
        d = self.pos.dist(Ship.center)
        direction = direction.mult(60 / (d * d))

        self.vel = self.vel.add(direction)

    """"
    rotate the ship
    """

    def rotate(self, left_right):
        self.angle += left_right * 0.03

    """
    moves the ship and checks its position
    """

    def move(self):
        dist_to_center = self.pos.dist(Ship.center)
        self.pos = self.pos.add(self.vel)

        # if the ship falls into the black hole, reset its position
        if dist_to_center < 20:
            self.setup()

        # calculate how slow the ship should move as it moves further to the edge
        if (dist_to_center > 300) and (dist_to_center < 390):
            self.velFactor -= (360 - self.pos.dist(Ship.center)) / 10.0

        # if the ship is out of bounds, place it back to spawn
        if dist_to_center > 600:
            self.setup()

    """
    calculate the thrust
    """

    def thrust(self):
        if self.thrust_meter > 0:
            to_add = Vector2((math.cos(self.angle - math.pi / 2.0) * 0.01),
                             (math.sin(self.angle - math.pi / 2.0) * 0.01))
            self.vel = self.vel.add(to_add)
            self.thrust_meter -= 0.2

    # normal shoot function
    def shoot(self):
        if self.ammo_counter:
            Game.bullets.add(Bullet(self.x, self.y, self.angle, self.ship_id))

    # super shoot function, activates after 4 hits
    def super_shoot(self):
        if self.super_meter == 4:
            pass
