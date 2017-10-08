import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/kj/pic/1.jpg',-1)
plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
