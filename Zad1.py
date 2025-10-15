import matplotlib.pyplot as plt
import cv2

image = cv2.imread('zdjecie.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,8))
plt.imshow(image)
plt.show()
