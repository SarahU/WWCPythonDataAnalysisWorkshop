# 4.1 Create a structured array representing a position (x,y) and a color (r,g,b)
import numpy as np

x = 1
y = 2
r = 25
g = 57
b = 90

position = np.dtype ([
    ('x', np.int16),
    ('y', np.int16)
])
color = np.dtype ([
    ('r', np.int32),
    ('g', np.int32),
    ('b', np.int32)
])

element1 = ((2,3),(234,345,456))
element2 = ((5,6),(357,135,680))

dots = np.array([element1, element2],
                dtype=[('pos', position),('col', color)])

print(dots)

# 4.2 Consider a 16x16 array, how to get the block-sum (block size is 4x4)
a = np.random.random(256)
a = a.reshape(16, 16)

print('Original')
print(a)

block_size = 4
blocks = np.add.reduceat(np.add.reduceat(a,
                                         np.arange(0, a.shape[0], block_size), axis=0),
                                         np.arange(0, a.shape[1], block_size), axis=1)

print('Block Sum')
print(blocks)