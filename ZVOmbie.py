import pyray as pr

class ZVOmbie:
    def __init__(self):
        self.x = 400
        self.y = 500
        self.i = 0
        self.frame = 0
        self.texture = pr.load_texture(f"Assets/game/enemy/enemyt.png")

    def Update(self):
        self.x -= 1

    def Draw(self):
        pr.draw_texture_pro(self.texture, pr.Rectangle(0, 0, 29, 39), pr.Rectangle(self.x, self.y, 27, 39), pr.Vector2(0, 0), 0, pr.WHITE)

    def NeNarkoman(self):
        pass
    
        