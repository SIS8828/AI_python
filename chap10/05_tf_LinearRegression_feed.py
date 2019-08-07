import tensorflow as tf

tf.set_random_seed(777)

# y = Wx + b
w = tf.Variable(tf.random_normal([1]),name='Wight') # W와b를 Variable이라는 개념으로 정의
b = tf.Variable(tf.random_normal([1]),name='bias') # 우리는 W와b의 값을 모르므로 임의의값 추출

#
x = tf.placeholder(tf.float32, shape=[None])
y = tf.placeholder(tf.float32, shape=[None])
# 실질적인 데이터는 나중에 프로그램을 수행할때 해당값을 그때 넣어준다.

hypothsis = x * w + b

# cost 함수
cost = tf.reduce_mean(tf.square(hypothsis - y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) # 최적화의 minimize 함수를 찾아서 cost를 최소화하라고 명시하면
train = optimizer.minimize(cost)# 자기가 알아서 최적화된 최소값을 찾아내기 시작함

session = tf.Session() # 세션생성
session.run(tf.global_variables_initializer()) # Variable을 initalize 한다

for step in range(2001):
    cost_val,w_val,b_val,_ = session.run([cost,w,b,train],feed_dict={x:[1,2,3],y:[1,2,3]})

    if step % 20 == 0:
        print(step,cost_val,w_val,b_val)

print(session.run(hypothsis, feed_dict={x:[5]}))
print(session.run(hypothsis, feed_dict={x:[2.5]}))
print(session.run(hypothsis, feed_dict={x:[1.5,3.5]}))

for step in range(2002):
    cost_val,w_val,b_val,_ = session.run([cost, w,b,train],feed_dict={x:[1,2,3,4,5,6,7,8,9,10],y:[10,15,20,25,30,35,40,45,50,55]})
    #  _은 None을 반환해주는데 이거는 train이 함수객체이므로 함수를 반환하면 주소값을 반환해주기떄문에 값이 나타나지는 않는다.
    print(session.run([cost, w,b,train],feed_dict={x:[1,2,3,4,5,6,7,8,9,10],y:[10,15,20,25,30,35,40,45,50,55]}))
    if step % 20 == 0:
        print(step, cost_val, w_val,b_val)

    print(session.run([cost, w,b,train],feed_dict={x:[1,2,3,4,5,6,7,8,9,10],y:[10,15,20,25,30,35,40,45,50,55]}))