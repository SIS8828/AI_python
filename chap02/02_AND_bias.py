import numpy as np
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.7 # 어떠한 값도 가능

    tmp = np.sum(w * x) + b

    if tmp <= 0 :
        return 0
    else:
        return 1



if __name__=="__main__":
    result = AND(0,0)
    print(result)

    result = AND(0, 1)
    print(result)

    result = AND(1, 0)
    print(result)

    result = AND(1, 1)
    print(result)
