import pyray as pr
import PlaymanityAPI.SDK as sdk
from PIL import Image
from io import BytesIO

class Ad:
    def __init__(self):
        self.url = sdk.get_photoURL()
        self.uimage = Image.open(BytesIO(self.url))
        self.uimage.save("ad.png")
        self.image = pr.load_texture("ad.png")
        self.timer = 200
        self.dell = False
        self.mouserect = pr.Rectangle(0, 100, 200, 100)

    def draw(self):
        pr.draw_texture_pro(self.image, pr.Rectangle(0, 0, self.image.width, self.image.height), pr.Rectangle(0, 100, 200, 100), pr.Vector2(0, 0), 0, pr.WHITE)
        pr.draw_rectangle_rec(self.mouserect, pr.WHITE)

    def update(self):
        self.mouserect = pr.Rectangle(pr.get_mouse_x(), pr.get_mouse_y(), 10, 10)
        self.timer -= 1

        if pr.is_mouse_button_pressed(pr.MouseButton.MOUSE_BUTTON_LEFT) and pr.check_collision_recs(pr.Rectangle(0, 100, self.image.width, self.image.height), self.mouserect):
            pr.open_url("https://tenor.com/uk/view/fnaf-meme-cock-balls-boobs-ass-cock-ass-gif-25082723")

        if self.timer < 0:
            self.dell = True