import pyray as pr
import Scenes

class Game:
    def __init__(self):
        pr.init_window(800, 600, "ZombieStrikeRE")
        pr.set_target_fps(60)
        self.screen = Scenes.Logo()

    def Run(self):
        while not pr.window_should_close():
            if pr.is_key_down(pr.KeyboardKey.KEY_F11):
                pr.toggle_fullscreen()
            self.ScreenUpdate()
        pr.close_window()

    
    def ScreenUpdate(self):
        self.screen.Draw()
        self.screen.Update()
        if self.screen.screenId == 0:
            if self.screen.finishScreen == 1:
                self.screen.Unload()
                self.screen = Scenes.Logo2()
        elif self.screen.screenId == 1:
            if self.screen.finishScreen == 1:
                self.screen.Unload()
                self.screen = Scenes.Menu()
        elif self.screen.screenId == 2:
            if self.screen.finishScreen == 1:
                self.screen.Unload()
                pr.close_window()
            elif self.screen.finishScreen == 2:
                self.screen.Unload()
                self.screen = Scenes.Game()
    
    

if __name__ == "__main__":
    gam = Game()
    gam.Run()