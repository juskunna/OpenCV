import cv2

import numpy as np
import pandas as pd

image_plate = cv2.imread("/content/lautanen.JPG")
print(image_plate.shape)
height, width, layout = image_plate.shape

cv2.line(image_plate, ((int)(width/2), 0), ((int)(width/2), height), (255,0,255), 3)
cv2.circle(image_plate, (100, 100), 10, (255,0,255), 3)

cv2.line(image_plate, (0, 630), (width, 630), (255,0,0), 3)

rows = []
for image_pixel in range(0, width):
  color_data = image_plate[627, image_pixel]
  #print(color_data)
  row = [image_pixel, color_data[0]]
  rows.append(row)
  if color_data[0] > 175:
    cv2.line(image_plate, (image_pixel, 630), (image_pixel, 625), (0,0,255), 1)

df = pd.DataFrame(rows, columns=["image_pixel", "color_data"])
df.plot(x="image_pixel")

cv2.imshow(image_plate)
