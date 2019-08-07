# Tensor Manipulation
# https://www.tensorflow.org/api_docs/python/

import tensorflow as tf
import numpy as np
import pprint

tf.set_random_seed(777)

pp = pprint.PrettyPrinter(indent=4)
sess = tf.InteractiveSession()

# 1차원 배열
t = np.array([0.,1.,2.,3.,4.,5.,6.])
pp.pprint(t)
print(t)
"""
print(t.shape) # shape, (7,)
print(t.ndim)  # rank, 1
print(t[0],t[1],t[-1]) # 0.0 1.0 6.0
print(t[2:5], t[4:-1]) # [2. 3. 4.] [4. 5.]
print(t[:2], t[3:]) # [0. 1.] [3. 4. 5. 6.]

# 2차원 배열(Matrix:행렬)
t = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.],[10.,11.,12.]]) # 4x3행렬
pp.pprint(t)
print(t.ndim)  # rank-2
print(t.shape) # shape(4,3)

# shape, Rank, Axis
t = tf.constant([1,2,3,4])
print(tf.shape(t)) # Tensor("Shape:0", shape=(1,), dtype=int32)
print(tf.shape(t).eval()) # [4]

t = tf.constant([[1,2],[3,4]])
print(tf.shape(t)) # Tensor("Shape_2:0", shape=(2,), dtype=int32)
print(tf.shape(t).eval()) # [2 2]

t = tf.constant([[[1,2,3,4],[5,6,7,8]],
                 [[9,10,11,12],[13,14,15,16]],
                 [[17,18,19,20],[21,22,23,24]]])
print(tf.shape(t)) # Tensor("Shape_4:0", shape=(3,), dtype=int32)
print(tf.shape(t).eval()) # [3 2 4]

t = tf.constant([[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
                  [[13,14,15,16], [17,18,19,20], [21,22,23,24]]]])
print(tf.shape(t).eval()) # [1 2 3 4]

# matmul vs multiply
matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])
result = tf.matmul(matrix1,matrix2).eval()
print(result) # [[12]], 3*2+3*2

result = (matrix1 * matrix2).eval()
print(result)# [[6 6] [6 6]]


# Random values for variable initializations
print(tf.random_normal([3]).eval())
print(tf.random_normal([2,3]).eval())


# Reduce Mean / Sum
print(tf.reduce_mean([2,4]).eval()) # 3

x = [[1.,2.],[3.,4.]]
result = tf.reduce_mean(x).eval()
print(result) # 2.5

result = tf.reduce_mean(x, axis=0).eval()
print(result) # [2. 3.]

result = tf.reduce_mean(x, axis=1).eval()
print(result) # [1.5 3.5]

result = tf.reduce_mean(x, axis=-1).eval()
print(result) # [1.5 3.5]

result = tf.reduce_mean(x, axis=-2).eval()
print(result) # [2. 3.]

# ====================================
result = tf.reduce_sum(x).eval()
print(result) # 10.0

result = tf.reduce_sum(x, axis=0).eval()
print(result) # [4. 6.]

result = tf.reduce_sum(x, axis=1).eval()
print(result) # [3. 7.]

result = tf.reduce_sum(x, axis=-1).eval()
print(result) # [3. 7.]

result = tf.reduce_sum(x, axis=-2).eval()
print(result) # [4. 6.]

result = tf.reduce_mean(tf.reduce_sum(x, axis=1)).eval()
print(result) # 5.0

# argmax with axis
x = [[0,1,2],[2,1,0]]
print(tf.argmax(x, axis=0).eval()) # [1 0 0]
print(tf.argmax(x, axis=1).eval()) # [2 0]
print(tf.argmax(x, axis=-1).eval()) # [2 0]
print(tf.argmax(x, axis=-2).eval()) # [1 0 0]

# Reshape, squeeze, expand_dims
t = np.array([[[0,1,2],[3,4,5]],
              [[6,7,8], [9,10,11]]])
print(t.shape) # (2, 2, 3)

print(tf.reshape(t, shape=[-1, 3]).eval())
# [[ 0  1  2][ 3  4  5][ 6  7  8][ 9 10 11]]

result = tf.reshape(t, shape=[-1, 1, 3]).eval()
print(result)
# [[[ 0  1  2]]
#  [[ 3  4  5]]
#  [[ 6  7  8]]
#  [[ 9 10 11]]]
print(result.shape) # (4, 1, 3)

result = tf.squeeze([[0],[1],[2]]).eval()
print(result) # [0 1 2]
print(result.shape) # (3,)

result = tf.expand_dims([0,1,2], axis=1).eval()
print(result) # [[0] [1] [2]]
print(result.shape) # (3, 1)


# One-hot Encoding
print(tf.one_hot([[0],[1],[2],[0]], depth=3).eval())
## [[[1. 0. 0.]] [[0. 1. 0.]] [[0. 0. 1.]] [[1. 0. 0.]]]

t = tf.one_hot([[0],[1],[2],[0]], depth=3).eval()
print(tf.reshape(t, shape=[-1, 3]).eval())
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]

# casting
print(tf.cast([1.8, 2.2, 3.3, 4.9], tf.int32).eval()) # [1 2 3 4]
print(tf.cast([True, False, 1 == 1, 0 == 1], tf.int32).eval())


# Stack
x = [1,4]
y = [2,5]
z = [3,6]

print(tf.stack([x,y,z]).eval()) # [[1 4][2 5][3 6]]
print(tf.stack([x,y,z], axis=0).eval()) # [[1 4][2 5][3 6]]
print(tf.stack([x,y,z], axis=1).eval()) # [[1 2 3][4 5 6]]

# Ones like and Zeros like
x = [[0, 1, 2],[2, 1, 0]]

z = tf.ones_like(x).eval()
print(z) # [[1 1 1] [1 1 1]]

z = tf.zeros_like(x).eval()
print(z) # [[0 0 0][0 0 0]]


# zip
for x,y in zip([1,2,3],[4,5,6]):
    print(x,y)

for x,y,z in zip([1,2,3],[4,5,6],[7,8,9]):
    print(x,y,z)
"""

