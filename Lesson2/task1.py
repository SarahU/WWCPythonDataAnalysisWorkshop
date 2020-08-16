import numpy as np


a = np.arange(54)
b = np.logspace(1,100,54)
c = np.ones(54, int)

reshaped_a = a.reshape(6,9)
reshaped_b = b.reshape(6,9)
reshaped_c = c.reshape(6,9)

print(a)
print(b)
print(c)

print(reshaped_a)
print(reshaped_b)
print(reshaped_c)