import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # Y값을 One Hot으로 읽어오게 됩니다

nb_classes = 10 # 0~9개라 총 10개

X = tf.placeholder(tf.float32, [None, 784]) # MNIST data 이미지 모양 28 * 28 = 784 (입력값)
Y = tf.placeholder(tf.float32, [None, nb_classes]) # 0 ~ 9개라 10개의 값을 예측 (출력값)

W = tf.Variable(tf.random_normal([784, nb_classes])) # [입력값, 출력값]
b = tf.Variable(tf.random_normal([nb_classes])) # [출력값]

# Hypothesis (softmax를 이용)
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# Cost 함수 구하기
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

# Test model
is_correct = tf.equal(tf.arg_max(hypothesis, 1), tf.arg_max(Y, 1))

# Calculate accuracy
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

# parameters
training_epochs = 15
batch_size = 100

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # 위에서 변수를 사용하기 위해서 변수를 초기화 함
    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size) # batch_size만큼씩 읽어라
            c, _ = sess.run([cost, optimizer], feed_dict={X: batch_xs, Y: batch_ys})
            avg_cost += c / total_batch

        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

    print("Learning finished")

    # Test the model using test sets
    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))
