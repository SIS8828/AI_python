import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

xy = np.loadtxt('data-01-test-score.csv',delimiter=',',dtype=np.float)

# print(xy)

x_data = xy[: 0: -1]
y_data = xy[:,[-1]]

