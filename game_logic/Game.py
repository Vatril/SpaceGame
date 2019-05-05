from Ships import Ship
from Bullets import Bullet
from uuid import uuid4
from time import time


class Game:
    ships = []
    bullets = []

    last_update = 0

    @staticmethod
    def update():
        for aShip in Game.ships:
            aShip.update()
            aShip.move()

        for aBullet in Game.bullets:
            aBullet.update()
            aBullet.move()

    def add(self, name, color):
       uuid = str(uuid4())
       Game.ships.append(Ship(uuid, name, color))
       return uuid

    def get(self):
        if Game.last_update == 0:
            Game.last_update = time()
        delta = (time() + 100) - Game.last_update
        if delta > 0:
            for i in range(0, int(delta/100)):
                self.update()
            Game.last_update = time()
        return Game.ships, Game.bullets
