import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

xy = np.loadtxt("data-04-zoo.csv", delimiter=',', dtype=np.float32)
# 훈련
x_train_data = xy[:-10, :-1]
y_train_data = xy[:-10, [-1]]  # 마지막항목

x_test_data = xy[-10:, :-1]
y_test_data = xy[-10:, [-1]]

X = tf.placeholder(tf.float32, shape=[None, 16])
Y = tf.placeholder(tf.float32, shape=[None, 1])

# shape
# one-hot encoding 으로 처리해라
Y_one_hot = tf.one_hot(Y, 7)

Y_one_hot = tf.reshape(Y_one_hot, [-1, 7])

W = tf.Variable(tf.random_normal([16, 7]))
b = tf.Variable(tf.random_normal([7]))

# softmax classification hypothesis

hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# Loss(cost) func - Cross Entropy Error
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=tf.matmul(X, W) + b, labels=Y_one_hot))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

prediction = tf.argmax(hypothesis, 1)  # 그것을 0~6으로 나타내는 함수
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))  # 실제값과의 비교
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(train, feed_dict={X: x_train_data, Y: y_train_data})
        if step % 100 == 0:
            loss, acc = sess.run([loss, accuracy], feed_dict={X: x_train_data, Y: y_train_data})
            print("Step : {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(step, loss, acc))

    pred = sess.run(prediction, feed_dict={X: x_test_data})
    # y_data: (N,1) = flatten => (N, ) matches pred.shape
    for p, y in zip(pred, y_test_data.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))
