import keras
from keras.models import Sequential
# 引入sequential，这个就是一个空的网络结构，并且这个结构是一个顺序的序列，所以叫Sequential，
from keras.layers import Dense
import numpy as np

a = np.array([[0, 1, 0], [1, 3, 2], [0, 0, 0]])     #第一个数组跟第二个必须相同的dim
y = np.array([0, 0, 1])
simple_model = Sequential()
simple_model.add(Dense(5, input_shape=(
    a.shape[1],), activation='relu', name='layer1'))  # 5个端口，必须要一个输入端口
simple_model.add(Dense(4, activation='relu', name='layer2'))
simple_model.add(Dense(1, activation='sigmoid', name='layer3'))
simple_model.compile(optimizer='sgd', loss='mean_squared_error')
simple_model.fit(a, y, epochs=100)
simple_model.predict(a[0:1])
