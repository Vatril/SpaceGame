from Ships import Ship
from Bullets import Bullet
from uuid import uuid4


class Game:
    ships = []
    bullets = []

    def update(self):
        for aShip in Game.ships:
            aShip.setup()
            aShip.update()
            aShip.move()

    def add(self, name, color):
       uuid = str(uuid4())
       Game.ships.append(Ship(uuid, name, color))
       return uuid

    def get(self):
        self.update()
        return Game.ships, Game.bullets
