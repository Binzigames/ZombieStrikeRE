import pyray as pr
import random as rn
SoundVolm = 100


def choise_button_sound(choice):
    global SoundVolm
    try:
        ButtonSound = pr.load_sound("Assets/Sounds/choise.wav")
        ButtonSound2 = pr.load_sound("Assets/Sounds/choise_2.wav")

        if choice == 1:
            pr.set_sound_volume(ButtonSound, SoundVolm / 100)
            pr.set_sound_pitch(ButtonSound , rn.randint(1, 10))
            pr.play_sound(ButtonSound)

        elif choice == 2:
            pr.set_sound_volume(ButtonSound2, SoundVolm / 100)
            pr.set_sound_pitch(ButtonSound2, rn.randint(1, 10))
            pr.play_sound(ButtonSound2)
        else:
            print("Invalid choice. Please use 1 or 2.")
    except Exception as e:
        print(f"Error loading or playing sound: {e}")

