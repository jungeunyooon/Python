# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# print("hello world")
# print(1+1)

# name = "Gil Dong"
# age = 20
# grade = "A"
# weight = 70.1
# print(name,"'s weight is ",weight,"kg") # 띄어쓰기 있이 붙이는 방법
# print(name+"'s weight is",weight,"kg") # 띄어쓰기 없이 붙이는 방법

# a,b,c=1,2,3
# print(a<b)
# print(a!=b)
# print(a==b)

# import math 
# print(math.sqrt(2))

# print(math.e*math.e)
# print(math.e**2)
# print(pow(math.e,2))
# print(math.exp(2))

# import math as ma
# print(ma.e) # 이런식으로 math를 ma로 축약해서 쓸 수 있다. 


# a = [1,2,3,4]
# A = [[1,2],[3,4]]
# print(a)
# print(len(a))

# aa = range(1,100,2)
# aa = list(aa)


# =============================================================================
# a = list(range(1,101)) # stop 조건인 101은 포함하지 않는다. 기억할것
# b = a[:50] # 0부터 49번째 인덱스까지 가져온다
# c = a[50:] # 50부터 끝까지의 인덱스를 가져온다
# d = a[29:40]
# print(a)
# print(b)
# print(c)
# print(d)
# 
# import numpy as np
# np_a=np.array(a)
# np_a=np_a.reshape(len(np_a),1) # (100,1)에서 1을 적어줘야 나중에 오류가 뜨지 않는다. 
# 
# np_b=np.array(range(100,199))
# np_b=np_b.reshape(len(np_b),1)
# np_c=np.hstack((np_a,np_b)) # hstack 이 있고 vstack이 있음
# =============================================================================

# a = [1,2,3,4]
# import numpy as np
# np_a=np.array(a) # 리스트 a를 넘파이 배열로 바꾸겠다 라는 의미이다. 
# np_a=np_a.reshape(len(np_a),1) # (100,1)에서 1을 적어줘야 나중에 오류가 뜨지 않는다. 
# np_b=np.array(range(100,199))
# np_b=np_b.reshape(len(np_b),1)
# np_c=np.hstack((np_a,np_b)) # hstack 이 있고 vstack이 있음


# import numpy as np
# a = np.array([1,2,3,4,5,6])
# print("a=",a)
# print("1.shape:",a.shape)
# print("2.size:",a.size)
# a.fill(3)
# print("3.after fill:",a)
# b = a.reshape(2,3)
# print("4.after reshape:",b)
# print("5.shape after reshape:",b.shape)
# c = b.transpose()
# print("6.transpose:",c)
# print("7.shape after transpose:",c.shape)


# rand와 randn의 차이: rand는 무작위, randn에서 n은 정규화(normalize)를 말한다.정규분포에서 뽑힌다.  
# rand 범위가 0-1일때 -1-+1로 범위를 바꾸려면 2배하고 -1해서 그래프를 옮긴다. 

# =============================================================================
# import numpy as np
# a = np.arange(-10,10,20/100) # (10-(-10))/100  100등분
# print(a)
# =============================================================================

# import numpy as np

# a = np.arange(5,10,0.5)
# b = np.array(['A','A','B','B','B','C'])

# id1 = np.where(a>7.0)
# print(id1,type(id1))

# id2 = np.where(b=='B')
# print(id2,type(id2))

# import numpy as np
# A = np.array([[1,2,3],[4,5,6]])
# print(A+1)
# print(A-2)
# print(2*A)
# print(A/2)
# print(1/A)
# print(2**A)

# A = np.array([1,2,3,4,5])
# B = np.full((5,),2) # 2로 5개를 채워라
# C = np.matnul(A,B)

# print(A,B)
# print(C)
# print(A+B)
# print(A-B)
# print(A*B)


# import numpy as np
# import random

# A = np.random.rand(10,10) 
# A= A*10
# print(A)


# for i in range(10):
#     s = A[i,10]
#     b = np.sum




import numpy as np
import random

A = 10*np.random.rand(10,10) 
A1 = np.sum(A,axis=0)  # axis 검색하면 다 나온다 활용해 구글링은 중요하다
print(np.argmax(A1))
A2 = np.sum(A,axis=1)
print(np.argmin(A2))