import numpy as np
from common.util import im2col

x1 = np.random.rand(1,3,7,7) # (데이터 수, 채널수, 높이, 너비) 4차원의 데이터
col1 = im2col(x1,5,5)
print(col1.shape) # 9, 75 (칸의갯수, 칸에 더해질 숫자의 수)

