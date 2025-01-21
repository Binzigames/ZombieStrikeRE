import pyray as pr

class Screen:
    def __init__(self):
        self.finishScreen = 0
        self.screenId = -1

    def Update(self):
        ...

    def Draw(self):
        ...

    def Unload(self):
        ...

   
     

class Logo(Screen):
    def __init__(self):
        super().__init__()
        self.screenId = 0
        self.logo = pr.load_texture("Assets/raylib_logo.png")
        self.ppo = 300
        self.rot = 0.0
        self.alpha = 0
        self.font = pr.load_font("Assets/pizda.fnt")

    def Update(self):
        self.ppo -= 1
        if self.ppo <= 0:
            self.finishScreen = 1

        self.rot += 0.5
        self.alpha += 3
        if self.alpha >= 255:
            self.alpha = 255

        if self.rot >= 360:
            self.rot = 0
        
        if pr.is_key_pressed(pr.KeyboardKey.KEY_UP):
            self.finishScreen = 1

    def Draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.GRAY)
        pr.draw_texture_pro(self.logo, pr.Rectangle(0, 0, 256, 256), pr.Rectangle(pr.get_screen_width()/2, pr.get_screen_height()/2, 256, 256), pr.Vector2(256/2, 256/2), self.rot, pr.Color(255, 255, 255, self.alpha))
        
        pr.draw_text(f"{self.ppo}", 10, 10, 10, pr.WHITE)
        pr.draw_text_ex(self.font, "Created with Raylib", pr.Vector2(200+5, 500+5), 50, 1, pr.Color(0, 0, 0, self.alpha))
        pr.draw_text_ex(self.font, "Created with Raylib", pr.Vector2(200, 500), 50, 1, pr.Color(255, 255, 255, self.alpha))
        pr.draw_fps(0, 550)
        pr.end_drawing()

    def Unload(self):
        pr.unload_texture(self.logo)
        pr.unload_font(self.font)



class Logo2(Screen):
    def __init__(self):
        super().__init__()
        self.screenId = 1
        self.texture1 = pr.load_texture("Assets/logo_porko.png")
        self.texture2 = pr.load_texture("Assets/logo_ne.png")
        self.font = pr.load_font("Assets/pizda.fnt")
        self.alpha = 0
        self.count = 300

    def Update(self):
        self.count -= 1
        if self.count <= 0:
            self.finishScreen = 1

        self.alpha += 3
        if self.alpha >= 255:
            self.alpha = 255
        
        if pr.is_key_pressed(pr.KeyboardKey.KEY_UP):
            self.finishScreen = 1

    def Draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_text(f"{self.count}", 10, 10, 10, pr.WHITE)
        pr.draw_texture_pro(self.texture1, pr.Rectangle(0, 0, 440, 430), pr.Rectangle(200, 20, 440-100, 430-100), pr.Vector2(0, 0), 0, pr.Color(255, 255, 255, self.alpha))
        pr.draw_texture_pro(self.texture2, pr.Rectangle(0, 0, 120, 139), pr.Rectangle(350, 400, 120+100, 139+100), pr.Vector2((120+100)/2, (139+100)/2), -15, pr.Color(255, 255, 255, self.alpha))
        pr.draw_text_ex(self.font, "Guy who makes original game", pr.Vector2(150, 20), 25, 0, pr.Color(255, 255, 255, self.alpha))
        pr.draw_text_ex(self.font, "Guy who helps with remake of game", pr.Vector2(150, 270), 25, 0, pr.Color(255, 255, 255, self.alpha))
        pr.end_drawing()

    def Unload(self):
        pr.unload_texture(self.texture1)
        pr.unload_texture(self.texture2)
        pr.unload_font(self.font)

class Menu(Screen):
    def __init__(self):
        super().__init__()
        self.screenId = 2
        self.playButton = 0
        self.exitButton = 0
        self.font = pr.load_font("Assets/pizda.fnt")
        pr.gui_set_style(0, pr.GuiDefaultProperty.TEXT_SIZE, 20)

    def Update(self):
        if self.exitButton == 1:
            self.finishScreen = 1

    def Draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_text("ZombieStrikeRE", 50, 50, 75, pr.WHITE)
        self.playButton = pr.gui_button(pr.Rectangle(50, 300, 200, 50), "Play")
        self.exitButton = pr.gui_button(pr.Rectangle(50, 400, 200, 50), "Exit")
        pr.end_drawing()

    def Unload(self):
        pass