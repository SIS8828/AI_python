import numpy as np

def cross_entropy_error (y, t) :
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

# 2로 예측
y = [0.1, 0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
t = [0, 0, 1,0,0,0,0,0,0,0]

print(cross_entropy_error(np.array(y),np.array(t)))
# 0.510825457099338

# 7로 예측
y = [ 0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(cross_entropy_error(np.array(y),np.array(t)))
# 2.302584092994546

