
from PIL import Image, ImageOps
import cluster
import LegoGraph
import partition
from legoParts import legoParts
import visitorMap

size = 50

im = Image.open("balance.jpg")
im2 = Image.open("balance.jpg")

im = im.convert('RGB')
im = im.resize((size*10,size*10))

im2 = ImageOps.grayscale(im2)
im2 = im2.resize((size,size))
pixelMap2 = im2.load()
pixArr = cluster.BWClust(im2)

counter = 0
grid = [[0 for x in range(size)] for y in range(size)]
for i in range(size):
    for j in range(size):
        grid[i][j] = pixArr[counter]
        counter += 1

print("grid:", grid)
print("length grid:", len(grid))
print("row len:", len(grid[0]))

comp = LegoGraph.findComponents(grid)  # buggy.. but
print('Comps: ', comp)
print('Number of comps: ', len(comp))

lego_parts = []
for component in comp:
    lego_parts = lego_parts + partition.partitionComp(component)

print("lego parts:", lego_parts)
print("lego parts number:", len(lego_parts))
counter = 0
counter1 = 0
counter2 = 0
counter4 = 0
counter8 = 0

for i in lego_parts:
    counter += len(i)
    if len(i) == 1:
        counter1 += 1
    if len(i) == 2:
        counter2 += 1
    if len(i) == 4:
        counter4 += 1
    if len(i) == 8:
        counter8 += 1
print(counter)
price = counter1*0.07 + counter2*0.11 + counter4*0.15 + counter8*0.21
print("total price ", price,"$")


w = im2.size[0]
h = im2.size[1]
bool_grid = [[False for x in range(len(grid))] for y in range(len(grid))]
sorted_lego_parts = []
for i in range(len(lego_parts)):
    if not visitorMap.isFinished(bool_grid):
        x, y = visitorMap.findNextIndex(bool_grid)
        the_part = visitorMap.findNextPart(lego_parts, [x, y])
        sorted_lego_parts.append(the_part)
        bool_grid = visitorMap.updateGrid(bool_grid, the_part)

print("sorted lego parts:", sorted_lego_parts)
lego_parts_instance = legoParts(sorted_lego_parts, grid)

pixelMap = im.load()
pixelMap = lego_parts_instance.concat(im, size)
im = im.transpose(Image.ROTATE_270)
im.show()
