import numpy as np
import matplotlib.pyplot as plt
import cv2

#imagen negra
img = np.zeros((10,10,1), np.uint8)

#cambiar pixeles
img[0,5] = 30
img[1,1] = 100
img[2,8] = 132
img[9,9] = 240

#mostramos los valores
print(img)

#mostramos la imagen
plt.imshow(img, cmap = 'gray')
plt.show()




