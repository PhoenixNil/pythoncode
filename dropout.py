from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(1, input_shape=(2,), activation='sigmoid'))
