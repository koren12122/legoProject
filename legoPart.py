from PIL import Image


def is4x2(part):
    x_arr = []
    for index in part:
        x_arr.append(index[0])
    return max(x_arr) - min(x_arr) > 2


def is2x1(part):
    x_arr = []
    for index in part:
        x_arr.append(index[0])
    return max(x_arr) - min(x_arr) > 0


class legoPart:

    def __init__(self, part, grid):
        length = len(part)
        self.length = length
        x = part[0][0]
        y = part[0][1]
        color = grid[x][y]
        if length == 8:
            if is4x2(part):
                if color == 0:
                    im = Image.open("4X2B.jpg")
                    im = im.resize((20, 40))
                    self.image = im.convert('RGB')
                elif color == 1:
                    im = Image.open("4X2G1.jpg")
                    im = im.resize((20, 40))
                    self.image = im.convert('RGB')
                elif color == 2:
                    im = Image.open("4X2G2.jpg")
                    im = im.resize((20, 40))
                    self.image = im.convert('RGB')
                elif color == 3:
                    im = Image.open("4X2W.jpg")
                    im = im.resize((20, 40))
                    self.image = im.convert('RGB')
            else:
                if color == 0:
                    im = Image.open("2X4B.jpg")
                    im = im.resize((40, 20))
                    self.image = im.convert('RGB')
                elif color == 1:
                    im = Image.open("2X4G1.jpg")
                    im = im.resize((40, 20))
                    self.image = im.convert('RGB')
                elif color == 2:
                    im = Image.open("2X4G2.jpg")
                    im = im.resize((40, 20))
                    self.image = im.convert('RGB')
                elif color == 3:
                    im = Image.open("2X4W.jpg")
                    im = im.resize((40, 20))
                    self.image = im.convert('RGB')
        elif length == 4:
            if color == 0:
                im = Image.open("2X2B.jpg")
                im = im.resize((20, 20))
                self.image = im.convert('RGB')
            elif color == 1:
                im = Image.open("2X2G1.jpg")
                im = im.resize((20, 20))
                self.image = im.convert('RGB')
            elif color == 2:
                im = Image.open("2X2G2.jpg")
                im = im.resize((20, 20))
                self.image = im.convert('RGB')
            elif color == 3:
                im = Image.open("2X2W.jpg")
                im = im.resize((20, 20))
                self.image = im.convert('RGB')
        elif length == 2:
            if is2x1(part):
                if color == 0:
                    im = Image.open("2X1B.jpg")
                    im = im.resize((10, 20))
                    self.image = im.convert('RGB')
                elif color == 1:
                    im = Image.open("2X1G1.jpg")
                    im = im.resize((10, 20))
                    self.image = im.convert('RGB')
                elif color == 2:
                    im = Image.open("2X1G2.jpg")
                    im = im.resize((10, 20))
                    self.image = im.convert('RGB')
                elif color == 3:
                    im = Image.open("2X1W.jpg")
                    im = im.resize((10, 20))
                    self.image = im.convert('RGB')
            else:
                if color == 0:
                    im = Image.open("1X2B.jpg")
                    im = im.resize((20, 10))
                    self.image = im.convert('RGB')
                elif color == 1:
                    im = Image.open("1X2G1.jpg")
                    im = im.resize((20, 10))
                    self.image = im.convert('RGB')
                elif color == 2:
                    im = Image.open("1X2G2.jpg")
                    im = im.resize((20, 10))
                    self.image = im.convert('RGB')
                elif color == 3:
                    im = Image.open("1X2W.jpg")
                    im = im.resize((20, 10))
                    self.image = im.convert('RGB')
        else:
            if color == 0:
                im = Image.open("1X1B.jpg")
                im = im.resize((10, 10))
                self.image = im.convert('RGB')
            elif color == 1:
                im = Image.open("1X1G1.jpg")
                im = im.resize((10, 10))
                self.image = im.convert('RGB')
            elif color == 2:
                im = Image.open("1X1G2.jpg")
                im = im.resize((10, 10))
                self.image = im.convert('RGB')
            elif color == 3:
                im = Image.open("1X1W.jpg")
                im = im.resize((10, 10))
                self.image = im.convert('RGB')






