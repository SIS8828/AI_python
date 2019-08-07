import matplotlib.pyplot as plt
import numpy as np

xs = [1,2]
ys = [2,5]

plt.plot(xs,ys,'rx')
plt.ylim(0.1,6)
plt.xlim(0,3)

# w 예상치
w = 1
# b 예상치
b = 2

# numpy를 이용해서 y 라는 배열을 xs 배열을 이용해 쉽게 계산
y = w * np.array(xs) + b

plt.plot(xs,y,'b')


plt.show()