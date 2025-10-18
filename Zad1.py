import matplotlib.pyplot as plt
import cv2
import numpy as np

#Zad 1
#Wczytanie obrazu i wyswietlenie
image = cv2.imread('zdjecie.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# plt.figure(figsize=(10,8))
# plt.imshow(image_rgb)
# plt.title('Wczytany obraz')
# plt.show()

# Konwersja do szarości
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.figure(figsize=(10,8))
# plt.imshow(image_grey, cmap='gray')
# plt.show()


#Zad 2
#Rozmycie Gaussa
def Gaus(image, size=3, sigma=0):
    size = int(input('Podaj wartość rozmiaru jądra Gaussa: '))
    assert size % 2 == 1, 'Rozmiar jądra musi być liczbą nieparzystą'
    sigma = int(input('Podaj wartość odchylenia standardowego horyzontalnego: '))
    image_gaus = cv2.GaussianBlur(image, (size,size), sigma)
    return image_gaus

# image_gaussianblur = Gaus(image_rgb)
# plt.figure(figsize=(10,8))
# plt.imshow(image_gaussianblur)
# plt.title('Rozmycie Gaussa')
# plt.show()


# Zad 3
# t1 = int(input('Podaj wartość dolnej granicy: '))
# t2 = int(input('Podaj wartość górnej granicy: '))
# image_canny = cv2.Canny(image_gray, t1, t2)
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.title('Oryginał')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')
#
# plt.subplot(1,2,2)
# plt.title('Krawędzie (Canny)')
# plt.imshow(image_canny, cmap='gray')
# plt.axis('off')
# plt.show()

# Zad 4
# prog = int(input('Podaj wartość progu: '))
# ret, image_prog = cv2.threshold(image_gray, prog, 255, cv2.THRESH_BINARY)
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.title('Oryginał')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')
#
# plt.subplot(1,2,2)
# plt.title('Progowanie binaryzujące')
# plt.imshow(image_prog, cmap='gray')
# plt.axis('off')
# plt.show()

# Zad 5
# (h, w) = image.shape[:2]
# srodek = (w//2, h//2)
# kat = int(input('Podaj kąt obrotu w stopniach: '))
# macierz_obrotu = cv2.getRotationMatrix2D(srodek, kat, scale=1)
# obrocony = cv2.warpAffine(image_rgb, macierz_obrotu, (w,h))
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.title('Oryginał')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.subplot(1,2,2)
# plt.title('Progowanie binaryzujące')
# plt.imshow(obrocony)
# plt.axis('off')
# plt.show()

# Zad 6
# scale = float(input('Podaj współczynnik przeskalowania: '))
# height = int(image.shape[0]*scale)
# width = int(image.shape[1]*scale)
# resized_image = cv2.resize(image_rgb, (width, height))
#
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.title('Oryginał')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.subplot(1,2,2)
# plt.title('Przeskalowany rozmiar')
# plt.imshow(resized_image)
# plt.axis('off')
# plt.show()

# Zad 7

# image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
# lumin, Cr, Cn = cv2.split(image)
# lumin_equalized = cv2.equalizeHist(lumin)
# image_ycrcb_eq = cv2.merge((lumin_equalized, Cr, Cn))
# image_rgb_eq = cv2.cvtColor(image, cv2.COLOR_YCrCb2RGB)
#
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.title('Oryginał')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')
#
# plt.subplot(1,2,2)
# plt.title('Po wyrównaniu histogramu')
# plt.imshow(image_rgb_eq, cmap='gray')
# plt.axis('off')
# plt.show()

# Zad 8
# jadro = np.array([[0, -1, 0],
#                    [-1, 5,-1],
#                    [0, -1, 0]])
#
# -1 oznacza taka sama głębokość wyjsciowa jak wejsciowa
# wyostrzony = cv2.filter2D(image_rgb, -1, jadro)
#
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.title('Oryginał')
# plt.imshow(image_rgb)
# plt.subplot(1,2,2)
# plt.title('Wyostrzone')
# plt.imshow(wyostrzony)
# plt.show()
#



