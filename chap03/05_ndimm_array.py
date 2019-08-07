import numpy as np

# 3 x 2 행렬과 2 x 3 행렬의 내적
A = np.array([[1,2],[3,4],[5,6]])
print(A.shape) # (3, 2)
B = np.array([[1,2,3],[4,5,6]])
print(B.shape) # (2, 3)

Z = np.dot(A,B)
print(Z)
"""
[[ 9 12 15]
 [19 26 33]
 [29 40 51]]
"""

Z = np.dot(B,A)
print(Z)
"""
[[22 28]
 [49 64]]
"""

# A가 2차원 행렬, B가 1차원 배열 곱

A = np.array([[1,2],[3,4],[5,6]]) # 3행 2열 대괄호 수로 몇차원인지 구분
B = np.array([1,2]) # (2,) 1차원배열은 튜플형태

print(np.dot(A,B)) #[ 5 11 17]

# 신경망의 내적

X = np.array([1,2]) # x1 = 1 , x2 = 2
W = np.array([[1,3,5],[2,4,6]])
Y = np.dot(X,W)
print(Y) #[ 5 11 17]










































