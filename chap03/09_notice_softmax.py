import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return  y

a = np.array([1010,1000,990])
'''
y = softmax(a)

print(y) #[nan nan nan]

'''

max = np.max(a)

result = np.exp(a-max) / np.sum(np.exp(a-max))
print(result) #[9.99954600e-01 4.53978686e-05 2.06106005e-09]


def soft_max_computer(a):
     max = np.max(a)
     exp_a = np.exp(a-max)
     sum_exp_a = np.sum(exp_a)
     y = exp_a / sum_exp_a
     return y

result = soft_max_computer(a)
print(result) #[9.99954600e-01 4.53978686e-05 2.06106005e-09]

x = np.array([0.3,2.9,4.0])
y = soft_max_computer(x)
print(y)# [0.01821127 0.24519181 0.73659691]
print(np.sum(y)) # 1.0
