import tensorflow as tf

tf.set_random_seed(777)

# matrix
x_data = [[73.,80.,75.],
          [93.,88.,93.],
          [89.,91.,90.],
          [96.,98.,100.],
          [73.,66.,70.]]

y_data = [[152.],
          [185.],
          [180.],
          [196.],
          [142.]]

X = tf.placeholder(tf.float32,shape=[None,3])
Y = tf.placeholder(tf.float32,shape=[None,1])

W = tf.Variable(tf.random_normal([3,1]),name = 'weight')
b = tf.Variable(tf.random_normal([1]),name = 'bias')

# 가설함수 H(x) = WX + b

hypothesis = tf.matmul(X,W) + b

# loss(cost) 함수

loss = tf.reduce_mean(tf.square(hypothesis - Y))

# 경사하강법 알고리즘
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(8001):
    loss_val , hy_val,_ = sess.run([loss,hypothesis,train] , feed_dict={X:x_data,Y:y_data})

    if step % 100 == 0:
        print(step,loss_val,hy_val)

print("Test-set: ", sess.run(hypothesis,
                             feed_dict={X:[[75.,70,72]]}))