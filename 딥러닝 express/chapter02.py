# # 리스트
# lst = [10,20,30,40,50] # 리스트 정의
# print(lst)
# print(lst[2])
# lst[2] = 90 # 리스트 요소 변경
# print(lst)
# print(len(lst)) # 리스트의 길이 

# # 리스트 슬라이싱
# lst[0:3] # [10,20,90]
# lst[2:] # [90,40,50]
# lst[:3] # [10,20,90]
# lst[:-1] # [10,20,90,40]


# 넘파이

# import numpy as np

# a = np.array([1,2,3]) # 배열 생성
# b = np.array([1,2,3],[4,5,6],[7,8,9]) # 2차원 배열 생성

# c = np.zeros((3,4)) # 0으로 채워진 배열 생성
# d = np.ones((3,4)) # 1로 채워진 배열 생성
# e = np.eye(3) #  대각선 요소만 1인 배열 생성

# # 연속되는 값으로 배열 생성하기
# np.arange(5) # [0,1,2,3,4]
# np.arange(1,6) # [1,2,3,4,5]
# np.arange(1,10,2) # [1,3,5,7,9] 

# # 균일한 간격의 값으로 배열 생성하기
# np.linspace(0,10,100) # 0에서 10까지 100개의 수들이 균일하게 생성된다.

# np.sort(a) # 배열 정렬
# np.concatenate(a,b) # 2가지 배열 합치기
# np.vstack(a,b) # 배열을 수직으로 쌓기 nstack()도 가능

# # 배열의 형태 변경하기
# new_array = a.reshape((2,3))

# # 배열을 여러개의 작은 배열로 분할하기
# array = np.arange(30).reshape(-1,10)
# arr1,arr2 = np.split(array,[3],axis=1) # axis=1은 세로, axis=0이면 가로로 자른다.

# # 배열에 새로운 축 추가하기 
# a = np.array([1,2,3,4,5,6])
# a.shape # 배열의 형상 몇개의 행과 열이 있는지 
# a1 = a[np.newaxis,:] # (1,6)
# # np.newaxis 및 np.expand_dims 사용 가능
# a2 = a[:,np.newaxis] # (6,1) 

# # 넘파이 곱셈과 행렬 곱셉 : 2개의 행렬을 곱하면 행렬의 요소끼리 곱해진다. 행렬 곱셈(내적)을 하려면 dot()이나 @ 연산자를 사용해야 한다. 

# # 균일 분포 난수 생성하기
# np.random.seed(100) 
# np.random.rand(5) # 5개의 난수를 얻을 수 있다. 
# a = np.random.rand(5,3) # (행의 개수, 열의 개수 )
# # 10-20 사이의 난수 5개 생성
# a=10; b=20
# (b-a)*np.random.rand(5)+a # 정수난수는 randint()

# # 정규 분포 난수 생성
# np.random.randn(5) # randn의 n은 normal을 의미
# np.random.randn(5,4) # 2차원 배열
# a = np.random.normal(loc=0.0,scale=1.0,size=None) # (평균,표준편차,배열의 차원)

# import numpy as np

# y = np.array([1,1,2,2,4])
# ypred = np.array([0.7,1.34,1.89,2.53,3.2])

# mse = (np.square(ypred-y)).mean()
# print(mse)

# matplotlib

# import matplotlib.pyplot as plt

# x = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
# Y1 = [15.6,14.2,16.3,18.3,17.1,20.2,22.4]
# Y2 = [20.1,23.1,23.8,25.9,23.4,25.1,26.3]

# plt.plot(x,Y1,label="seoul")
# plt.plot(x,Y2,label="busan")
# plt.xlabel("day")
# plt.ylabel("temperature")
# plt.legend(loc="upper left")
# plt.title("Temperatures of Cities")
# plt.show()

# import matplotlib.pyplot as plt

# x = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
# plt.plot(x,[15.6,14.2,16.3,18.3,17.1,20.2,22.4],"sm")
# plt.show()

# import matplotlib.pyplot as plt

# x = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
# Y = [15.6,14.2,16.3,18.3,17.1,20.2,22.4]
# plt.bar(x,Y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# numbers = np.random.normal(size=10000)

# plt.hist(numbers) # 히스토그램을 생성하고 화면에 그리는 명령문
# plt.xlabel("value")
# plt.ylabel("freq")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.arange(0,10)
# y1 = np.ones(10)
# y2 = x
# y3 = x**2
# plt.plot(x,y1,x,y2,x,y3)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# def sigmoid(x):
#     s=1/(1+np.exp(-x))
#     ds=s*(1-s)
#     return s,ds

# x = np.linspace(-10,10,100)
# y1,y2 = sigmoid(x)

# plt.plot(x,y1,x,y2)
# plt.xlabel("x")
# plt.ylabel("Sigmoid(X),Sigmoid'(x)")
# plt.show()

# 1. 10에서 19까지의 값을 가지는 1차원 배열을 생성하라

# import numpy as np
# a = np.arange(10,20,1)
# print(a)

# 2. 0부터 9까지의 값으로 넘파이 1차원 배열을 채우고, 이 배열을 거꾸로 하는 문장을 작성하라

# import numpy as np
# a = np.arange(0,10)
# a = a[::-1]
# print(a)

# 3. 0부터 8까지의 값을 가지고 크기가 3X3인 행렬을 생성하라

# import numpy as np
# a = np.arange(0,9)
# a = a.reshape(3,3)
# print(a)

# 4. 난수로 채워진 3X3 넘파이 배열을 생성해보자

# import random
# import numpy as np
# a = np.random.rand(3,3)
# print(a)

# 5. 배열의 테두리에 1, 내부에 0을 가진 3X3 크기의 2차원 배열을 슬라이싱을 이용해 생성해보자

# import numpy as np
# a = np.ones((3,3))
# a[1,1]=0
# print(a)

# import numpy as np
# arr=np.ones((3,3))
# arr[1:-1,1:-1]=0
# print(arr)

# 6. 5X5 행렬을 만들어 체스 보드 패턴으로 채워보자

# import numpy as np
# a = np.zeros((5,5))
# a[1::2,::2] = 1
# print(a)

