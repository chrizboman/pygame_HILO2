import game


game = game.Game()

while game.active:
    game.Update()
    game.Draw()
    game.HandleEvents()
