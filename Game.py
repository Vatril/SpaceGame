from Ships import Ship
from Bullets import Bullet


class Game:
    ships = []
    bullets = []

    def update(self):
        for aShip in Game.ships:
            aShip.setup()
            aShip.update()
            aShip.move()

