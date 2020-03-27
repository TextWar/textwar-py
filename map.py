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
        self.pic_footer = "#############################################\n私聊我输入指令进行操作" + \
                          "\nw=前进|" + "s=后退|\n" + "a=左走|" + "d=右走|"
        self.pic_font_size = 20
        self.pic_width = 1100
        self.pic_height = 2000
        self.pic_back_ground_color = (255, 255, 255)
        self.pic_font_color = (0, 0, 0)
        self.file = "map"

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
                if get_length(b) >= 5:
                    self.array[i][ia] = 0
                    file_ = get_ava(b)
                    im2 = Image.open(file_).convert("RGB")
                    paste_image((10, 10), im, im2, i, ia)
        draw = ImageDraw.Draw(im)
        text = str(self)
        unicode_font = ImageFont.truetype("/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf", self.pic_font_size)
        unicode_font_2 = ImageFont.truetype("/usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf", 46)
        draw.text((10, 10), text, font=unicode_font, fill=self.pic_font_color)
        draw.text((0, self.pic_height - 200), self.pic_footer, font=unicode_font_2, fill=self.pic_font_color)
        print("the end")
        self.save_image(im)
        return self

def paste_image(edge, im, im2, x, y):
    im2 = im2.resize((20, 20))
    im.paste(im2, (int(edge[0] + y * 20), int(edge[1] + x * 22)))


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
