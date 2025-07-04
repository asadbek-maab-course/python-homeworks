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