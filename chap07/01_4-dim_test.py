import numpy as np

x = np.random.rand(10, 1, 28, 28) # 무작위로 데이터 생성
print(x.shape)

for i in range(10):
    print(x[i].shape)

# print(x[0,0])

print(x[0][0])
