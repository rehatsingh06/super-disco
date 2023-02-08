import gpiozero
from pygame import mixer, time

mixer.init()

# Set this variable to play a sound
SOUND: mixer.Channel | None = None

# TODO: Change pins
# INPUTS

a_major_input = gpiozero.DigitalInputDevice(17)
a_sharp_input = gpiozero.DigitalInputDevice(17)

b_major_input = gpiozero.DigitalInputDevice(18)

c_major_input = gpiozero.DigitalInputDevice(19)
c_sharp_input = gpiozero.DigitalInputDevice(19)

d_major_input = gpiozero.DigitalInputDevice(20)
d_sharp_input = gpiozero.DigitalInputDevice(20)

e_major_input = gpiozero.DigitalInputDevice(21)

f_major_input = gpiozero.DigitalInputDevice(22)
f_sharp_input = gpiozero.DigitalInputDevice(22)

g_major_input = gpiozero.DigitalInputDevice(23)
g_sharp_input = gpiozero.DigitalInputDevice(23)


# SOUNDS

a_major = mixer.Sound("notes/A_major.wav")
a_sharp = mixer.Sound("notes/A_sharp.wav")

b_major = mixer.Sound("notes/B_major.wav")

c_major = mixer.Sound("notes/C_major.wav")
c_sharp = mixer.Sound("notes/C_sharp.wav")

d_major = mixer.Sound("notes/D_major.wav")
d_sharp = mixer.Sound("notes/D_sharp.wav")

e_major = mixer.Sound("notes/E_major.wav")

f_major = mixer.Sound("notes/F_major.wav")
f_sharp = mixer.Sound("notes/F_sharp.wav")

g_major = mixer.Sound("notes/G_major.wav")
g_sharp = mixer.Sound("notes/G_sharp.wav")


a_major_input.when_activated = a_major.play
b_major_input.when_activated = b_major.play
c_major_input.when_activated = c_major.play
d_major_input.when_activated = d_major.play
e_major_input.when_activated = e_major.play
f_major_input.when_activated = f_major.play
g_major_input.when_activated = g_major.play


def main():
    # test
    SOUND = a_major.play()

    while True:
        if SOUND is not None and SOUND.get_busy():
            time.delay(100)


if __name__ == "__main__":
    main()
