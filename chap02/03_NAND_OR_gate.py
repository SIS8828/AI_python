import numpy as np
import math
# NAND Gate
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    bias = 0.7

    tmp = np.sum(w * x) + bias

    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    bias = math.sin(60)

    tmp = np.sum(w * x) + bias

    if tmp <= 0:
        return 0
    else:
        return 1

if __name__=="__main__":
    result = NAND(0,0)
    print(result)

    result = NAND(0, 1)
    print(result)

    result = NAND(1, 0)
    print(result)

    result = NAND(1, 1)
    print(result)

    print("##########################")

    result = OR(0, 0)
    print(result)

    result = OR(0, 1)
    print(result)

    result = OR(1, 0)
    print(result)

    result = OR(1, 1)
    print(result)

