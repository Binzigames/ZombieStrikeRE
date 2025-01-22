import pyray as pr
import math

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
        self.settingsButton = 0
        self.playButton = 0
        self.exitButton = 0
        self.fullscreenToggle = False
        self.count = 0
        self.settingstoggle = False
        self.font = pr.load_font("Assets/pizda.fnt")
        self.textureLogo = pr.load_texture("Assets/gay_logo.png")
        self.cloud_image = pr.load_image("Assets/cumulus-cloud.png")
        pr.image_color_grayscale(self.cloud_image)
        pr.image_blur_gaussian(self.cloud_image, 2)
        pr.image_color_brightness(self.cloud_image, -200)
        self.cloudTexture = pr.load_texture_from_image(self.cloud_image)
        pr.gui_set_font(self.font)
        pr.gui_set_style(0, pr.GuiDefaultProperty.TEXT_SIZE, 20)

    def Update(self):
        self.count += 1
        if self.exitButton == 1:
            self.finishScreen = 1

        if self.playButton == 1:
            self.finishScreen = 2

        if self.settingsButton == 1:
            print("suka")
            self.settingstoggle = True

    def Draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_texture_ex(self.cloudTexture, pr.Vector2(-10 + 10 * math.cos(self.count/120), -50 + 5 * math.sin(self.count/120)), 1 * math.cos(self.count/120), 1, pr.WHITE)
        pr.draw_texture_pro(self.textureLogo, pr.Rectangle(0, 0, 820, 88), pr.Rectangle(800/2, 100 + 10 * math.cos(self.count/120), 620, 88), pr.Vector2(620/2, 88/2), 5 * math.sin(self.count/120), pr.WHITE)
        self.playButton = pr.gui_button(pr.Rectangle(800/2-100, 400, 200, 30), "Play")
        self.settingsButton = pr.gui_button(pr.Rectangle(800/2-100, 430, 200, 30), f"Settings: {self.settingstoggle}")
        self.exitButton = pr.gui_button(pr.Rectangle(800/2-100, 460, 200, 30), "Exit")

        if self.settingstoggle == True:
            result = pr.gui_window_box(pr.Rectangle(100, 100, 600, 300), "Settings")
            if result == 1:
                self.settingstoggle = False
            # Цей кал я хз як робити
            # toggle = pr.gui_check_box(pr.Rectangle(120, 135, 15, 15), f"Music {self.fullscreenToggle}", pr.ffi.new("_Bool *", self.fullscreenToggle))

        pr.end_drawing()

    def Unload(self):
        pr.unload_font(self.font)



class Game(Screen):
    def __init__(self):
        super().__init__()
        self.screenId = 3
        self.BGTexture = pr.load_texture("Assets/game/BG.png")
        self.font = pr.load_font("Assets/pizda.fnt")
        self.natural = 1
        self.gay = False # Ти для мене бужеш True
        self.trans = 0
        self.updateBulletButton = 0
        pr.gui_set_font(self.font)
        pr.gui_set_style(0, pr.GuiDefaultProperty.TEXT_SIZE, 20)

    def Update(self):
        if self.gay == False:
            self.trans += 1


        if self.natural == 1 and self.gay == False:
            self.gay = True
        elif self.natural == 1 and self.gay == True:
            self.gay = False

    def Draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_texture(self.BGTexture, 0, 0, pr.WHITE)
        pr.draw_text(f"{self.gay}", 10, 10, 10, pr.WHITE)
        pr.draw_circle_v(pr.Vector2(300, 300 + 30 * math.cos(self.trans/30)), 10, pr.WHITE)
        pr.draw_text("$: 0", 50, 10, 10, pr.GREEN)
        self.updateBulletButton = pr.gui_button(pr.Rectangle(10, 30, 25, 25), pr.gui_icon_text(pr.GuiIconName.ICON_ARROW_UP_FILL, ""))
        pr.draw_text_ex(self.font, "Bullet Update", pr.Vector2(40, 30), 20, 0, pr.WHITE)
        pr.draw_text("Level: 0", 40, 50, 10, pr.WHITE)

        self.updateBulletButton = pr.gui_button(pr.Rectangle(10, 60, 25, 25), pr.gui_icon_text(pr.GuiIconName.ICON_ARROW_UP_FILL, ""))
        pr.draw_text_ex(self.font, "Protect Update", pr.Vector2(40, 60), 20, 0, pr.WHITE)
        pr.draw_text("Level: 0", 40, 80, 10, pr.WHITE)
        
        
        if self.gay == True:
            pr.draw_rectangle(0, 0, 800, 600, pr.Color(0, 0, 0, 150))
            pr.draw_text_ex(self.font, "Trans Paused", pr.Vector2(50, 50), 50, 0, pr.WHITE) # Made by GAYmaster
        
        self.natural = pr.gui_button(pr.Rectangle(800-50, 20, 25, 25), pr.gui_icon_text(pr.GuiIconName.ICON_GEAR_BIG, ""))
        pr.end_drawing()

    def Unload(self):
        pass