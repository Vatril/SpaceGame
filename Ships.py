from Vectors import Vector2
import math


class Ship:
    center = Vector2(400, 400)

    def __init__(self, id):
        self.pos = Vector2(0.0, 0.0)
        self.vel = Vector2(2.0, 0.5)
        self.velFactor = 1.0
        self.angle = 0.0

        self.super_meter = 0
        self.thrust_meter = 150
        self.ammo_counter = 8
        self.id = id
        self.score = 0

    def setup(self):
        self.pos = Vector2(0.0, 0.0)
        self.vel = Vector2(2.0, 0.5)
        self.velFactor = 1.0
        self.super_meter = 0
        self.thrust_meter = 150
        self.ammo_counter = 4
        self.score = 0

    def update(self):
        direction = Vector2(800 / 2 - self.pos.x, 800 / 2 - self.pos.y)
        direction = direction.normalize()
        d = self.pos.dist(Ship.center)
        direction = direction.mult(1000 / (d * d))

        self.vel = self.vel.add(direction)

    def move(self):
        dist_to_center = self.pos.dist(Ship.center)
        self.pos = self.pos.add(self.vel)

        if dist_to_center < 20:
            self.setup()

        if (dist_to_center > 300) and (dist_to_center < 390):
            self.velFactor -= (360 - self.pos.dist(Ship.center)) / 10.0

            if dist_to_center > 390:
                self.setup()

    def thrust(self):
        if self.thrust_meter > 0:
            to_add = Vector2((math.cos(self.angle - math.pi/2.0) * 0.05),
                            (math.sin(self.angle - math.pi/2.0) * 0.05))
            self.vel.add(to_add)
            self.thrust_meter -= 2

    def shoot(self):
        if self.ammo_counter:
            pass
