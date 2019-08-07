import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
import pprint

pp = pprint.PrettyPrinter(indent=4)
sess = tf.InteractiveSession()

h = [1,0,0,0]
e = [0,1,0,0]
l = [0,0,1,0]
o = [0,0,0,1]

with tf.variable_scope('one_cell') as scope:
    # RNN input_dim(4) -> output_dim(2)
    hidden_size = 2
    #cell = tf.contrib.rnn.BasicRNNCell(num_units=hidden_size)
    cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size)
    print(cell.output_size, cell.state_size)

    x_data = np.array([[h]], dtype=np.float32)
    pp.pprint(x_data)

    output, _states = tf.nn.dynamic_rnn(cell,x_data,dtype=tf.float32)

    sess.run(tf.global_variables_initializer())
    pp.pprint(output.eval())














