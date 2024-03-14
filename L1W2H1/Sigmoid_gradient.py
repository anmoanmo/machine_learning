"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/3/13 16:49
@IDE:PyCharm
=============================
"""

import numpy as np

def basic_sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    return basic_sigmoid(x) * (1 - basic_sigmoid(x))

x = np.array([1, 2, 3])
print(sigmoid_grad(x))