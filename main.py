def on_button_pressed_ab():
    strip.show()
    strip.clear()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

strip: neopixel.Strip = None
basic.show_icon(IconNames.HAPPY)
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)

def on_every_interval():
    if input.sound_level() > 100:
        strip.clear()
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.YELLOW))
        strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.GREEN))
        strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.PURPLE))
        strip.show()
        strip.clear()
    elif input.sound_level() > 80:
        strip.clear()
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.YELLOW))
        strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.GREEN))
        strip.show()
        strip.clear()
    elif input.sound_level() > 60:
        strip.clear()
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
        strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.YELLOW))
        strip.show()
        strip.clear()
    elif input.sound_level() > 50:
        strip.clear()
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
        strip.show()
        strip.clear()
    elif input.sound_level() > 10:
        strip.clear()
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        strip.show()
    else:
        strip.clear()
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        strip.show()
        strip.clear()
loops.every_interval(100, on_every_interval)
