import numpy as np

X = np.array([5,10])
W = np.array([[1,2,3],[4,5,6]])
B = np.array([10])

print(X.shape)
print(W.shape)
print(B.shape)

Y = np.dot(X,W) + B
print(Y)
