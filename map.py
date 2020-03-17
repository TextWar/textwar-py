import math
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
# configuration
from urllib3 import request

def get_ava(qq):
    url = "http://q1.qlogo.cn/g?b=qq&nk={}&s=100".format(qq)
    r = requests.get(url)
    if not os.path.isfile("{}.png".format(qq)):
        with open("{}.png".format(qq), 'wb') as f:
            f.write(r.content)
    return "{}.png".format(qq)
def generate(file):
    font_size = 20
    width = 550
    height = 1000
    back_ground_color = (255, 255, 255)
    font_color = (0, 0, 0)

    array = [
        [8, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4]
    ]


    def walk(maze, x, y, depth):
        maze[x][y] = 0
        rand = random.randint(1, 5)
        if (maze[x][y + 1] == 1 or maze[x][y + 1] == 0) and rand == 1:
            # print("右")
            if maze[x][y + 1] == 0:
                walk(maze, x, y + 1, depth)
            walk(maze, x, y + 1, depth + 1)
        if (maze[x][y - 1] == 1 or maze[x][y - 1] == 0) and rand == 2:
            # print("左")
            if maze[x][y - 1] == 0:
                walk(maze, x, y - 1, depth)
            walk(maze, x, y - 1, depth + 1)
        if (maze[x + 1][y] == 1 or maze[x + 1][y] == 0) and rand == 3:
            # print("前")
            if maze[x + 1][y] == 0:
                walk(maze, x + 1, y, depth)
            walk(maze, x + 1, y, depth + 1)
        if (maze[x - 1][y] == 1 or maze[x - 1][y] == 0) and rand == 4:
            # print("后")
            if maze[x - 1][y] == 0:
                walk(maze, x - 1, y, depth)
            walk(maze, x - 1, y, depth + 1)
        if maze[x + 1][y] == 6 and depth >= 20:
            maze[x + 1][y] = 0
            raise ValueError("the end")
        if maze[x - 1][y] == 2 and depth >= 20:
            maze[x - 1][y] = 0
            raise ValueError("the end")
        if maze[x][y + 1] == 4 and depth >= 20:
            maze[x][y + 1] = 0
            raise ValueError("the end")
        if maze[x][y - 1] == 8 and depth >= 20:
            maze[x][y - 1] = 0
            raise ValueError("the end")

        walk(maze, x, y, depth)
    seed = random.randint(1, 99999999999999)
    random.seed(a=seed)

    for i, a in enumerate(array):
        for ib, b in enumerate(a):
            if len(a) / 2 == ib and random.randint(1, 10) >= 5:
                try:
                    walk(array, i, ib, 20)
                except:
                    pass
    text = array.__str__().replace("]", "\n").replace(",", "").replace("[", "").replace(" ", "").replace("1", "▉").replace(
        "0", "　").replace("8", "▉").replace("4", "▉").replace("2", "▉").replace("6", "▉")
    im = Image.new("RGB", (width, height), back_ground_color)
    draw = ImageDraw.Draw(im)
    unicode_font = ImageFont.truetype("/home/fafa/.fonts/simsun.ttc", font_size)
    unicode_font_2 = ImageFont.truetype("/home/fafa/.fonts/simsun.ttc", 46)
    draw.text((10, 10), text, font=unicode_font, fill=font_color)
    draw.text((10, 10), "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n#######################\n私聊我输入指令进行操作"+"\nw=前进|" + "s=后退|\n" + "a=左走|" + "d=右走|", font=unicode_font_2, fill=font_color)
    im2 = Image.open('842355358.png').convert("RGB")
    im2 = im2.resize((20,20))
    im.paste(im2,(10,10))
    print("the end", seed)
    im.save(file)
generate("map.jpg")