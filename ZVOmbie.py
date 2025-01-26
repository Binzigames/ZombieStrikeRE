import pyray as pr
import SoundManager as SM

class ZVOmbie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.destroyed = False
        self.textures = [pr.load_texture(f"Assets/game/enemy/Sprite-000{i}.png") for i in range(1, 5)]
        self.rect = pr.Rectangle(self.x, self.y, 29, 39)
        self.frame = 0
        self.i = 0
        self.timer = 150
        self.stop = False
     

    def Update(self, suka, baseHP):
        if not self.destroyed:
            self.suka = suka
            self.rect = pr.Rectangle(self.x, self.y, 29, 39)
            if not self.stop == True:
                self.x -= 1  # Ворог рухається ліворуч

            self.frame += 1
            self.i = (self.frame // 10) % len(self.textures)

            if pr.check_collision_recs(self.rect, suka):
                if not self.destroyed:
                    self.stop = True
                    self.timer -= 1
                    if self.timer <= 0:
                        baseHP -= 3
                        print("suuka")
                        self.timer = 150

                     

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

            pr.draw_text(f"att:{self.timer}", self.x, self.y + 100, 10, pr.WHITE)


