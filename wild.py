import random

from PIL import Image, ImageDraw, ImageFont

from map import Map, get_length, paste_image, get_ava


class WildMap(Map):
    def __init__(self, *kwargs):
        super().__init__(kwargs)
        self.array_height = 80
        self.array_weight = 50

    def init_array(self):
        # self.array = [[0] * self.array_height for _ in xrange(self.array_weight)]
        for i in range(0, self.array_height):
            new = []
            for ia in range(0, self.array_weight):
                new.append(1)
            self.array.append(new)

    def generate(self, seed=random.randint(1, 99999999999999)):
        def walk(maze, x, y, depth):
            if maze[x][y] == 1:
                maze[x][y] = 0
            if depth >= 90:
                raise ValueError("the end")
            rand = random.randrange(1, 6)
            if depth >= 70 and rand == 5:
                raise ValueError("the end")
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

            walk(maze, x, y, depth)

        random.seed(a=seed)

        for i, a in enumerate(self.array):
            for ib, b in enumerate(a):
                if len(a) / 2 == ib and random.randint(1, 10) >= 5:
                    try:
                        walk(self.array, i, ib, 20)
                    except:
                        pass
        return self

