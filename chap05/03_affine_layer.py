import numpy as np

class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dw = None
        self.db = None
    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out

    def backward(self,dout):
        dx = np.dot(dout,self.W.T) # W.T .T를 입력함으로써 전치행렬를 표기할수 있다.
        self.dw = self.dw = np.dot(self.x.T,dout)
        self.db = np.sum(dout, axis=0)
        return dx

if __name__ == "__main__":
    X_dot_W = np.array([[0,0,0],[10,10,10]])
    B = np.array([1,2,3])

    print(X_dot_W+B)

    dy = np.array([[1,2,3],[11,12,13]])
    db = np.sum(dy, axis= 0)
    print(db)