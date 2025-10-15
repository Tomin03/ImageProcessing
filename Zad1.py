import matplotlib.pyplot as plt
import cv2

#Zad 1
#Wczytanie obrazu i wyswietlenie
image = cv2.imread('zdjecie.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,8))
plt.imshow(image_rgb)
plt.show()

#Konwersja do szarości
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(10,8))
plt.imshow(image_grey, cmap='gray')
plt.show()

#Zad 2


