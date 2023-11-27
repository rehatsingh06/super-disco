from typing import Callable
from pathlib import Path
import gpiozero
from pygame import mixer, time

mixer.init()

NOTES_DIR = Path(__file__).parent / "notes"

# Set this variable to play a sound
SOUND: mixer.Channel | None = None

# TODO: Change pins
# INPUTS

a_major_input = gpiozero.DigitalInputDevice(14, bounce_time=0.1)
a_sharp_input = gpiozero.DigitalInputDevice(17, bounce_time=0.1)
b_major_input = gpiozero.DigitalInputDevice(15, bounce_time=0.1)
c_major_input = gpiozero.DigitalInputDevice(18, bounce_time=0.1)
c_sharp_input = gpiozero.DigitalInputDevice(27, bounce_time=0.1)
d_major_input = gpiozero.DigitalInputDevice(23, bounce_time=0.1)
d_sharp_input = gpiozero.DigitalInputDevice(22, bounce_time=0.1)
e_major_input = gpiozero.DigitalInputDevice(24, bounce_time=0.1)
f_major_input = gpiozero.DigitalInputDevice(25, bounce_time=0.1)
f_sharp_input = gpiozero.DigitalInputDevice(10, bounce_time=0.1)
g_major_input = gpiozero.DigitalInputDevice(8, bounce_time=0.1)
g_sharp_input = gpiozero.DigitalInputDevice(9, bounce_time=0.1)


# SOUNDS

a_major = mixer.Sound(NOTES_DIR / "A_major.wav")
a_sharp = mixer.Sound(NOTES_DIR / "A_sharp.wav")

b_major = mixer.Sound(NOTES_DIR / "B_major.wav")

c_major = mixer.Sound(NOTES_DIR / "C_major.wav")
c_sharp = mixer.Sound(NOTES_DIR / "C_sharp.wav")

d_major = mixer.Sound(NOTES_DIR / "D_major.wav")
d_sharp = mixer.Sound(NOTES_DIR / "D_sharp.wav")

e_major = mixer.Sound(NOTES_DIR / "E_major.wav")

f_major = mixer.Sound(NOTES_DIR / "F_major.wav")
f_sharp = mixer.Sound(NOTES_DIR / "F_sharp.wav")

g_major = mixer.Sound(NOTES_DIR / "G_major.wav")
g_sharp = mixer.Sound(NOTES_DIR / "G_sharp.wav")


def play_sound(sound: mixer.Sound, note: str) -> Callable[[], None]:
    def wrapped():
        sound.play()
        mixer.fadeout(4000)
        print("Playing note", note)

    return wrapped


a_major_input.when_activated = play_sound(a_major, "A")
a_sharp_input.when_activated = play_sound(a_sharp, "A#")

b_major_input.when_activated = play_sound(b_major, "B")

c_major_input.when_activated = play_sound(c_major, "C")
c_sharp_input.when_activated = play_sound(c_sharp, "C#")

d_major_input.when_activated = play_sound(d_major, "D")
d_sharp_input.when_activated = play_sound(d_sharp, "D#")

e_major_input.when_activated = play_sound(e_major, "E")

f_major_input.when_activated = play_sound(f_major, "F")
f_sharp_input.when_activated = play_sound(f_sharp, "F#")

g_major_input.when_activated = play_sound(g_major, "G")
g_sharp_input.when_activated = play_sound(g_sharp, "G#")


def main():
    while True:
        time.delay(100)


if __name__ == "__main__":
    main()
