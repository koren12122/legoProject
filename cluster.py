from PIL import Image, ImageOps
import matplotlib as plt
import numpy
from sklearn.cluster import KMeans


# def clust(image):
#     pixelMap = image.load()
#     pix_arr = []
#     w = image.size[0]
#     h = image.size[1]
#     for i in range(w):
#         for j in range(h):
#             pix_arr.append(pixelMap[i, j])
#
#     new_arr = [list(i) for i in pix_arr]
#     print(new_arr)
#     kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
#     y_kmeans = kmeans.fit_predict(new_arr)
#
#     black = [0, 0, 0]  # 0
#     gray = [128, 128, 128]  # 1
#     red = [255, 0, 0]  # 2
#     green = [0, 255, 0]  # 3
#     blue = [0, 0, 255]  # 4
#     white = [255, 255, 255]  # 5
#
#     for i in range(len(pix_arr)):
#         if y_kmeans[i] == 0:
#             pix_arr[i] = black
#         elif y_kmeans[i] == 1:
#             pix_arr[i] = gray
#         elif y_kmeans[i] == 2:
#             pix_arr[i] = white
#         elif y_kmeans[i] == 3:
#             pix_arr[i] = green
#         elif y_kmeans[i] == 4:
#             pix_arr[i] = blue
#         elif y_kmeans[i] == 5:
#             pix_arr[i] = red
#
#     counter = 0
#     for i in range(w):
#         for j in range(h):
#             pixelMap[i, j] = tuple(pix_arr[counter])
#             counter += 1
#
#     return pixelMap


def KMBWClust(image):
    gray = ImageOps.grayscale(image)
    pixelMap = image.load()
    pix_arr = []
    w = gray.size[0]
    h = gray.size[1]
    for i in range(w):
        for j in range(h):
            pix_arr.append(pixelMap[i, j])
    print(pix_arr)
    new_arr = []
    for i in pix_arr:
        new_arr.append([i])

    kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
    y_kmeans = kmeans.fit_predict(new_arr)

    for i in range(len(pix_arr)):
        if y_kmeans[i] == 0:
            pix_arr[i] = 0
        elif y_kmeans[i] == 1:
            pix_arr[i] = 1
        elif y_kmeans[i] == 2:
            pix_arr[i] = 2
        elif y_kmeans[i] == 3:
            pix_arr[i] = 3

    return pix_arr


def BWClust(image):
    gray = ImageOps.grayscale(image)
    pixelMap = image.load()
    pix_arr = []
    w = gray.size[0]
    h = gray.size[1]
    for i in range(w):
        for j in range(h):
            if -1 < pixelMap[i, j] < 64:
                pix_arr.append(0)
            elif 63 < pixelMap[i, j] < 128:
                pix_arr.append(1)
            elif 127 < pixelMap[i, j] < 192:
                pix_arr.append(2)
            else:
                pix_arr.append(3)

    return pix_arr






