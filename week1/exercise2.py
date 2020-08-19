import cv2
import matplotlib.pyplot as plt
image2 = cv2.imread("kitty.jpg")

image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

plt.imshow(image2)
plt.show()

