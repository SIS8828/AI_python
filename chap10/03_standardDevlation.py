import matplotlib.pyplot as plt
import numpy as np
import math
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

# 편차의 합
sumofDeviation = 0.0

# 분산의 합
sumofVariance = 0.0

# 표준편차의 합
sumofStandardDeviation = 0.0

for i, x in enumerate(xs):
    deviation = ys[i] - y[i] # 편차
    variance = deviation ** 2 # 분산
    standardDeviation = math.sqrt(variance)

    sumofDeviation += deviation
    sumofVariance += variance
    sumofStandardDeviation += standardDeviation


    print("x가",x,"일떄 , 실제값 : ", ys[i])
    print("           편차: ", deviation)
    print("           분산: ", variance)
    print("           표준편차: ", standardDeviation)

print("편차의 합 :", sumofDeviation)
print("분산의 합 :", sumofVariance)
print("표준편차의 합 :", sumofStandardDeviation)

plt.plot(xs, y, 'b')
plt.show()