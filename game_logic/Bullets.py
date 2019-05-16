from game_logic.Vectors import Vector2
import math
from uuid import uuid4
from time import time


class Bullet:
    center = Vector2(400, 400)

    def __init__(self, x, y, angle, s_obj):
        self.parent_ship = s_obj
        self.created = time()
        self.pos = Vector2(x, y)
        self.vel = Vector2(math.cos(angle - math.pi / 2) * 2.0,
                           math.sin(angle - math.pi / 2) * 2.0)
        self.bullet_id = str(uuid4())

    """
    remove the bullet from the array
    """

    def remove(self, bullets):
        bullets.remove(self)

    """
    collision method
    """

    def check_hit(self, ships, bullets):
        # check if we hit a ship and if the ship is not ours
        for aShip in ships:
            if (self.pos.dist(aShip.pos) < 20) and (self.parent_ship != aShip):
                print("hit")
                self.remove(bullets)

                self.parent_ship.score += 1

                if aShip.super_meter < 4:
                    aShip.super_meter += 1

                aShip.destroyed = True
                aShip.time_destroyed = time()

        """
        # check if we hit a bullet and if it is not ours
        for aBullet in bullets:
            if (self.pos.dist(aBullet.pos) < 20) and (self.parent_ship != aBullet.parent_ship):
                self.remove(bullets)
                self.remove(bullets)
        """

    """
    calculates the velocity and position
    """

    def update(self, ships, bullets):
        delta = time() - (self.created + 4)
        if delta > 0:
            self.remove(bullets)
            return
        # calculate the gravity
        direction = Vector2(Bullet.center.x - self.pos.x, Bullet.center.y - self.pos.y)
        direction = direction.normalize()
        d = self.pos.dist(Bullet.center)
        direction = direction.mult(1200 / (d * d))

        self.vel = self.vel.add(direction)

        if self.pos.dist(Bullet.center) > 400.0:
            self.remove(bullets)

        self.check_hit(ships, bullets)

    """
    update func for bullets
    """

    def move(self):
        self.pos = self.pos.add(self.vel)
