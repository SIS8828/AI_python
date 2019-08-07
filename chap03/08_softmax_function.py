import numpy as np

a = np.array([0.3,2.9,4.0])
exp_a = np.exp(a)
print(exp_a) #[ 1.34985881 18.17414537 54.59815003]

sum_exp_a = np.sum(exp_a) #자연지수함수의 총합
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)
z = np.sum(y)
print(z)
