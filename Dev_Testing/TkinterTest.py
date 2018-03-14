# Project: DataStories
# Author: Michael Albuquerque
# Date Created: 11/28/17
# Python Version: 3.6.2

# Description: Tkinter Test

#import statements

from PIL import Image, ImageFont, ImageDraw


def image_with_lyrics(image_loc, lyrics):
    image = Image.open(image_loc)
    font_type = ImageFont.truetype('Arial.ttf', size=18)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(50, 50), text=lyrics, fill=(255, 69, 0), font=font_type)
    image.show()


image_with_lyrics('/Users/michaelalbuquerque/Downloads/Test.jpg', "Text One")