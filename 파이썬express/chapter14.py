# # matplot

# import matplotlib.pyplot as plt

# # plt.plot([15.6,14.2,16.3,18.2,17.1,20.2,22.4])
# # plt.show()


# import matplotlib.pyplot as plt

# x = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
# y1 = [15.6,14.2,16.3,18.2,17.1,20.2,22.4]
# y2 = [20.1,23.1,23.8,25.9,23.4,25.1,26.3]

# plt.plot(x,y1,label="Seoul")
# plt.plot(x,y2,label="Busan")
# plt.xlabel("day")
# plt.ylabel("temperature")
# plt.legend(loc="upper left")
# plt.title("Temperatures of Cities")
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# axis = plt.axes(projection="3d")

# z = np.linspace(0,1,100)
# x = z*np.sin(30*z)
# y = z*np.cos(30*z)

# axis.plot3D(x,y,z)
# plt.show()


# 넘파이

# import numpy as np

# heights = [ 1.83,1.76,1.69,1.86,1.77,1.73 ]
# weights = [ 86,74,59,95,80,68]

# np_heights = np.array(heights)
# np_weights = np.array(weights)

# bmi = np_weights/(np_heights**2)
# print(bmi)

# import numpy as np
# import matplotlib.pyplot as plt
# A = np.arange(1,10,2)
# plt.plot(A)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# A = np.linspace(0,10,100)
# plt.plot(A)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# pure = np.linspace(1,10,100)
# noise = np.random.normal(0,1,100)

# signal = pure + noise
# plt.plot(signal)
# plt.show()

# import matplotlib.pylab as plt
# from sklearn import linear_model

# reg = linear_model.LinearRegression() # 선형 회귀 객체 생성

# X = [[174],[152],[138],[128],[186]]
# y = [71,55,46,38,88]

# reg.fit(X,y)
# reg.coef_ # 직선의 기울기
# reg.intercept_ # 직선의 절편
# reg.score(X,y) # 학습 점수 
# reg.predict([[178]])
# plt.scatter(X,y,color='black')
# y_pred = reg.predict(X)
# plt.plot(X,y_pred,color='blue',linewidth=3)
# plt.show()

