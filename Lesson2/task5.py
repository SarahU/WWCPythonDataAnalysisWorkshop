import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1, usecols=[1,2,3])
print(type(data))

average_marks = np.average(data, axis=1)

plt.bar(range(len(average_marks)), average_marks, align='center')
plt.show()

n, bins, patches = plt.hist(average_marks)
print('n', n)
print('bins', bins)
print('patches', patches)

bins = np.delete(bins, 0)
print('bins', bins)

plt.show()

plt.pie(n, labels=bins)
plt.show()
