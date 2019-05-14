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
            aBullet.update(Game.bullets)
            aBullet.move()

    @staticmethod
    def add(name, color):
        uuid = str(uuid4())
        s = Ship(uuid, name, color)
        print(s.pos.x, s.pos.y)
        s.set_on_bullet(lambda bullet: Game.bullets.append(bullet))
        Game.ships.append(s)
        return uuid

    def get(self):
        if Game.last_update == 0:
            Game.last_update = time()
        delta = (time() + 100) - Game.last_update
        if delta > 0:
            for i in range(0, int(delta)):
                self.update()
            Game.last_update = time()
        return Game.ships, Game.bullets
