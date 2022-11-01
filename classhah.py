# from keras.models import Sequential
# from keras.layers import Dense
# import numpy as np


class Student(object):
    def __init__(self, name, score):    #把一些我们认为必须绑定的属性强制填写进去
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


Lisa = Student('Lisa', 22)
hony = Student('hony', 89)
print(Lisa.score)
print(Lisa.name)
print(Lisa.get_grade())
