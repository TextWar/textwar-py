from PIL import ImageDraw, ImageFont
from PIL import Image
from map import Map, get_length, paste_image, get_ava


class Town(Map):
    def __init__(self, *kwargs, hash_map):
        self.hash_map = hash_map
        super(Town, self).__init__(kwargs)
        self.json_file = ""
    def update(self):
        im = Image.new("RGB", (self.pic_width, self.pic_height), self.pic_back_ground_color)
        if len(self.array) == 1:
            self.array = self.array[0]
        for i, a in enumerate(self.array):
            a.append('\n')
            for ia, b in enumerate(a):
                for ic, c in enumerate(self.hash_map):
                    # print(c,ic)
                    if b == ic:
                        replaced = ""
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
                if get_length(b) >= 5:
                    self.array[i][ia] = 0
                    file_ = get_ava(b)
                    im2 = Image.open(file_).convert("RGB")
                    paste_image((10, 10), im, im2, i, ia)
        draw = ImageDraw.Draw(im)
        text = str(self)
        unicode_font = ImageFont.truetype("/usr/share/fonts/Unifont/Unifont.ttf", self.pic_font_size)
        # unicode_font.
        unicode_font_2 = ImageFont.truetype("/usr/share/fonts/steam-fonts/arial.ttf", 46)
        draw.text((10, 10), text, font=unicode_font, fill=self.pic_font_color)
        draw.text((0, self.pic_height - 200), self.pic_footer, font=unicode_font_2, fill=self.pic_font_color)
        self.save_image(im)
        return self
    # def get_map(self):
