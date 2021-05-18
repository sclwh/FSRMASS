def on_button_pressed_a():
    global MODE
    MODE = 1
    basic.show_string("FSR")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global MODE
    MODE = 2
    basic.show_string("VEL")
input.on_button_pressed(Button.B, on_button_pressed_b)

MASS = 0
B = 0
M = 0
FSR = 0
MODE = 0
MODE = 0

def on_forever():
    global FSR, M, B, MASS
    FSR = 100000
    if MODE == 1:
        M = -2.16
        B = 1151
        MASS = (FSR - M) / B
        basic.show_number(MASS)
    if MODE == 2:
        M = -0.476
        B = 1411
        MASS = (FSR - M) / B
        basic.show_number(MASS)
basic.forever(on_forever)
