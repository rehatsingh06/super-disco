import gpiozero
from pygame import mixer, time

mixer.init()

# Set this variable to play a sound
SOUND: mixer.Channel | None = None

# TODO: Change pins
# INPUTS

a_major_input = gpiozero.Button(14)
a_sharp_input = gpiozero.Button(17)

b_major_input = gpiozero.Button(15)

c_major_input = gpiozero.Button(18)
c_sharp_input = gpiozero.Button(27)

d_major_input = gpiozero.Button(23)
d_sharp_input = gpiozero.Button(22)

e_major_input = gpiozero.Button(24)

f_major_input = gpiozero.Button(25)
f_sharp_input = gpiozero.Button(10)

g_major_input = gpiozero.Button(8)
g_sharp_input = gpiozero.Button(9)


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
a_sharp_input.when_activated = a_sharp.play

b_major_input.when_activated = b_major.play

c_major_input.when_activated = c_major.play
c_sharp_input.when_activated = c_sharp.play

d_major_input.when_activated = d_major.play
d_sharp_input.when_activated = d_sharp.play

e_major_input.when_activated = e_major.play

f_major_input.when_activated = f_major.play
f_sharp_input.when_activated = f_sharp.play

g_major_input.when_activated = g_major.play
g_sharp_input.when_activated = g_sharp.play


def main():
    while True:
        time.delay(100)


if __name__ == "__main__":
    main()
