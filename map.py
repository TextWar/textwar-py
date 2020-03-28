import math
import os
from PIL import Image, ImageDraw, ImageFont
import requests


def get_ava(qq):
    url = "http://q1.qlogo.cn/g?b=qq&nk={}&s=100".format(qq)
    r = requests.get(url)
    if not os.path.isfile("{}.png".format(qq)):
        with open("{}.png".format(qq), 'wb') as f:
            f.write(r.content)
    return "{}.png".format(qq)


class Map:
    def __init__(self, array=None):
        # Init the map
        if array is None:
            self.array = []
        else:
            self.array = array

        self.pic_font_size = 20
        self.pic_width = 1100
        self.pic_height = 2000
        self.pic_back_ground_color = (255, 255, 255)
        self.pic_font_color = (0, 0, 0)
        self.file = "map"
        self.unicode_font = ImageFont.truetype("/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf", self.pic_font_size)
        self.unicode_font_2 = ImageFont.truetype("/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf", 46)
        if self.array != []:
            self.array_height = len(self.array)
            self.array_weight = len(self.array[0])
        else:
            self.array_height = 0
            self.array_weight = 0
        self.pic_offset_x = 10
        self.pic_offset_y = 10
    def __str__(self):
        return ''.join(sum(self.array, []))


    def save_image(self, im):
        im.save(self.file + ".jpg", quality=100)

    def update(self):
        im = Image.new("RGB", (self.pic_width, self.pic_height), self.pic_back_ground_color)
        if len(self.array) == 1:
            self.array = self.array[0]
        for i, a in enumerate(self.array):
            for ia, b in enumerate(a):
                try:
                    if b.isalnum() and get_length(b) >= 5:
                        self.array[i][ia] = "　"
                        file_ = get_ava(b)
                        im2 = Image.open(file_).convert("RGB")
                        self.paste_image(im, im2, i, ia)
                except:
                    pass
        draw = ImageDraw.Draw(im)
        text = str(self)
        draw.text((self.pic_offset_x, self.pic_offset_y), text, font=self.unicode_font, fill=self.pic_font_color)
        print("the end")
        self.save_image(im)
        return self

    def paste_image(self, im, im2, y , x):
        size_offset = self.unicode_font.getoffset("　")
        ascent, descent = self.unicode_font.getmetrics()
        size = (self.unicode_font.getsize("　")[0], self.unicode_font.getsize("　")[1])
        im2 = im2.resize(size)
        print(int(self.pic_offset_x +(size[1] * x)), int(self.pic_offset_x +(size[0] * y)))
        im.paste(im2, box=(int(self.pic_offset_x +(size_offset[0] *(x/10) +size[0] * x)), int(self.pic_offset_y +(descent *2 *(y/(self.pic_font_size/2)) + size[1] * y))))


def get_length(n):
    try:
        if n > 0:
            return int(math.log10(n)) + 1
        elif n == 0:
            return 1
        else:
            return int(math.log10(-n)) + 2
    except:
        return 1

#
# a = Map()
# a.init_array()
# a.file = "map"
# a.generate().array[9][3] = 9
# a.update()
# # a.generate().array[17][10] = 4124982190

# a.update()
#
# array[3][5] = 1230912
# array[3][9] = 1234124
# array[9][4] = 12322154
# array[8][3] = 4219412
# array[16][10] = 321321
# print(array)
# update("map3.jpg",array)
