import math
import matplotlib.pyplot as plt

PI2 = math.pi * 2
SAMP_SEC = 240

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
    # print ("FLO:", flo)
    sec = len(data) / SAMP_SEC
    err = energy(data)
    minf = minp = mina = 0
    remain = []
    print ("FPA initial err:", err)
    p = plo
    while p < phi:
        f = flo
        # print ("FLO == f:", f)
        while f <= fhi:
            basis = sindata(f, p, sec)
            a = alo
            while a <= ahi:
                b = mulscalar(basis, a)
                c = subdata(data, b)
                e2 = energy(c)
                # print ("FPA test fpa:", f, p, a, "err:", e2, "new:", e2<err)
                if e2 <= err:
                    err = e2
                    minf = f
                    minp = p
                    mina = a
                    remain = list(c)
                a += da
            f += df
        p += dp
    return minf, minp, mina, remain, err

def max_fpa(data):
    f, p, a, r, e = max_fpa_(data, 1, 10, .25, 0, PI2, PI2/16, .1, 11, .1)
    print ("FPA initial:", f, p, a, e)
    f, p, a, r, e = max_fpa_(data, f-.125, f+.125, .005, p-PI2/32, p+PI2/16-PI2/32, PI2/256, a-.05, a+.05, .01)
    print ("FPA fine-tune:", f, p, a, e)
    return f, p, a, r, e


"""
sin = sindata(2, 0, 1)
# print (sin)

cos = sindata(2, PI2/4, 1)
# print (cos)

mul = muldata(sin, cos)

plt.plot(list(zip(sin, cos, mul)), marker = '.')
plt.show()
"""

test = sindata(5.444, 1, 1)
test = mulscalar(test, 1.6)
test2 = sindata(8.111, 2, 1)
test2 = mulscalar(test2, .75)

# test=test2

plt.plot(list(zip(test, test2)), marker = '.')
plt.show()
#
test = adddata(test2, test)

plt.plot(test, marker = '.')
plt.show()

f, p, a, r, er = max_fpa(test)
print ("RESULT:", f, p, a, "ERR:", er)

plt.plot(list(zip(test, r)), marker = '.')
plt.show()

test = r
f, p, a, r, er = max_fpa(test)
print ("RESULT:", f, p, a, er)

plt.plot(r, marker = '.')
plt.show()
