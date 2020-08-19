from skimage import io
img = io.imread('kitty.jpg')
io.imsave('kitty_new.jpg', img)

import cv2
cv2.imwrite('kitty_new2.jpg', img)