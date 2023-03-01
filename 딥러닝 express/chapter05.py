# import numpy as np
# epsilon = 0.0000001

# def perceptron(x1,x2):
#     X = np.array([x1,x2])
#     W = np.array([1.0,1.0])
#     B = -1.5
#     sum = np.dot(W,X)+B
#     if sum > epsilon :
#         return 1
#     else : 
#         return 0
# print(perceptron(0,0))
# print(perceptron(1,0))
# print(perceptron(0,1))
# print(perceptron(1,1))

# 퍼셉트론 학습 알고리즘 구현하기

# import numpy as np

# epsilon = 0.0000001

# def step_func(t):
#     if t > epsilon : return 1 
#     else : return 0

# X = np.array([
#     [0,0,1],
#     [0,1,1],
#     [1,0,1],
#     [1,1,1]
# ])

# y = np.array([0,0,0,1])
# W = np.zeros(len(X[0]))

# def perceptron_fit(X,Y,epochs=10):
#     global W
#     eta = 0.2
#     for t in range(epochs):
#         print("epoch=",t,"=====================")
#         for i in range(len(X)):
#             predict = step_func(np.dot(X[i],W))
#             error = Y[i] - predict
#             W += eta * error * X[i]
#             print("현재 처리 입력=",X[i],"정답=",Y[i],"출력=",predict,"변경된 가중치=",W)
#         print("==============================")
# def perceptron_predict(X,Y):
#     global W
#     for x in X:
#         print(x[0],x[1],"->",step_func(np.dot(x,W)))

# perceptron_fit(X,y,6)
# perceptron_predict(X,y)


# sklearn 으로 퍼셉트론 실습하기 

# from sklearn.linear_model import Perceptron

# X = [[0,0],[0,1],[1,0],[1,1]]
# y = [0,0,0,1]

# clf = Perceptron(tol=1e-3,random_state=0)

# clf.fit(X,y)
# print(clf.predict(X))

# 퍼셉트론 시각화

from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import Perceptron
import numpy as np

clf = Perceptron(tol=1e-3,random_state=0)

X,y = make_blobs(n_samples=100,centers=2)
clf.fit(X,y)

from sklearn.metrics import accuracy_score
print(accuracy_score(clf.predict(X),y))

plt.scatter(X[:,0],X[:,1],c=y,s=100)
plt.xlabel("x1")
plt.ylabel("x2")

x_min,x_max = X[:,0].min() -1, X[:,0].max() + 1
y_min,y_max = X[:,1].min() -1, X[:,1].max() + 1

xx,yy = np.meshgrid(np.arange(x_min,x_max,0.1),np.arange(y_min,y_max,0.1))
Z = clf.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)

plt.contourf(xx,yy,Z,alpha=0.4)
plt.show()


