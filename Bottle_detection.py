import numpy as np
import cv2
from matplotlib import pyplot as plt

bottle_cascade = cv2.CascadeClassifier('Desi.xml')

img = cv2.imread('Bottle2.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
font = cv2.FONT_HERSHEY_SIMPLEX
bottles = bottle_cascade.detectMultiScale(gray, 1.3, 2, 75)

for ( q, w, e, r) in bottles:
    img = cv2.rectangle(img, (q, w), (q+e, w+r), (255, 0, 0), 2)
    cv2.putText(img, 'Bottle', (q, w), font, 0.9, (255, 0, 0), 2)

p, l, m = cv2.split(img)
img = cv2.merge([m, l, p])

plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
