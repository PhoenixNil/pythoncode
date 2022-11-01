import numpy as np
import os


def get_result(x, y):
    x1 = x//100
    x2 = (x-x1*100)//10
    x3 = x % 10
    y1 = y//100
    y2 = (y-y1*100)//10
    y3 = y % 10
    circles = int(x1 == y1) + int(x2 == y2) + int(x3 == y3)
    triangles = int(((x1 == y2) or (x1 == y3)) and (x1 != y1)) + \
        int(((x2 == y3) or (x2 == y1)) and (x2 != y2)) + \
        int(((x3 == y1) or (x3 == y2)) and (x3 != y3))
    return (circles * 10 + triangles)


d = np.zeros(504, dtype=np.int32)
j = 0
for i in range(123, 988):
    b = i//100
    s = (i-b*100)//10
    g = i % 10
    if (b != s) and (b != g) and (s != g) and (s > 0) and (g > 0):
        d[j] = i
        j += 1

if (not os.path.isfile('test.npy')):
    a = np.zeros((504, 504), dtype=np.int32)
    for i in range(504):
        for j in range(504):
            r = get_result(d[i], d[j])
            a[i, j] = r

    np.save('test.npy', a)
else:
    a = np.load('test.npy')

t = np.zeros((504, 9))
k = np.array([30, 12, 3, 20, 11, 2, 10, 1, 0])
x = -1
while x != 30:
    for i in range(504):
        for j in range(9):
            t[i, j] = np.sum(a[i, :] == k[j]) + j/10.0
    m = np.max(t, axis=1)
    n = np.argmin(m)
    if (x >= 0):
        print(d[a[n, :] >= 0])

    x = -1
    while (x < 0):
        print(d[n], '\nOΔ:')
        x = input()
        x = int(x)
    a[:, a[n, :] != x] = -1
