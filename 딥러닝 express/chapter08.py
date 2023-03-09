# 정수 인코딩 

# import numpy as np 
# X = np.array([['korea',44,7200],
#              ['Japan',27,4800],
#              ['china',30,6100]])
# from sklearn.preprocessing import LabelEncoder
# labelencoder = LabelEncoder()
# X[:,0]= labelencoder.fit_transform(X[:,0])
# print(X)

# 원-핫 인코딩

# import numpy as np
# X = np.array([['korea',44,7200],
#              ['Japan',27,4800],
#              ['china',30,6100]])

# from sklearn.preprocessing import OneHotEncoder

# xx = OneHotEncoder.fit_transform(X[:,0].reshpae(-1,1)).toarray()
# print(xx)

# X = np.delete(X,[0],axis=1)
# X = np.concatenate((xx,X),axis =1)
# print(X)

# 원-핫 인코딩(케라스사용)

# class_vector = [2,6,6,1]

# from tensorflow.keras.utils import to_categorical
# output = to_categorical(class_vector,num_classes=7,data="int32")
# print(output)

