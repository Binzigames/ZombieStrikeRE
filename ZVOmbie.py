import pyray as pr
import SoundManager as SM
pHP = 3
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

        


     

    def Update(self):
        global pHP
        if not self.destroyed:
            self.rect = pr.Rectangle(self.x, self.y, 29, 39)
            if not self.stop == True:
                self.x -= 1  # Ворог рухається ліворуч

            self.frame += 1
            self.i = (self.frame // 10) % len(self.textures)


            if self.x == 0:
                pHP -= 1
                print(pHP)


            

                     

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





