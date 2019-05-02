from game_logic.Ships import Ship
from uuid import uuid4


class Game:
    ships = []
    bullets = []

    @staticmethod
    def update():
        for aShip in Game.ships:
            aShip.setup()
            aShip.update()
            aShip.move()

        for aBullet in Game.bullets:
            aBullet.setup()
            aBullet.update()
            aBullet.move()

    def add(self, name, color):
       uuid = str(uuid4())
       Game.ships.append(Ship(uuid, name, color))
       return uuid

    def get(self):
        self.update()
        return Game.ships, Game.bullets
