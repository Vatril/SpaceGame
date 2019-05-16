from game_logic.Ships import Ship
from game_logic.Bullets import Bullet
from uuid import uuid4
from time import time


class Game:
    ships = []
    bullets = []

    last_update = 0

    @staticmethod
    def add(name, color):
        uuid = str(uuid4())
        s = Ship(uuid, name, color)
        s.set_on_bullet(lambda bullet: Game.bullets.append(bullet))
        Game.ships.append(s)
        return uuid

    @staticmethod
    def get():
        if Game.last_update == 0:
            Game.last_update = time()
        delta = (time() + 0.1) - Game.last_update
        if delta > 0:
            for i in range(0, int(delta*100)):
                Game.update()
            Game.last_update = time()
        return Game.ships, Game.bullets

    @staticmethod
    def update():
        for aShip in Game.ships:
            delta = time() - (aShip.last_requested + 3)
            if delta > 0:
                Game.remove(aShip)
            else:
                aShip.update()
                aShip.move()

        for aBullet in Game.bullets:
            aBullet.update(Game.ships, Game.bullets)
            aBullet.move()

    @staticmethod
    def remove(s):
        print("removed")
        Game.ships.remove(s)
