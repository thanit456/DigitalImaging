from skimage import io
img = io.imread('kitty.jpg')
io.imshow(img)
io.show()

import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()