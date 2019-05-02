from game_logic.Ships import Ship
from game_logic.Bullets import Bullet
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
        delta = (time() + 100) - Game.last_update
        if delta > 0:
            for i in range(0, i):
                self.update()
            Game.last_update = time()
        return Game.ships, Game.bullets
