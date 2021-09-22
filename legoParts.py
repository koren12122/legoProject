from legoPart import legoPart


def isFinished(matrix):
    for row in matrix:
        for val in row:
            if val == -1:
                return False
    return True

def findNextIndex(matrix):
    w = len(matrix)
    h = len(matrix[0])
    for i in range(w):
        for j in range(h):
            if matrix[i][j] == -1:
                return i, j

class legoParts:

    def __init__(self, parts, grid):
        parts_arr = []
        for part in parts:
            instance = legoPart(part, grid)
            parts_arr.append(instance)
            self.lego_parts = parts_arr

    """
    steps for the concat:
    1) 640X640 matrix with -1 in each index.
    2) for each iteration, find the next index with the value -1, and concat the lego part that is next in the sorted 
        legoParts (this part should start in this index) to the accumulate current image.
     
    -- Define some methods to help you --
    """
    def concat(self, image, size):
        pixelMap = image.load()
        lego_parts = self.lego_parts
        wi, hi = size*10, size*10
        matrix = [[-1 for x in range(wi)] for y in range(hi)]
        while not isFinished(matrix):
            for part in lego_parts:
                im = part.image
                w = im.size[1]
                h = im.size[0]
                pix_map = im.load()
                x, y = findNextIndex(matrix)
                for i in range(w):
                    for j in range(h):
                        matrix[x+i][y+j] = pix_map[j, i]
        for i in range(wi):
            for j in range(hi):
                pixelMap[j, size-1-i] = matrix[i][j]
        return matrix


