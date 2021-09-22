"""
Given component we want to name a partition to this component to legal lego parts, of 1,2,4,8 for example.
"""


def partitionComp(comp):
    lego_parts = []
    arr, new_comps = fillEight(comp)
    lego_parts = lego_parts + arr  # concat
    if len(new_comps) == 0:
        return lego_parts
    arr, new_comps = fillFour(new_comps)
    lego_parts = lego_parts + arr
    if len(new_comps) == 0:
        return lego_parts
    arr, new_comps = fillTwo(new_comps)
    lego_parts = lego_parts + arr
    if len(new_comps) == 0:
        return lego_parts
    arr = fillOne(new_comps)
    lego_parts = arr + lego_parts
    return lego_parts


def inComp(index, comp):
    for pix in comp:
        if index == pix:
            return True
    return False


def fillEight(comp):
    new_comp = comp
    arr = []
    x = 0
    y = 0
    for pix in new_comp:
        x = pix[0]
        y = pix[1]
        if inComp([x+1,y], new_comp) and inComp([x+2,y], new_comp) and inComp([x+3,y], new_comp) and inComp([x,y+1], new_comp) and inComp([x+1,y+1], new_comp) and inComp([x+2,y+1], new_comp) and inComp([x+3,y+1], new_comp) and inComp([x,y], new_comp):
            arr.append([[x,y],[x+1,y], [x+2,y], [x+3,y],[x,y+1],[x+1,y+1], [x+2,y+1], [x+3,y+1]])
            new_comp.remove([x,y])
            new_comp.remove([x+1,y])
            new_comp.remove([x+2,y])
            new_comp.remove([x+3,y])
            new_comp.remove([x,y+1])
            new_comp.remove([x+1,y+1])
            new_comp.remove([x+2,y+1])
            new_comp.remove([x+3,y+1])

    for pix in new_comp:
        x = pix[0]
        y = pix[1]
        if inComp([x, y+1], new_comp) and inComp([x, y+2], new_comp) and inComp([x, y+3], new_comp) and inComp([x+1, y], new_comp) and inComp([x+1, y+1], new_comp) and inComp([x+1, y+2], new_comp) and inComp([x+1, y+3], new_comp) and inComp([x, y], new_comp):
            arr.append([[x, y], [x, y+1], [x, y+2], [x, y+3], [x+1, y], [x+1, y+1], [x+1, y+2], [x+1, y+3]])
            new_comp.remove([x, y])
            new_comp.remove([x, y+1])
            new_comp.remove([x, y+2])
            new_comp.remove([x, y+3])
            new_comp.remove([x+1, y])
            new_comp.remove([x+1, y+1])
            new_comp.remove([x+1, y+2])
            new_comp.remove([x+1, y+3])

    return arr, new_comp


def fillFour(comp):
    new_comp = comp
    arr = []
    x = 0
    y = 0
    for pix in new_comp:
        x = pix[0]
        y = pix[1]
        if inComp([x, y], new_comp) and inComp([x, y+1], new_comp) and inComp([x+1,y], new_comp) and inComp([x+1,y+1], new_comp):
            arr.append([[x,y],[x,y+1],[x+1,y],[x+1,y+1]])
            new_comp.remove([x, y])
            new_comp.remove([x, y+1])
            new_comp.remove([x+1, y])
            new_comp.remove([x+1, y+1])

    return arr,new_comp


def fillTwo(comp):
    new_comp = comp
    arr = []
    x = 0
    y = 0
    for pix in new_comp:
        x = pix[0]
        y = pix[1]
        if inComp([x, y], new_comp) and inComp([x, y + 1], new_comp):
            arr.append([[x, y], [x, y + 1]])
            new_comp.remove([x, y])
            new_comp.remove([x, y + 1])

    for pix in new_comp:
        x = pix[0]
        y = pix[1]
        if inComp([x, y], new_comp) and inComp([x+1, y], new_comp):
            arr.append([[x, y], [x+1, y]])
            new_comp.remove([x, y])
            new_comp.remove([x+1, y])

    return arr,new_comp

def fillOne(comp):  # Not nessesery lolz
    new_comp = comp
    arr = []
    for pix in new_comp:
        arr.append([pix])
    return arr


