# 정수 인코딩 

import numpy as np 
X = np.array([['korea',44,7200],
             ['Japan',27,4800],
             ['china',30,6100]])
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:,0]= labelencoder.fit_transform(X[:,0])
print(X)
