from idlelib.mainmenu import menudefs

import pyray as pr
import math

import Common
import Common as Com

import ZVOmbie as Vagner
import PPO

import SoundManager as SM

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
        self.texture2 = pr.load_texture("Assets/pigaysus_logo.png")
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
        pr.draw_texture_pro(self.texture2, pr.Rectangle(0, 0, 883, 126), pr.Rectangle(200, 400, 120+400, 139+100), pr.Vector2((120+100)/2, (139+100)/2), 0, pr.Color(255, 255, 255, self.alpha))
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
        self.optSelect = 0
    

    def Update(self):
        self.count += 1
        if self.exitButton == 1:
            self.finishScreen = 1
            SM.choise_button_sound(2)

        if self.playButton == 1:
            self.finishScreen = 2
            SM.choise_button_sound(1)

        if self.settingsButton == 1:
            print("suka")
            self.settingstoggle = True
            SM.choise_button_sound(1)

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
            self.listOptions = [f"Sounds: {Com.sounds}", "Music: "]

            if pr.is_key_pressed(pr.KeyboardKey.KEY_DOWN):
                self.optSelect += 1
            elif pr.is_key_pressed(pr.KeyboardKey.KEY_UP):
                self.optSelect -= 1

            if pr.is_key_pressed(pr.KeyboardKey.KEY_ENTER):
                if self.optSelect == 0 and Com.sounds == True:
                    Com.sounds = False
                else:
                    Com.sounds = True

            for i in range(len(self.listOptions)):
                if self.optSelect == i:
                    pr.draw_text(">>" + self.listOptions[i], 200, 125 + 25 * i, 20, pr.GRAY)
                else:
                    pr.draw_text(self.listOptions[i], 200, 125 + 25 * i, 20, pr.GRAY)


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
        self.updateProtectButton = 0
        self.emo = 50
        self.autoKillyourself = False
        self.timeKillyourselflimit = 500
        self.timeKillyourself = self.timeKillyourselflimit
        self.costSlave = 50
        self.vagners = []
        self.vagnersTimeLimit = 100
        self.vagnerTime = 100
        self.bullets = []
        self.HP = Vagner.pHP
        self.minusHP = 5
        self.rectangleBase = pr.Rectangle(0, 400, 150, 100)
        pr.gui_set_font(self.font)
        pr.gui_set_style(0, pr.GuiDefaultProperty.TEXT_SIZE, 20)
        Com.money = 100
        Com.costUpdateBullet = 100
        Com.costProtectBullet = 100
        Com.updateBulletLevel = 1
        Com.updateProtectLevel = 1


    def Update(self):
        if self.gay == False:
            self.trans += 1
            self.vagnerTime -= 1
            if self.vagnerTime == 0:
                self.vagnerTime = self.vagnersTimeLimit
                self.vagners.append(Vagner.ZVOmbie(900 , 460))
                self.vagnersTimeLimit -= 1
                print("Femboys if cumming")

            if pr.is_mouse_button_pressed(pr.MouseButton.MOUSE_BUTTON_LEFT):
                if self.emo >= 0:
                    SM.choise_button_sound(3)
                    self.emo -= 1
                    self.bullets.append(PPO.PPO(145,470))
                else:
                    SM.choise_button_sound(4)

            for enemy in self.vagners:
                enemy.Update()
                enemy.Draw()

            # Оновлюємо та малюємо кулі
            for bullet in self.bullets:
                bullet.Update()
                bullet.Draw()

            # Перевірка колізій
            self.CheckCollisions()

            if Com.costUpdateBullet > 2:
                self.autoKillyourself = True

            if self.autoKillyourself == True:
                self.timeKillyourself -= 1
                if self.timeKillyourself <= 0:
                    if self.emo >= 0:
                        SM.choise_button_sound(3)
                        self.timeKillyourself = self.timeKillyourselflimit
                        self.emo -= 1
                        self.bullets.append(PPO.PPO(145,470))
                    else:
                        SM.choise_button_sound(4)
                        print("Not enought emo, bum")
                        self.timeKillyourself = self.timeKillyourselflimit


            for i in range(len(self.bullets)):
                self.bullets[i].Update()

            for i in range(len(self.vagners)):
                self.vagners[i].Update()
            
            if self.updateBulletButton == 1:
                if Com.money >= Com.costUpdateBullet:
                    Com.money -= Com.costUpdateBullet
                    Com.costUpdateBullet += 100
                    Com.updateBulletLevel += 1
                    self.timeKillyourselflimit -= 10

            if self.updateProtectButton == 1:
                if Com.money >= Com.costProtectBullet:
                    Com.money -= Com.costProtectBullet
                    Com.costProtectBullet += 100
                    Com.updateProtectLevel += 1

            if self.emButton == 1:
                if Com.money >= self.costSlave:
                    Com.money -= self.costSlave
                    self.emo += 50

            self.bullets = [bullet for bullet in self.bullets if not bullet.destroyed]
            self.vagners = [enemy for enemy in self.vagners if not enemy.destroyed]

            if Vagner.pHP == 0:
                self.finishScreen = 2




        if self.natural == 1 and self.gay == False:
            self.gay = True
        elif self.natural == 1 and self.gay == True:
            self.gay = False

    def CheckCollisions(self):
        # Перевірка колізій між кулею та ворогом
        for bullet in self.bullets:
            for enemy in self.vagners:
                if not bullet.destroyed and not enemy.destroyed:
                    if pr.check_collision_recs(bullet.rectangle, enemy.rect): 
                        print("Collision detected!")
                        SM.choise_button_sound(5)
                        bullet.destroyed = True
                        Com.money += 10
                        enemy.destroyed = True

    def Draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_texture(self.BGTexture, 0, 0, pr.WHITE)
        pr.draw_text(f"{self.gay}", 10, 10, 10, pr.WHITE)
        pr.draw_circle_v(pr.Vector2(300, 300 + 30 * math.cos(self.trans/30)), 10, pr.WHITE)
        pr.draw_text(f"$: {Com.money}", 50, 10, 10, pr.GREEN)

        self.updateBulletButton = pr.gui_button(pr.Rectangle(10, 30, 25, 25), pr.gui_icon_text(pr.GuiIconName.ICON_ARROW_UP_FILL, ""))
        pr.draw_text_ex(self.font, "Bullet Update", pr.Vector2(40, 30), 20, 0, pr.WHITE)
        pr.draw_text(f"Level: {Com.updateBulletLevel}", 40, 50, 10, pr.WHITE)
        pr.draw_text(f"$: {Com.costUpdateBullet}", 80, 50, 10, pr.GREEN)

        self.updateProtectButton = pr.gui_button(pr.Rectangle(10, 60, 25, 25), pr.gui_icon_text(pr.GuiIconName.ICON_ARROW_UP_FILL, ""))
        pr.draw_text_ex(self.font, "Protect Update", pr.Vector2(40, 60), 20, 0, pr.WHITE)
        pr.draw_text(f"Level: {Com.updateProtectLevel}", 40, 80, 10, pr.WHITE)
        pr.draw_text(f"$: {Com.costProtectBullet}", 80, 80, 10, pr.GREEN)

        self.emButton = pr.gui_button(pr.Rectangle(145, 60, 25, 25), pr.gui_icon_text(pr.GuiIconName.ICON_ARROW_UP_FILL, ""))
        pr.draw_text_ex(self.font, "Ammo from Temu", pr.Vector2(182, 60), 20, 0, pr.WHITE)
        pr.draw_text(f"$: {self.costSlave}", 180, 80, 10, pr.GREEN)






        for i in range(len(self.vagners)):
            self.vagners[i].Draw()

        for i in range(len(self.bullets)):
                self.bullets[i].Draw()

        pr.draw_text(f"AMMO: {self.emo}", 100, 500, 10, pr.WHITE)
        pr.draw_text(f"HP:{Vagner.pHP}", 10, 400, 30, pr.RED)



        if self.gay == True: #pegaysus GAYmaster
            pr.draw_rectangle(0, 0, 800, 600, pr.Color(0, 0, 0, 150))
            pr.draw_text_ex(self.font, "Trans Paused", pr.Vector2(50, 50), 50, 0, pr.WHITE)
            MenuButton = pr.gui_button(pr.Rectangle(300, 250, 200, 50), "Return to Menu")

            if MenuButton == 1:
                self.finishScreen = 1
                SM.choise_button_sound(2)
                print("return to Konnas Gachi House")


        self.natural = pr.gui_button(pr.Rectangle(800-50, 20, 25, 25), pr.gui_icon_text(pr.GuiIconName.ICON_GEAR_BIG, ""))
        pr.end_drawing()

    def Unload(self):
        pass


class GameOver(Screen):
    def __init__(self):
        super().__init__()
        self.screenId = 4
        self.font = pr.load_font("Assets/pizda.fnt")
        pr.gui_set_font(self.font)
        pr.gui_set_style(0, pr.GuiDefaultProperty.TEXT_SIZE, 20)
        self.backButton = 0

    def Update(self):
        pass

    def Draw(self):
        pr.draw_text("GAME OVER", 10, 10, 50, pr.RED)
        pr.draw_text(f"Money:{Com.money}", 10, 50, 20, pr.WHITE)
        self.backButton = pr.gui_button(pr.Rectangle(10, 400, 100, 200), "Back to menu")


    def Unload(self):
        pass
