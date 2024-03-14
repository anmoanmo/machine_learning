"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/3/13 17:59
@IDE:PyCharm
=============================
"""
import numpy as np
def normalizeRows(x):
    x_norm = np.linalg.norm(x,axis=1,keepdims=True)
    return x/x_norm

x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print("normalizeRows(x) = " + str(normalizeRows(x)))