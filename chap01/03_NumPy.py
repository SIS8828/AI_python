"""
# NumPy 란?
  - 파이썬 기반 데이터 분석 환경에서 행렬 연산을 핵심 라이브러리.
  - "Numerical Python"의 약자로 대규모 다차원 배열과 행렬 연산에
    필요한 다양한 함수를 제공.
  - 특히 메모리 버퍼에 배열 데이터를 저장하고 처리하는 효율적인
    인터페이스를 제공.
  - 파이썬 list 객체를 개선한 NumPy의 ndarray 객체를 사용하면
    더 많은 데이터를 더 빠르게 처리할 수 있다.
"""

# 배열 생성
import numpy as np
import matplotlib.pyplot as plt # pip install matplotlib 설치


# - 1차원 배열(Vector) 정의
arr = np.array([1,2,3])
print(arr)


# - 2차원 배열(Matrix) 정의
arr2 = np.array([[1,2,3],[4,5,6]]) # 2행3열
print(arr2)


# - 3차원 배열(Array) 정의
arr3 = np.array([[[1,2,3],[4,5,6]],[[3,2,1],[6,5,4]]]) # 2면2행3열
print(arr3)
print("arr3.shape : {0}".format(arr3.shape))


# 배열 생성 및 초기화
# zeros((행, 열)) : 0으로 채우는 함수

arr_zeros = np.zeros((3,4))
print(arr_zeros)


# ones((행, 열)) : 1로 채우는 함수
arr_ones = np.ones((2, 2))
print(arr_ones)

# full((행, 열), 값) : 값으로 채우는 함수
arr_full = np.full((3,4),7)
print(arr_full)

# eye(N) : (N,N)의 단위 행렬 생성
arr_eye = np.eye(5)
print(arr_eye)

# empty((행,열)) : 초기화 없이 기존 메모리 값이 들어감.
arr_empty = np.empty((3,3))
print(arr_empty)

# _like(배열) 지정한 배열과 동일한 shape의 행렬을 만듦.
# 종류: np.zeros_like(), np.ones_like(), np.full_like(), np.empty_like()

arr_sample = np.array([[1,2,3],[4,5,6]])
arr_like = np.ones_like(arr_sample)
print(arr_like)


# 배열 데이터 생성 함수

# np.linspace(시작, 종료, 개수):개수에 맞게끔 시작과 종료 사이에
# 균등하게 분배
arr_linspace = np.linspace(1,10,5)
print(arr_linspace)


# plt.plot(arr_linspace, 'o') # 그래프를 그려주는 함수 마커를
# plt.show()                  # 원('o')으로 만든 그래프를 보여줌.

# np.arange(시작, 종료, 스텝) : 시작과 종료 사이에 스텝 간격으로 생성
arr_arange = np.arange(1,20,2)
print(arr_arange) # [ 1  3  5  7  9 11 13 15 17 19]

# plt.plot(arr_arange, 'v')
# plt.show()



# list vs ndarray(1차원배열(Vector))
x1 = [1,2,3]
y1 = [4,5,6]
print(x1+y1) # [1, 2, 3, 4, 5, 6]

x2 = np.array([1,2,3])
y2 = np.array([4,5,6])
print(x2+y2) # [5 7 9]

print(type(x1)) # <class 'list'>
print(type(x2)) # <class 'numpy.ndarray'>

print(x2[2]) # 요소의 참조

x2[2] = 10   # 요소의 수정
print(x2)    # [1  2 10]

# 연속된 정수 벡터의 생성
print(np.arange(10))   # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(5,10)) # [5 6 7 8 9]

x = np.array([10,11,12])
for i in np.arange(1,4):
    print(i)
    print(i+x)

# ndarray형의 주의점
a = np.array([1,1])
b = a # 주소값 복사

print('a = '+str(a)) # a = [1 1]
print('b = '+str(b)) # b = [1 1]

b[0] = 100
print('b = '+str(b)) # b = [100 1]
print('a = '+str(a)) # a = [100 1]

# ======================================

b = a.copy() # 데이터 복사
print('a = '+str(a)) # a = [1 1]
print('b = '+str(b)) # b = [1 1]

b[0] = 100
print('b = '+str(b)) # b = [100 1]
print('a = '+str(a)) # a = [1 1]


# 행렬(2차원)
x = np.array([[1,2,3],[4,5,6]]) # 2행3열
print(x)
print(type(x)) # <class 'numpy.ndarray'>
print(x.shape) # (2, 3) - tuple
w,h = x.shape
print(w) # 2
print(h) # 3
print(x[1,2]) # 요소의 참조 방법
x[1,2] = 100  # 요소의 수정
print(x)


# 요소가 랜덤인 행렬 생성

randArrary = np.random.rand(2,3) # 0 ~ 1 사이의 균일한 분포
print(randArrary)
randArrary = np.random.randn(2,3) # 평균 0 , 분산 1 가우스분포로 난수를 생성.
print(randArrary)
randArrary = np.random.randint(10,20,(2,3))
print(randArrary)

# np.random.normal( 정규분포 평균, 포준편차, (행,열) or 개수):
#   -   정규 분포 확률 밀도에서 표본 추출

mean = 0 # 평균
std = 1 # 표준편차
arr_normal = np.random.normal(mean,std,10000)
print(arr_normal)
plt.hist(arr_normal,bins=100)
# 나누는 구간 갯수(100개 정도로 더 잘게 나누어 보라는 의미)
# plt.show()

# np.random.random((행,열) or size ): (행,열)의 정규 분포로 난수(0~1) 발생
arr_random = np.random.random((3,2))
print(arr_random)

data = np.random.random(10000) # size
plt.hist(data,bins=100)
# plt.show()

# 행렬의 크기 변경
a = np.arange(10)
print(a)
a_arange = a.reshape(2, 5)
print(a_arange)

# 행렬의 사칙연산
x = np.array([[4,4,4],[8,8,8]])
y = np.array([[1,1,1],[2,2,2]])
print(x+y)
# - 스칼라 x 행렬
x = np.array([[4,4,4],[8,8,8]])
scar_arr = 10 * x
print(scar_arr)

# - 산술함수: np. exp(x) 함수, np.sqrt(), np.log(), np.round()
#                   np.mean(), np.str(), np.max(), np.min()
print(np.exp(x))

# - 행렬 * 행렬
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2],[3,4],[5,6]])
print(x.dot(y))

# 원소 접근

x = np.array([[51,55],[14,19],[0,4]])
print(x)
print(x[0][1])

for row in x:
    print(row)

x.flatten()  #x를 1차원 배열로 변환(평탄화)
y = x.flatten()
print(y)

# 슬라이싱
x = np.arange(10)
print(x[:5]) # [0 1 2 3 4]
print(x[5:]) # [4,5,6,7,8,9]
print(x[3:8]) #[3 4 5 6 7]
print(x[3:8:2]) #[3 5 7]
print(x[::-1]) #[9 8 7 6 5 4 3 2 1 0]

y = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 3행 3열

print(y[:2,1:2])

# 조건을 만족하는 데이터 수정
# - bool 배열 사용
x = np.array([1,1,2,3,5,8,15])
print(x > 3) #[False False False False  True  True  True]
y = x[[False ,False ,False ,False , True  ,True  ,True]] #[ 5  8 15]
print(y)
x[x>3] = 555
print(x) #[  1   1   2   3 555 555 555]

