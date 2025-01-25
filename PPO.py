import pyray as pr
import ZVOmbie as vagina
class PPO:
    def __init__(self):
        self.x = 145
        self.y = 470
        self.desroy = False
        self.rectangle = 0
        self.vag = vagina.ZVOmbie()

    def Draw(self):
        if self.desroy == False:
            pr.draw_circle_v(pr.Vector2(self.x, self.y), 3, pr.YELLOW)

    def Update(self, glist):
        self.rectangle = pr.Rectangle(self.x, self.y, 3, 3)
        self.x += 1
        glist = self.vag.rect
        for i in range(len(glist)):
            if pr.check_collision_recs(self.rectangle, glist.rect):
                self.desroy = True