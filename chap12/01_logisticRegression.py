import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([2, 1], name='weight'))
b = tf.Variable(tf.random_normal([1], name='bias'))

# 가설함수 : sigmoid 함수 적용
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

# 손실함수
loss = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))

# 경사하강법
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

train = optimizer.minimize(loss)

predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, Y), dtype=tf.float32))

with tf.Session() as sess:  # sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        loss_val, _ = sess.run([loss, train], {X: x_data, Y: y_data})

        if step % 200 == 0:
            print(step, loss_val)

    h, c, a = sess.run([hypothesis, predict, accuracy], {X: x_data, Y: y_data})

    print("\nhypth:", h, "\npridict: ", c, "\nAccuracy: ", a)

    print("4시간 수업, 2시간 자율학습: ", sess.run(predict, {X: [[4, 2]]}))
    print("3시간 수업, 1시간 자율학습: ", sess.run(predict, {X: [[3, 1]]}))

