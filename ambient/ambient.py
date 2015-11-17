#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys, random

unicorn.brightness(1)

vs = [.5, .6, .7, .8,.9,1]

def color_ambient(cval, flow = 50):
    while True:
	rr = range(cval-flow, cval) + range(cval, cval-flow,-1)
        for z in rr:
            for y in range(8):
                for x in range(8):
                    #rgb = colorsys.hsv_to_rgb(z/360.0,1,random.choice(vs))
                    rgb = colorsys.hsv_to_rgb(z/360.0,1,1)
                    r = int(rgb[0]*255.0)
                    g = int(rgb[1]*255.0)
                    b = int(rgb[2]*255.0)
                    unicorn.set_pixel(x,y,r,g,b)
            unicorn.show()
            time.sleep(0.1)


if __name__ == "__main__":
    color_ambient(130, flow=50)
