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

