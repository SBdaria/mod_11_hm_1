import numpy as np

a = np.random.randint(1, 10, (3, 5))
print('Изначальный массив:', a, sep='\n')
a = a.ravel()
print('Массив в строчку:', a, sep='\n')
a.shape = (5, 3)
print('Массив с другим размером:', a, sep='\n')

a = np.random.randint(1, 10, (3, 3))
print('Матрица:', a, sep='\n')
b = np.linalg.det(a)
print('Определитель матрицы:', b, sep='\n')
c = np.linalg.inv(a)
print('Обратная матрица:', c, sep='\n')


import matplotlib.pyplot as plt
import random

x = sorted([random.randint(1, 10) for i in range(10)])
y = sorted([random.randint(1, 10) for i in range(10)])
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

import requests

r = requests.get('https://vikisews.com/login?next=/profile/')
print(r.status_code)

image = requests.get('https://skillbox.ru/upload/setka_images/11260617012023_ac77ad2a2e993737b916ebafdf36de7f8221dccf.jpg')
with open('new_image.jpg', 'wb') as f:
       f.write(image.content)

type_ = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre/')
type_ = type_.json()
print(type_)
