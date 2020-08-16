# Create a 5x5 array with random values
# Calculate sum in rows, average in column

import numpy as np

a = np.random.random((5, 5))

sum_rows = np.apply_along_axis(np.sum, axis=1, arr=a)
avg_cols = np.apply_along_axis(np.average, axis=0, arr=a)

print('original')
print(a)

print('sum of rows')
print(sum_rows)

print('average of columns')
print(avg_cols)
