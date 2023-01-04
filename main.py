import gpiozero
import playsound


a_major_input = gpiozero.DigitalInputDevice(17)
b_major_input = gpiozero.DigitalInputDevice(17)
c_major_input = gpiozero.DigitalInputDevice(17)
d_major_input = gpiozero.DigitalInputDevice(17)
e_major_input = gpiozero.DigitalInputDevice(17)
f_major_input = gpiozero.DigitalInputDevice(17)
g_major_input = gpiozero.DigitalInputDevice(17)

a_major_input.when_activated = playsound.playsound(
    "notes/A_major", block=False
)
b_major_input.when_activated = playsound.playsound(
    "notes/B_major", block=False
)
c_major_input.when_activated = playsound.playsound(
    "notes/C_major", block=False
)
d_major_input.when_activated = playsound.playsound(
    "notes/D_major", block=False
)
e_major_input.when_activated = playsound.playsound(
    "notes/E_major", block=False
)
f_major_input.when_activated = playsound.playsound(
    "notes/F_major", block=False
)
g_major_input.when_activated = playsound.playsound(
    "notes/G_major", block=False
)


def main():
    # test
    playsound.playsound("notes/A_major")


if __name__ == "__main__":
    main()
