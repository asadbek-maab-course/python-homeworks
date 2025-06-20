# task 1
import numpy as np

@np.vectorize
def f2c(t):
    return (t - 32) * (5 / 9)

temps = np.array([32, 68, 100, 212, 77])
temps_c = f2c(temps)

print(temps_c)

# task 2
import numpy as np

@np.vectorize
def power_of_elements(a, b):
    return np.power(a, b)

nums = [2, 3, 4, 5]
powers = [1, 2, 3, 4]
print(power_of_elements(nums, powers))


#task 3
import numpy as np

A = np.array([
    [4, 5, 6],
    [3, -1, -1],
    [2, 1, -2]
])
B = np.array([7, 4, 5])
ans = np.linalg.solve(A, B)
x, y, z = ans
print(x, y, z)

# task 4
import numpy as np

A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
B = np.array([12, -5, 15])
ans = np.linalg.solve(A, B)
i1, i2, i3 = ans
print(i1, i2, i3)

# image task
import numpy as np
from PIL import Image

PATH = "/media/asadbek/D/maab/new/python-homeworks/lesson-14"

with Image.open(PATH + '/cybertruck.jpg') as img:
    arr = np.array(img)

def flip_image(arr):
    gorizontal_flip = Image.fromarray(np.flip(arr, axis=1))
    gorizontal_flip.save(PATH + "/cybertruck_gorizontal_flip.jpg")
    vertical_flip = Image.fromarray(np.flip(arr, axis=0))
    vertical_flip.save(PATH + "/cybertruck_vertical_flip.jpg")
flip_image(arr)

def add_noise(arr):
    h, w, rgb = arr.shape
    for i in np.random.randint(low=0, high=h*w, size=np.random.randint(0, h*w//2)):
        arr[np.random.randint(0, h)][np.random.randint(0, w)] = np.random.randint(low = 0, high = 255, size=(3,))
    noised_image = Image.fromarray(arr)
    noised_image.save(PATH + "/noised_car.jpg")

# add_noise(arr)

bright_k = 40
@np.vectorize
def increase_val(a):
    return min(255, a+bright_k)
def brighten_channels(arr):
    arr[:, :, :] = increase_val(arr[:, :, :])
    brighten_image = Image.fromarray(arr)
    brighten_image.save(PATH + "/brighten.jpg")
# brighten_channels(arr)


def apply_mask(arr):
    mask_size = (100, 100)
    h, w, rgb = arr.shape
    h_start_index = (h - mask_size[0]) // 2
    w_start_index = (w - mask_size[1]) // 2
    arr[h_start_index:h_start_index+mask_size[0], w_start_index:w_start_index+mask_size[1], :] = 0
    masked_image = Image.fromarray(arr)
    masked_image.save(PATH + "/masked.jpg")

# apply_mask(arr)