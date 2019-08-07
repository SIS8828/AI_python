import numpy as np

# 타겟이 one-hot- encoding 방식일 경우
# 이미지 1장당 평균의 CEE
def cross_entropy_error(y,t):
    if y.dim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y))/batch_size

# 출력이 One-hot-encoding 방식이 아닐경우
# one-hot-encoding 이란 숫자를 0또는 1로 ㅎ표현하는것 [0,0,0,0,1,0,0,0,0,0,0]
def croos_entropy_error2(y,t):
    if y.dim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size,t)]))/batch_size
# 접선의 기울기로 값을 감소시켜야될지 키워야될지 알 수 있다.
# 접선의 기울기는 주어진 식에 미분을 해주면된다.
# 미분은 접선의 기울기
# 계단함수가 정확도를 구하려고쓰는 함수
# 시그모이드는 손실함수에 관한 함수


