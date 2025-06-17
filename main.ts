input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    strip.show()
    strip.clear()
})
let strip : neopixel.Strip = null
basic.showIcon(IconNames.Happy)
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
loops.everyInterval(100, function on_every_interval() {
    if (input.soundLevel() > 100) {
        strip.clear()
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Yellow))
        strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Green))
        strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Purple))
        strip.show()
        strip.clear()
    } else if (input.soundLevel() > 80) {
        strip.clear()
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Yellow))
        strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Green))
        strip.show()
        strip.clear()
    } else if (input.soundLevel() > 60) {
        strip.clear()
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
        strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Yellow))
        strip.show()
        strip.clear()
    } else if (input.soundLevel() > 50) {
        strip.clear()
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
        strip.show()
        strip.clear()
    } else if (input.soundLevel() > 10) {
        strip.clear()
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        strip.show()
    } else {
        strip.clear()
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        strip.clear()
    }
    
})
