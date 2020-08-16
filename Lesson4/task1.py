# 1. Download toy dateset wine
# 2. Normalize columns with 2 different ways

import numpy as np
from sklearn import datasets
from sklearn import preprocessing

wine_X, wine_y = datasets.load_wine(return_X_y=True)

print('Normalised 1')
scalar = preprocessing.MinMaxScaler()
scalar.fit(wine_X, wine_y)
wine_data_norm_1 = scalar.transform(wine_X)
print(wine_data_norm_1)

print('Normalised 2')
scaler = preprocessing.StandardScaler()
scalar.fit(wine_X, wine_y)
wine_data_norm_2 = scalar.transform(wine_X)
print(wine_data_norm_2)
