# -*- coding: utf-8 -*-
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont


def text_to_Image(text, image, position, font_size, font_color):
    img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype('./huawen.ttf', font_size)
    draw = ImageDraw.Draw(img_PIL)
    for i in range(len(text)):
        draw.text(position, text[i], font=font, fill=font_color)
        position = (position[0],position[1]+65)
    position = (position[0]+30,position[1]-35)
    draw.text(position, ',', font=font, fill=font_color)
    image = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    return image



if __name__ == '__main__':
    image = cv2.imread('test1.jpg')
    text = "姗姗"

    image = text_to_Image(text, image, (550, 110), 60, (0, 0, 0))
    cv2.imwrite("textImage.jpg",image)
    #cv2.imshow('img', image)

    #cv2.waitKey(0)



