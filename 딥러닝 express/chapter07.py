# 3차원 배열 생성

# import numpy as np
# x = np.array(
#     [[[0,1,2,3,4],
#      [5,6,7,8,9]],
#     [[10,11,12,13,14],
#      [15,16,17,18,19]],
#     [[20,21,22,23,24],
#      [25,26,27,28,29]],])
# print(x.ndim)
# print(x.shape)

# BCD

# y_true = [ [1],[0],[0],[1] ]
# y_pred = [ [0.8],[0.3],[0.5],[0.9] ]
# bce = tf.keras.losses.BinaryCrossentropy()
# print(bce(y_true,y_pred).numpy())


# categorical cross entropy

# y_true = [[0.0,1.0,0.0],[0.0,0.0,1.0],[1.0,0.0,0.0]]
# y_pred = [[0.6,0.3,0.1],[0.3,0.6,0.1],[0.1,0.7,0.2]]
# cce = tf.keras.losses.CategoricalCrossentropy()
# print(cce(y_true,y_pred).numpy())

# sparse categorical cross entropy

# y_true = [1,2,0]
# y_pred = [[0.6,0.3,0.1],[0.3,0.6,0.1],[0.1,0.7,0.2]]
# scce = tf.keras.losses.SparseCategoricalCrossentropy()
# print(cce(y_true,y_pred).numpy())

# MSE

# y_true = [12,20,29,60]
# y_pred = [14,18,27,55]
# mse = tf.keras.losses.MeanSquaredError()
# print(mse(y_true,y_pred).numpy())


# # 사용자 지정 손실 함수 

# def custom_loss_function (y_true,y_pred):
#     squared_difference = tf.square ( y_true-y_pred)
#     return tf.reduce_mean (squared_difference, axis=-1)
# model.compile (optimizer = 'adam', loss = custom_loss_function)

# 가중치 초기화


# from tensorflow.keras import layers
# from tensorflow.keras import initializers

# layer = layers.Dense(
#     units=64, 
#     kernel_initializer=initializers.RandomNormal(stdden=0.01) # 가중치 초기화 
#     bias_initianlizer=initializers.Zeros() # 바이어스 초기화
# )

