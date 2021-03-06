from game_logic.Vectors import Vector2
from game_logic.Bullets import Bullet
import math
from time import time


class Ship:
    center = Vector2(400, 400)
    W_KEY = 1 << 0
    A_KEY = 1 << 1
    D_KEY = 1 << 2
    SPACE_KEY = 1 << 3
    V_KEY = 1 << 4

    def set_on_bullet(self, shoot_method):
        self.add_bullet = shoot_method

    """
    constructor for ship object
    """

    def __init__(self, ship_id, name, color):
        self.name = name
        self.ship_id = ship_id
        self.color = color
        self.pos = Vector2(250.0, 200.0)
        self.vel = Vector2(1.0, 0.25)
        self.velFactor = 1.0
        self.angle = 0.0

        self.thrust_pressed = False
        self.destroyed = False
        self.super_meter = 4
        self.thrust_meter = 150
        self.ammo_counter = 8
        self.score = 0

        self.destroyed_count = 1
        self.last_pressed = time()
        self.last_updated = time()
        self.last_super = time()
        self.last_requested = time()

        self.key_presses = 0
        self.add_bullet = lambda x: None

    """
    reset func for ship attributes
    """

    def setup(self):
        self.pos = Vector2(250.0, 200.0)
        self.vel = Vector2(1.0, 0.25)
        self.velFactor = 1.0
        self.super_meter = 0
        # self.thrust_meter = 150
        self.ammo_counter = 4
        self.last_pressed = 0

    def remove(self, ships):
        ships.remove(self)

    """
    update the ship's position as well as the keystrokes
    """

    def update(self):
        if self.destroyed:
            self.destroyed_count += 1

        delta = time() - (self.last_updated + 4.0)
        if delta > 0 and self.ammo_counter < 8:
            self.ammo_counter += 1
            self.last_updated = time()

        if self.thrust_meter < 150 and not self.thrust_pressed:
            self.thrust_meter += 0.2

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
        direction = direction.mult(600 / (d * d))

        self.vel = self.vel.add(direction)
        """
        self.vel = self.vel.mult(self.velFactor)
        """

    """"
    rotate the ship
    """

    def rotate(self, left_right):
        self.angle += left_right * 0.02

    """
    moves the ship and checks its position
    """

    def move(self):
        dist_to_center = self.pos.dist(Ship.center)
        self.pos = self.pos.add(self.vel)

        # if the ship falls into the black hole, reset its position
        if dist_to_center < 20.0:
            self.destroyed = True
            self.setup()

        # calculate how slow the ship should move as it moves further to the edge
        if (dist_to_center > 300.0) and (dist_to_center < 390.0):
            self.velFactor -= (360 - self.pos.dist(Ship.center)) / 10.0
        else:
            self.velFactor = 1.0

        # if the ship is out of bounds, place it back to spawn
        if self.pos.dist(Ship.center) > 400.0:
            self.destroyed = True
            self.setup()

    """
    calculate the thrust
    """

    def thrust(self):
        if self.thrust_meter > 0:
            self.thrust_pressed = True
            to_add = Vector2((math.cos(self.angle - math.pi / 2.0) * 0.01),
                             (math.sin(self.angle - math.pi / 2.0) * 0.01))
            self.vel = self.vel.add(to_add)
            self.thrust_meter -= 0.6
        self.thrust_pressed = False

    # normal shoot function
    def shoot(self):
        delta = time() - (self.last_pressed + 0.5)
        if self.ammo_counter > 0 and delta > 0:
            self.ammo_counter -= 1
            self.add_bullet(Bullet(self.pos.x, self.pos.y, self.angle, self))
            self.last_pressed = time()

    # super shoot function, activates after 4 hits
    def super_shoot(self):
        if self.super_meter == 4:
            self.add_bullet(Bullet(self.pos.x, self.pos.y, self.angle - 0.3, self))
            self.add_bullet(Bullet(self.pos.x, self.pos.y, self.angle - 0.1, self))
            self.add_bullet(Bullet(self.pos.x, self.pos.y, self.angle + 0.1, self))
            self.add_bullet(Bullet(self.pos.x, self.pos.y, self.angle + 0.3, self))
        self.super_meter = 0
