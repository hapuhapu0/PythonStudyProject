import numpy as np

# 배열선언
Array = [[1, 2, 3], [4, 5, 6]]

# <class 'list'>
print(type(Array))

# a배열을 넘파이 배열로
NpArray = np.array(Array)

# <class 'numpy.ndarray'>
print(type(NpArray))

# (2, 3) 2차원배열 배열길이 가져오기
print(NpArray.shape)

# 배열생성
# 0부터 9까지 2단위로
NpArray = np.arange(0, 10)
print(NpArray)

# 2x2 크기의 배열 선언
# 초기화라 이해했는대 잘 이해한지 모르겠다
NpArray = np.zeros((5, 5))
print(NpArray)

# 5x5 크기의 배열 선언
# 위와 비슷한 거라 이해했다
NpArray = np.ones((5, 5))
print(NpArray)

# [[1, 1], [1, 1]]
NpArray = np.ones((2, 2), int)
# print(NpArray)

# 10x2 배열의 원소를 9로 채운다
NpArray = np.full((2, 10), 9)
print(NpArray)

NpArray = np.eye(3)
print(NpArray)

# 원소가 0~20인 배열생성
NpArray = np.arange(20)
# 5x4 배열로 변환
NpArray = NpArray.reshape(4, 5)
print(NpArray)

