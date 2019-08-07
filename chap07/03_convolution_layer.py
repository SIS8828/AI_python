import numpy as np
from common.util import im2col
class Convolution:
    def __init__(self,W,b,stride= 1,pad=0):
        self.W = None
        self.b = None
        self.stride = stride
        self.pad = pad

    def forward(self,x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = int(((H+2 * self.pad-FH)/self.stride) + 1)
        out_W = int(((W + 2 * self.pad - FH) / self.stride) + 1)

        col = im2col(x, FH, FW, self.stride, self.pad)

        col_W =self.W.reshape(FN, -1)
        out = np.dot(col,col_W) + self.b

        out = out.reshape(N, out_h, out_W, -1).transpose(0,3,1,2)

        return out








