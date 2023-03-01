import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0,1.0,2.0])
y = np.array([3.0,3.5,5.5])

w = 0
b = 0

lrate = 0.01
epochs = 1000 # 반복 횟수  

n = float(len(x)) # 입력 데이터의 개수

# 경사 하강법

for i in range(epochs):
    y_pred = w*x + b
    dw = (2/n)*sum(x*(y_pred-y))
    db = (2/n)*sum(y_pred-y)
    w = w - lrate *dw
    b = b - lrate *db

print(w,b)

y_pred = w*x + b
plt.scatter(x,y)

plt.plot([min(x),max(x)],[min(y_pred),max(y_pred)],color="red")
plt.show()