import math
import matplotlib.pyplot as plt

PI2 = math.pi * 2
SAMP_SEC = 400
SEC_CHUNK = 0.5

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
        data.append(x - y)
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
    bas = []
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
                    bas = list(b)
                a += da
            f += df
        p += dp
    return minf, minp, mina, remain, bas, err

# FHI  = SAMP_SEC/2
# FSTEP = FHI / 100
FHI  = 80
FSTEP = 1

def max_fpa(data):
    f, p, a, r, b, e = max_fpa_(data, 1, FHI, FSTEP, 0, PI2, PI2/16, .1, 11, .1)
    print ("FPA initial:", f, p, a, e)
    print ("FINETUNE FREQ BRACKET:", f-FSTEP*.5, f+FSTEP*.5, FSTEP/100)
    print ("FINETUNE PHASE BRACKET:", p-PI2/16, p+PI2/16, PI2/256)
    f, p, a, r, b, e = max_fpa_(data, f-FSTEP*.5, f+FSTEP*.5, FSTEP/100, p-PI2/16, p+PI2/16, PI2/256, a-.05, a+.05, .01)
    print ("FPA fine-tune:", f, p, a, e)
    return f, p, a, r, b, e


"""
sin = sindata(2, 0, 1)
# print (sin)

cos = sindata(2, PI2/4, 1)
# print (cos)

mul = muldata(sin, cos)

plt.plot(list(zip(sin, cos, mul)), marker = '.')
plt.show()
"""

test = sindata(4.21387, 1, 1)
test = mulscalar(test, 1.6)
test2 = sindata(15.82444, 2, 1)
test2 = mulscalar(test2, .8)

# test = sindata(8.77, 0, SEC_CHUNK)
# test = mulscalar(test, 1.6)
# test2 = sindata(10, 0, SEC_CHUNK)
# test2 = mulscalar(test2, 0)

# test=test2
t1 = list(test)

orig = test = adddata(test2, test)

plt.plot(list(zip(orig, t1, test2)), marker = '.')
plt.show()

f, p, a, r, b, er = max_fpa(test)
print ("RESULT:", f, p, a, "ERR:", er)

plt.plot(list(zip(orig, b, r)), marker = '.')
plt.show()

test = r
f2, p2, a2, r, b, er = max_fpa(test)
print ("RESULT:", f2, p2, a2, er)

plt.plot(list(zip(orig, b, r)), marker = '.')
plt.show()

rec1 = sindata(f, p, SEC_CHUNK)
rec1 = mulscalar(rec1, a)
rec2 = sindata(f2, p2, SEC_CHUNK)
rec2 = mulscalar(rec2, a2)

recon = adddata(rec1, rec2)

plt.plot(list(zip(orig, recon, r)), marker = '.')
plt.show()
