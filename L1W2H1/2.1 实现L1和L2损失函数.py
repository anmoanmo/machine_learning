"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/3/13 18:42
@IDE:PyCharm
=============================
"""
import numpy as np
def L1(yhat,y):
    return np.sum(np.abs(y-yhat))

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])

print("L1 = " + str(L1(yhat,y)))

def L2(yhat, y):
    return np.dot((y-yhat),(y-yhat).T)

yhat = np.array([.9, 0.2, 0.1, .4, .9 ])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))