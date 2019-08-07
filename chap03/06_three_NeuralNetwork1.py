import numpy as np

# 입력층에서 1층에서 2층으로 전달

X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

print(W1.shape) # (2,3)
print(X.shape) # (2,)
print(B1.shape) #(3,)

A1 = np.dot(X,W1) + B1

# 1층에서 활성화 함수 처리
def sigmoid(x):
    return 1 / (1+np.exp(-x))

Z1 = sigmoid(A1)

print(A1) # [0.3 0.7 1.1]
print(Z1) # [0.57444252 0.66818777 0.75026011]


# 1층에서 2층으로 전달

W2 = np.array([[0.1, 0.3],[0.5,0.2],[0.4,0.6]]) # 행렬의 형태는 3행 2열로 z값3개 a값 2개
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)

# 2층에서 3층으로 전달
W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

# 항등 함수의 정의 - 출력단
# 시그모이드활성함수를 사용하는 것 때문에 통일성을 위한 무의미한 함수
def identity_function(x):
    return x

A3 = np.dot(Z2,W3) + B3
Y = identity_function(A3)

print(Y) # [0.3132875  0.69539338]

