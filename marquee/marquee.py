
#!/usr/bin/env python

import PIL 
import unicornhat as unicorn

from PIL import Image, ImageFont, ImageDraw
import time
import sys

unicorn.brightness(.6)

def marquee_text(text, bg_color="black", text_color="white", fontfile=r"PetMe128.ttf"):
    """
    Show marquee (scrolling text) on the Unicorn HAT.
    Select text, text-color, background color and the font used. 
    """
    img = Image.new("RGB", ((len(text)+1)*8+6,8), bg_color) #draw image and approximate the needed width
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype(fontfile, 8) #adapt font size here

    draw.text((6, 0), text, font=font, fill=text_color) #start text with a slight offset
    
    for o_x in range(img.size[0]-8):
        for o_y in range(img.size[1]/8):
            for x in range(8):
                for y in range(8):
                    pixel = img.getpixel(((o_x)+7-x,(o_y*8)+7-y))
                    r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                    try:
                        unicorn.set_pixel(x, y, r, g, b)
                    except IndexError:
                        print x, y
            unicorn.show()
            time.sleep(.04)

if __name__ == "__main__":
    #command line argument text
    
    text = sys.argv[1]
    text_color = sys.argv[2]
    bg_color= sys.argv[3]
    while 1:
        marquee_text(text, bg_color, text_color)
    """
    #pre-defined text
    while 1:
        #marquee_text("Ho ho ho!", "black", "white")
    """    

