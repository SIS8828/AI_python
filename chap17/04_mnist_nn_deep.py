import tensorflow as tf
import random
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)
# mnist 데이터를 다운로드한다.
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

# 변수 설정
X = tf.placeholder(tf.float32, shape = [None,784])
Y = tf.placeholder(tf.float32, [None, 10])

W1 = tf.get_variable("W1",shape=[784,512],initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([512]))
L1 = tf.nn.relu(tf.matmul(X,W1)+b1)

W2 = tf.get_variable("W2",shape=[512,512],initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([512]))
L2 = tf.nn.relu(tf.matmul(L1,W2)+b2)

W3 = tf.get_variable("W3",shape=[512,512],initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([512]))
L3 = tf.nn.relu(tf.matmul(L2,W3)+b3)

W4 = tf.get_variable("W4",shape=[512,512],initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([512]))
L4 = tf.nn.relu(tf.matmul(L3,W4)+b4)

W5 = tf.get_variable("W5",shape=[512,10],initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([10]))
hypothesis = tf.matmul(L4,W5) + b5

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis,labels=Y))

train = tf.train.AdamOptimizer(learning_rate = 0.001).minimize(cost)

with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())

    training_epochs = 15
    batch_size = 100 # 한번에 처리할때 100개씩 처리
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples/batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)

            feed_dict = {X:batch_xs,Y:batch_ys}
            c, _ = sess.run([cost,train],feed_dict=feed_dict)
            avg_cost += c / total_batch

        print("Epoch:", '%04d' %(epoch+1), "cost = ", "{: 9f}".format(avg_cost))

    print('learing Finished')

    correct_prediction = tf.equal(tf.argmax(hypothesis,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))
    feed = {X: mnist.test.images, Y: mnist.test.labels}
    print ("Accuracy:", sess.run(accuracy,feed_dict=feed))

    r =  random.randint(0,mnist.test.num_examples-1)
    print("Label: ",sess.run(tf.argmax(mnist.test.labels[r:r+1],1))) # 가장큰값을 반환
    print("Prediction:",sess.run(tf.argmax(hypothesis,1),feed_dict= {X: mnist.test.images[r:r+1]}))

    plt.imshow(mnist.test.images[r:r+1].reshape(28,28))
    plt.show()