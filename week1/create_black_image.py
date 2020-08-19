import cv2
import numpy as np
import matplotlib.pyplot as plt

black = np.zeros((150, 150, 3), dtype=np.uint8)
print(black.shape)
plt.imshow(black)
plt.show()