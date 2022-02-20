from PIL import Image, ImageEnhance
from glitch_this import ImageGlitcher
import easygui
import os
import random 

cwd = os.getcwd()
# open 
glitcher = ImageGlitcher()

imgpath = easygui.fileopenbox()
img = Image.open(imgpath)
# img = Image.open(os.path.join(cwd,r'test.jpg'))

# glitching
glitch_img = glitcher.glitch_image(
        img,
        9, 
        color_offset= True,
        seed= random.randint(1, 20000000000)
        )
gImg = glitch_img.rotate(-90)

gcImg = ImageEnhance.Contrast(gImg)
gcImg.enhance(2.5).save(os.path.join(cwd, r'test_out.jpg'))
