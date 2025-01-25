import pyray as pr

class ZVOmbie:
    def __init__(self):
        self.x = 400
        self.y = 500
        self.i = 0
        self.frame = 0
        self.textures = [pr.load_texture(f"Assets/game/enemy/Sprite-000{i}.png") for i in range(1, 5)]

    def Update(self):
        self.x -= 1

        self.frame += 1
        self.i = (self.frame // 10) % len(self.textures)

    def Draw(self):
        current_texture = self.textures[self.i]
        pr.draw_texture_pro(
            current_texture,
            pr.Rectangle(0, 0, current_texture.width, current_texture.height),
            pr.Rectangle(self.x, self.y, 27, 39),
            pr.Vector2(0, 0),
            0,  
            pr.WHITE
        )

    def NeNarkoman(self):
        pass