input.onButtonPressed(Button.A, function () {
    MODE = 1
    basic.showString("FSR")
})
input.onButtonPressed(Button.B, function () {
    MODE = 2
    basic.showString("VEL")
})
let MASS = 0
let B = 0
let M = 0
let FSR = 0
let MODE = 0
MODE = 0
basic.forever(function () {
    FSR = pins.analogReadPin(AnalogPin.P0)
    if (MODE == 1) {
        M = -2.16
        B = 1151
        MASS = (FSR - M) / B
        basic.showNumber(MASS)
    }
    if (MODE == 2) {
        M = -0.476
        B = 1411
        MASS = (FSR - M) / B
        basic.showNumber(MASS)
    }
})
