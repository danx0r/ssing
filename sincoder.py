import math
import matplotlib.pyplot as plt

PI2 = math.pi * 2
SAMP_SEC = 100

def sindata(freq, phase, seconds):
    data = []
    for i in range(int(SAMP_SEC * seconds)):
        y = math.sin(phase)
        data.append(y)
        phase += PI2 * freq / SAMP_SEC
    return data

def muldata (a, b):
    data = []
    for x, y in zip(a, b):
        data.append(x * y)
    return data

def mulscalar (a, b):
    data = []
    for x in a:
        data.append(x * b)
    return data

def subdata (a, b):
    data = []
    for x, y in zip(a, b):
        data.append(y - x)
    return data

def energy(a):
    sum = 0
    for x in a:
        sum += x ** 2
    return sum ** .5

#detect freq, phase, amplitude of largest component
def max_fpa(data):
    sec = len(data) / SAMP_SEC
    err = energy(data)
    print ("FPA initial err:", err)
    for p in [x * PI2/16 for x in range(1)]:
        for f in [x / 10 for x in range(10, 41)]:
            basis = sindata(f, p, sec)
            for a in [1]: #[x / 4 for x in range(1, 11)]:
                b = mulscalar(basis, a)
                c = subdata(data, b)
                e2 = energy(c)
                print ("FPA test freq:", f, "err:", e2, "new:", e2<err)
                if e2 < err:
                    err = e2
                    minf = f
                    minp = p
                    mina = a
    return minf, minp, mina


"""
sin = sindata(2, 0, 1)
# print (sin)

cos = sindata(2, PI2/4, 1)
# print (cos)

mul = muldata(sin, cos)

plt.plot(list(zip(sin, cos, mul)), marker = '.')
plt.show()
"""

test = sindata(3, 0, 1)

f, p, a = max_fpa(test)
print (f, p, a)

plt.plot(test, marker = '.')
plt.show()

