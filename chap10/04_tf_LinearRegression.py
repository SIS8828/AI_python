# tensorflow를 이용한 Linear Regression

import tensorflow as tf

tf.set_random_seed(777) # 똑같은 랜덤값을 발생시킴

# x and Y data
x_train = [1,2,3]
Y_train = [1,2,3]


# y = Wx + b
w = tf.Variable(tf.random_normal([1]),name='Wight')
b = tf.Variable(tf.random_normal([1]),name='bias')

# 가설(H(x)) 정의 : H(x) = xW + b
hypothesis = x_train * w +b

# Loss(cost) function
cost = tf.reduce_mean(tf.square(hypothesis - Y_train))

# cost Minimise
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) #
train = optimizer.minimize(cost)

###################################
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(train)
    if step%1000 == 0:
        print(step,sess.run(cost),sess.run(w),sess.run(b))
# 훈련을 아무리 많이 시켜도 1이나 0으로 떨어지지 않는다. 어느정도에서 감소or증가 하다가 멈춤
''' # 출력값
0 2.823292 [2.1286771] [-0.8523567]
1000 0.0014875027 [1.0447946] [-0.10182849]
2000 1.20760815e-05 [1.0040361] [-0.00917497]
3000 9.85495e-08 [1.0003648] [-0.00082887]
4000 8.156131e-10 [1.000033] [-7.546401e-05]
5000 2.2339464e-11 [1.0000057] [-1.213047e-05]
6000 1.22781785e-11 [1.0000043] [-8.612543e-06]
7000 1.22781785e-11 [1.0000043] [-8.612543e-06]
8000 1.22781785e-11 [1.0000043] [-8.612543e-06]
9000 1.22781785e-11 [1.0000043] [-8.612543e-06]
10000 1.22781785e-11 [1.0000043] [-8.612543e-06]
11000 1.22781785e-11 [1.0000043] [-8.612543e-06]
12000 1.22781785e-11 [1.0000043] [-8.612543e-06]
# 6000부터 같은값이 출력된다.
...

'''