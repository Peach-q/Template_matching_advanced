import os

import cv2

method = cv2.TM_SQDIFF_NORMED

# Прочтение изображений из папки с изображениями
small_image = cv2.imread('C:/Users/Mi/PycharmProjects/pythonProject/green.jpg')  # искомое изображение
cwd = os.getcwd()
files = os.listdir(cwd + '/flow/')

for pic in files:
    pic_plate = cwd + '/flow/' + pic
    large_image = cv2.imread(pic_plate)
    result = cv2.matchTemplate(small_image, large_image, cv2.TM_CCOEFF_NORMED)
# Сведение разницы к минимуму
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
# Отрисовка выделения совпадения:
# Извлечение координат лучшего совпадения
    MPx, MPy = mnLoc

    trows, tcols = small_image.shape[:2]
# Отрисовка выделяющего квадрата
    cv2.rectangle(large_image, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
    print(result.max())
    if result.max() >= 0.7:
# Отображение выделения на совпадающих изображениях совпавших
        cv2.imshow('output', large_image)

        cv2.waitKey(0)