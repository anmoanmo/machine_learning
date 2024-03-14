"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/3/13 19:30
@IDE:PyCharm
=============================
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from datasets.lr_utils import load_dataset

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

index = 153
plt.imshow(train_set_x_orig[index])
print ("y = " + str(train_set_y[:, index])
       + ", it's a '" + classes[np.squeeze(train_set_y[:, index])].decode("utf-8") +
       "' picture.")
plt.show()

m_train = train_set_x_orig.shape[0]
m_test = test_set_x_orig.shape[0]
num_px = train_set_x_orig.shape[1]

print ("Number of training examples: m_train = " + str(m_train))
print ("Number of testing examples: m_test = " + str(m_test))
print ("Height/Width of each image: num_px = " + str(num_px))
print ("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
print ("train_set_x shape: " + str(train_set_x_orig.shape))
print ("train_set_y shape: " + str(train_set_y.shape))
print ("test_set_x shape: " + str(test_set_x_orig.shape))
print ("test_set_y shape: " + str(test_set_y.shape))