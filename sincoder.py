import math
import matplotlib.pyplot as plt

pi2 = math.pi * 2

samp_sec = 100
num_blk = 1
freq = 2

blocks = []

for b in range(num_blk):
    data = []
    phase = 0
    for i in range(samp_sec):
        sin = math.sin(phase)
        cos = math.cos(phase)
        data.append((sin, cos))
        phase += pi2 * freq / samp_sec
    print (data)

    plt.plot(data, marker = '.')
    plt.show()