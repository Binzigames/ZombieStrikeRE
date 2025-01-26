import pyray as pr
import random as rn
SoundVolm = 100


def choise_button_sound(choice):
    global SoundVolm
    try:
        ButtonSound = pr.load_sound("Assets/Sounds/choise.wav")
        ButtonSound2 = pr.load_sound("Assets/Sounds/choise_2.wav")
        BulletFire = pr.load_sound("Assets/Sounds/gun.wav")
        NoAmmo = pr.load_sound("Assets/Sounds/noammo.wav")
        KillZVO = pr.load_sound("Assets/Sounds/killzvo.wav")

        if choice == 1:
            pr.set_sound_volume(ButtonSound, SoundVolm / 100)
            pr.set_sound_pitch(ButtonSound , rn.randint(1, 10))
            pr.play_sound(ButtonSound)

        elif choice == 2:
            pr.set_sound_volume(ButtonSound2, SoundVolm / 100)
            pr.set_sound_pitch(ButtonSound2, rn.randint(1, 10))
            pr.play_sound(ButtonSound2)

        elif choice == 3:
            pr.set_sound_volume(BulletFire, SoundVolm / 100)
            pr.set_sound_pitch(BulletFire, rn.randint(1, 10))
            pr.play_sound(BulletFire)

        elif choice == 4:
            pr.set_sound_volume(NoAmmo, SoundVolm / 100)
            pr.set_sound_pitch(NoAmmo, rn.randint(1, 10))
            pr.play_sound(NoAmmo)

        elif choice == 5:
            pr.set_sound_volume(KillZVO, SoundVolm / 100)
            pr.set_sound_pitch(KillZVO, rn.randint(1, 10))
            pr.play_sound(KillZVO)
        else:
            print("Invalid choice. Please use 1 or 2.")
    except Exception as e:
        print(f"Error loading or playing sound: {e}")

