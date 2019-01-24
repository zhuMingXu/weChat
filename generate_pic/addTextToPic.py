# -*- coding: utf-8 -*-
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont


def text_to_Image(text, image, position, font_size, font_color):
    img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype('./fonts/simsun.ttc', font_size)
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, text, font=font, fill=font_color)
    image = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    return image


if __name__ == '__main__':
    image = cv2.imread('test.jpg')
    text = u"朱明旭"

    image = text_to_Image(text, image, (200, 200), 100, (0, 0, 0))
    cv2.imwrite("textImage.jpg",image)
    #cv2.imshow('img', image)

    #cv2.waitKey(0)



