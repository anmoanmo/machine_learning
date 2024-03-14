"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/3/13 16:40
@IDE:PyCharm
=============================
"""

import numpy as np

def basic_sigmod(x):
    return 1 / (1 + np.exp(-x))

print(basic_sigmod(np.array([1,2,3,4,5,6])))
