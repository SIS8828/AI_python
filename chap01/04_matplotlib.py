import matplotlib.pyplot as plt
import numpy as np

# 단순한 그래프 그리기
"""
# 데이터 준비
x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)


# 그래프 그리기
plt.plot(x,y1, label = "sin")
plt.plot(x,y2, linestyle = "--",label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()


np.random.seed(1234)
x = np.arange(10)
y = np.random.rand(10)

plt.plot(x,y) # 꺽은선 그래프를 등록
plt.show() 
"""

'''
# 3차함수  f(x) = (x-2)x(x+2)
def f(x):
    return (x-2) * x * (x+2)

print(f(0))
print(f(2))
print(f(-2))

# x 값에 대해 ndarray 배열이며 각각에 대응한 f를 한꺼번에 ndarray로 돌려준다.
print(f(np.array([1,2,3]))) # [-3  0 15]
print(type(f(np.array([1,2,3])))) # <class 'numpy.ndarray'>

# 그래프를 그리는 X 의 범위를 -3 ~ 3 까지 하고, 간격은 0.5
x = np.arange(-3,3.5,0.5)

plt.plot(x, f(x))


# 그래프를 장식
def f2(x,w):
    return (x-w) * (x+2)

# x를 정의
x = np.linspace(-3,3,100)

# 차트묘사
plt.plot(x,f2(x,2),color='black', label='$w=2$')
plt.legend(loc="upper left")
plt.ylim(-15,15)
plt.title("$f_2(x)$")
plt.xlabel('$x$')
plt.xlabel('$y$')
plt.grid(True)
'''
"""
# 참조 : 색상

import matplotlib

print(matplotlib.colors.cnames) # 색상 이름


# 그래프를 여러개 보여주기
plt.figure(figsize = (10,3)) # 전체 영역의 크기를 지정
plt.subplots_adjust(wspace=0.5,hspace=0.5) # 그래프의 간격을 지정

for i in range(6):
    plt.subplot(2,3,i+1) # 그래프 위치를 지정
    plt.title(i+1)
    plt.plot(x,f2(x,i))
    plt.ylim(-20,20)
    plt.grid(True)

plt.show()
"""
# 이미지 표시하기
from matplotlib.image import imread

img = imread('img/lena.png')

plt.imshow(img)

plt.show()