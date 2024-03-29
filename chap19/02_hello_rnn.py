import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

# Teach hello : hihell -> ihello

idx2char = ['h','i','e','l','o']

x_data = [[0,1,0,2,3,3]] # hihell
x_one_hot = [[[1,0,0,0,0],  # h -> 0
              [0,1,0,0,0],  # i -> 1
              [1,0,0,0,0],  # h -> 0
              [0,0,1,0,0],  # e -> 2
              [0,0,0,1,0],  # l -> 3
              [0,0,0,1,0]]] # l -> 3


y_data = [[1,0,2,3,3,4]] # (h)ihello

input_dim = 5
hidden_size = 5
batch_size = 1
sequence_length = 6
learning_rate = 0.1

X = tf.placeholder(tf.float32, [None,sequence_length,input_dim]) # x_one_hot
Y = tf.placeholder(tf.int32, [None,sequence_length]) # Y label

cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size)

initial_state = cell.zero_state(batch_size, tf.float32)
outputs, _state = tf.nn.dynamic_rnn(cell,X,initial_state=initial_state,dtype=tf.float32)


# FC layer
X_for_fc = tf.reshape(outputs, [-1, hidden_size])
"""
fc_w = tf.get_variable("fc_w", [hidden_size, 5])
fc_b = tf.get_variable("fc_b", [5])
hypothesis = tf.matmul(X_for_fc, fc_w) + fc_b
"""
hypothesis = tf.contrib.layers.fully_connected(inputs=X_for_fc,
                        num_outputs=5, activation_fn=None)

outputs = tf.reshape(hypothesis, [batch_size,sequence_length,5])

weights = tf.ones([batch_size, sequence_length])
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs,
                        targets=Y, weights=weights)

loss = tf.reduce_mean(sequence_loss)

train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

prediction = tf.argmax(outputs, axis=2)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(50):
        l, _ = sess.run([loss, train],
                        feed_dict={X:x_one_hot, Y:y_data})
        result = sess.run(prediction, feed_dict={X:x_one_hot})
        print(i, "loss:", l, "prediction:",result, "Y_data:",y_data)

        result_str = [idx2char[c] for c in np.squeeze(result)]
        print("\nPrediction str:",''.join(result_str))



