import math
import matplotlib.pyplot as plt

PI2 = math.pi * 2
SAMP_SEC = 100

def sindata(freq, phase, seconds):
    data = []
    for i in range(SAMP_SEC * seconds):
        y = math.sin(phase)
        data.append(y)
        phase += PI2 * freq / SAMP_SEC
    return data

def muldata (a, b):
    data = []
    for x, y in zip(a, b):
        data.append(x * y)
    return data

sin = sindata(2, 0, 1)
# print (sin)

cos = sindata(2, PI2/4, 1)
# print (cos)

mul = muldata(sin, cos)

plt.plot(list(zip(sin, cos, mul)), marker = '.')
plt.show()