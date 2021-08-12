import matplotlib.pyplot as plt
import skimage.io as io

path = r'D:\Workset\misPic\cube\*.jpg'
imlist = io.ImageCollection(path)
n = len(imlist)
print(imlist)
for i in range(n):
    img = imlist[i]
    io.imshow(img)
    plt.show()
    plt.pause(0.2)
    plt.ioff()
    plt.clf()
    plt.close()
