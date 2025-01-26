import pyray as pr


class ZVOmbie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.destroyed = False
        self.textures = [pr.load_texture(f"Assets/game/enemy/Sprite-000{i}.png") for i in range(1, 5)]
        self.rect = pr.Rectangle(self.x, self.y, 29, 39)
        self.frame = 0
        self.i = 0

    def Update(self):
        if not self.destroyed:
            self.x -= 1  # Ворог рухається ліворуч
            self.rect = pr.Rectangle(self.x, self.y, 29, 39)

            self.frame += 1
            self.i = (self.frame // 10) % len(self.textures)

    def Draw(self):
        if not self.destroyed:
            current_texture = self.textures[self.i]
            pr.draw_texture_pro(
                current_texture,
                pr.Rectangle(0, 0, current_texture.width, current_texture.height),
                pr.Rectangle(self.x, self.y, 29, 39),
                pr.Vector2(0, 0),
                0,
                pr.WHITE
            )


