import numpy as np
import matplotlib.pyplot as plt
import cv2

black = np.zeros((150, 150), dtype=np.uint8)
plt.imshow(black, cmap='gray')
plt.show()

red = np.zeros((100, 100, 3), dtype=np.uint8)
red[:, :, 2] = 255
cv2.imwrite('red_100x100.jpg', red)