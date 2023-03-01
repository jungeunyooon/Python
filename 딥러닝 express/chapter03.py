# from sklearn.model_selection import train_test_split
# from sklearn import datasets
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target

# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)

# print(X_train.shape)
# print(X_test.shape)

# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=6)
# knn.fit(X_train,y_train)

# y_pred = knn.predict(X_test)
# from sklearn import metrics
# scores = metrics.accuracy_score(y_test,y_pred)

# classes = {0:'setosa',1:'versicolor',2:'virginica'}
# X_new = [[3,4,5,2],[5,4,2,2]]
# y_predict = knn.predict(X_new)

# print(classes[y_predict[0]])
# print(classes[y_predict[1]])

# 필기체 숫자 이미지 분류해보기

import matplotlib.pyplot as plt
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
plt.imshow(digits.images[0],cmap=plt.cm.gray_r,interpolation='nearest')

n_samples = len(digits.images)
data = digits.images.reshape((n_samples,-1))

X_train,X_test,y_train,y_test = train_test_split(data,digits.target,test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

scores = metrics.accuracy_score(y_test,y_pred)
print(scores)

plt.imshow(X_test[10].reshape(8,8),cmap=plt.cm.gray_r,interpolation='nearest')
y_pred = knn.predict([X_test[10]])
print(y_pred)