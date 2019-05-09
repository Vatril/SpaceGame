from game_logic.Vectors import Vector2
import math


class Bullet:

    def __init__(self, x, y, angle, id):
        self.pos = Vector2(x, y)
        self.vel = Vector2(math.cos(angle - math.pi/2) * 6,
                           math.sin(angle - math.pi/2) * 6)
        self.id = id

    # remove the bullet from the array
    def remove(self, bullets):
        bullets.remove(self)

    # collision method
    def check_hit(self, ships, bullets):
        # check if we hit a ship and if the ship is not ours
        for aShip in ships:
            if (self.pos.dist(aShip.pos) < 20) and (self.id != aShip.id):
                self.remove(bullets)

                # look for the ship that shot the bullet
                for bShip in ships:
                    if self.id == bShip.id:
                        bShip.score += 1

                if aShip.superMeter < 4:
                    aShip.superMeter += 1

        # check if we hit a bullet and if it is not ours
        for aBullet in bullets:
            if (self.pos.dist(aBullet.pos) < 20) and (self.id != aBullet.id):
                aBullet.remove(bullets)
                self.remove(bullets)

    def move(self):
        self.pos = self.pos.add(self.vel)