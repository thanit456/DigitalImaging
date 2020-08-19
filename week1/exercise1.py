from skimage import io, color
import matplotlib.pyplot as plt
img = io.imread('kitty.jpg')
print(img.shape)
gray = color.rgb2gray(img)
print(gray.shape)

fig = plt.figure(figsize=(8, 4))
fig.add_subplot(1, 2, 1)
plt.imshow(img)
fig.add_subplot(1, 2, 2)
plt.imshow(gray)
io.show()