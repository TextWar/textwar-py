from PIL import ImageDraw, ImageFont
from PIL import Image
from map import Map, get_length, get_ava


class Town(Map):
    def __init__(self, *kwargs, hash_map):
        self.hash_map = hash_map
        super(Town, self).__init__(kwargs)
        self.json_file = ""
        if len(self.array) == 1:
            self.array = self.array[0]
    def update(self):
        im = Image.new("RGB", (self.pic_width, self.pic_height), self.pic_back_ground_color)
        for i, a in enumerate(self.array):
            a.append('\n')
            for ia, b in enumerate(a):
                for ic, c in enumerate(self.hash_map):
                    # print(c,ic)
                    if b == str(ic):
                        if c.startswith('*'):
                            replaced = c[1:]
                        else:
                            replaced = c
                        if len(replaced.encode("utf8")) == 1:
                            replaced = replaced + " "
                        if len(replaced.encode("utf8")) == 2:
                            replaced = replaced + ""
                        self.array[i][ia] = replaced
                        break
                    try:
                        if len(b) >= 5:
                            self.array[i][ia] = "　"
                            file_ = get_ava(b)
                            im2 = Image.open(file_).convert("RGB")
                            self.paste_image(im, im2, i, ia)
                    except:
                        pass
        draw = ImageDraw.Draw(im)
        text = str(self)
        draw.text((10, 10), text, font=self.unicode_font, fill=self.pic_font_color)
        self.save_image(im)
        return self
    # def get_map(self):
