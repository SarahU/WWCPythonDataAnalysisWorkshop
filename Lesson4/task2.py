# 1. Generate sample for regression analysis with 50 observations
# 2. Calculate coefficients for the model
# 3. Validate the model


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

wine_X, wine_y = datasets.load_wine(return_X_y=True)
# Use only one feature
wine_X = wine_X[:, np.newaxis, 2]

#only want 50 observations
wine_X = wine_X[:50]
wine_y = wine_y[:50]

#split training and test
wine_X_train = wine_X[:-10]
wine_X_test = wine_X[-10:]
wine_y_train = wine_y[:-10]
wine_y_test = wine_y[-10:]

# Create linear regression object
regr = linear_model.LinearRegression()
# Train the model using the training sets
regr.fit(wine_X_train, wine_y_train)
# Make predictions using the testing set
wine_y_pred = regr.predict(wine_X_test)

# Plot outputs
plt.scatter(wine_X_test, wine_y_test, color='black')
plt.plot(wine_X_test, wine_y_pred, color='purple', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()


# 2. Calculate coefficients for the model
print('Coefficients: \n', regr.coef_)

# 3. Validate the model
# The mean squared error
print('Mean squared error: %.2f'
% mean_squared_error(wine_y_test, wine_y_pred))


