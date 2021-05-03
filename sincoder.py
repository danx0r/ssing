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

def adddata (a, b):
    data = []
    for x, y in zip(a, b):
        data.append(x + y)
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
def max_fpa_(data, flo, fhi, df, plo, phi, dp, alo, ahi, da):
    sec = len(data) / SAMP_SEC
    err = energy(data)
    # print ("FPA initial err:", err)
    p = plo
    while p < phi:
        f = flo
        while f <= fhi:
            basis = sindata(f, p, sec)
            a = alo
            while a <= ahi:
                b = mulscalar(basis, a)
                c = subdata(data, b)
                e2 = energy(c)
                # print ("FPA test fpa:", f, p, a, "err:", e2, "new:", e2<err)
                if e2 < err:
                    err = e2
                    minf = f
                    minp = p
                    mina = a
                    remain = list(c)
                a += da
            f += df
        p += dp
    return minf, minp, mina, remain

def max_fpa(data):
    f, p, a, r = max_fpa_(data, 1, 30, .25, 0, PI2, PI2/16, .1, 11, .1)
    print ("FPA initial:", f, p, a)
    f, p, a, r = max_fpa_(data, f-.125, f+.125, .01, p-PI2/32, p+PI2/16-PI2/32, PI2/256, a-.05, a+.05, .01)
    print ("FPA fine-tune:", f, p, a)
    return f, p, a, r


"""
sin = sindata(2, 0, 1)
# print (sin)

cos = sindata(2, PI2/4, 1)
# print (cos)

mul = muldata(sin, cos)

plt.plot(list(zip(sin, cos, mul)), marker = '.')
plt.show()
"""

test = sindata(3.33, 1.5, 1)
test = mulscalar(test, 5.76)
test2 = sindata(5.11, 2.5, 1)
test2 = mulscalar(test2, 4.11)

plt.plot(list(zip(test, test2)), marker = '.')
plt.show()

test = adddata(test2, test)

plt.plot(test, marker = '.')
plt.show()

f, p, a, r = max_fpa(test)
print (f, p, a)

plt.plot(list(zip(test, r)), marker = '.')
plt.show()

