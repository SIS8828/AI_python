import tensorflow as tf

import numpy as np

tf.set_random_seed(777)

# 당뇨병 환자 데이터 셋
xy = np.loadtxt("data-03-diabetes.csv", delimiter=',', dtype=np.float32)
print(xy)
# 훈련용 749명
x_data = xy[:-10, 0:-1]
y_data = xy[:-10, [-1]]

# 테스트용 10명
x_test_data = xy[-10:, 0:-1]
y_test_data = xy[-10:,[-1]]

X = tf.placeholder(tf.float32,shape=[None,8])
Y = tf.placeholder(tf.float32,shape=[None,1])

W = tf.Variable(tf.random_normal([8,1]),name='weight')
b = tf.Variable(tf.random_normal([1]),name = 'bias')

hypothesis = tf.sigmoid(tf.matmul(X,W)+b)

loss = -tf.reduce_mean(Y*tf.log(hypothesis)+(1-Y)*tf.log(1-hypothesis))

train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))


with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        loss_val,_ = sess.run([loss,train],
                              feed_dict={X:x_data,Y:y_data})
        if step % 200 == 0 :
            print(step, loss_val)

    h,p,a = sess.run([hypothesis,predicted,accuracy],feed_dict={X:x_data,Y:y_data})

    print("\nhypothsis:", h, "\npridict: ", p, "\nAccuracy: ", a)

    # 추론

    h,p,y = sess.run([hypothesis,predicted,Y],
                     feed_dict={X:x_test_data,Y:y_test_data})
    print("\nhypothsis:", h, "\npridict: ", p, "\nY ", y)

