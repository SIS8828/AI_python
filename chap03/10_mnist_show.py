# MNIST
# - 손으로 직접 쓴 숫자(필기체 숫자) 들로 이루어진 데이터 셋
# - 0~9까지의 숫자 이미지로 구성되며, 60,000개의 트레이닝 데이터와
#   10,000 개의 테스트 데이터로 이루어져 있음.

import sys, os

sys.path.append(os.pardir) # 부모 디렉토리의 파일을 가져올 수 있도록 설정.

import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False,one_hot_label=False)

img = x_train[1]
label = t_train[1]
print(label) #0

print(img.shape) #  (784,)

img = img.reshape(28,28) # 형상을 원래 이미지의 크기로 변형
print(img.shape)
img_show(img)

