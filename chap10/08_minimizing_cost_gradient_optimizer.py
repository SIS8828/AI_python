import tensorflow as tf

tf.set_random_seed(777)

x_data = [1,5,10]
y_data = [5,25,50]

W = tf.Variable(-3.0)

# 가설함수
hypothesis = x_data * W

# Loss(cost) 함수
cost = tf.reduce_mean(tf.square(hypothesis - y_data))

# 경사하강법(Gradient Descent : 미분 - 기울기)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)


sess = tf.Session()

sess.run(tf.global_variables_initializer())

for step in range(22):

    print(step,sess.run(cost),sess.run(W))
    sess.run(train)

