import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 2로 예측
y = [0.1, 0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
t = [0, 0, 1,0,0,0,0,0,0,0]

print(mean_squared_error(np.array(y),np.array(t)))
# 0.09750000000000003

# 7로 예측
y = [ 0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(mean_squared_error(np.array(y),np.array(t)))
# 0.5975

