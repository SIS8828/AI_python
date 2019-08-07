 # 계단함수(step function)

import numpy as np

def step_function(x):
    if x > 0 :
        return 1
    else:
        return 0

def step_function_nparray(x):
    y = x > 0
    print(y)
    return y.astype(np.int)


if __name__ == "__main__":
    x = step_function(3.2)
    print(x)

    y = step_function(-3.0)
    print(y)

    z = np.array([-1.0,1.0,2.0])
    # i = step_function(z)
    # print(i)+

    wd = step_function_nparray(z)
    print(wd)
