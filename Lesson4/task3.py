# For task 1 Use Multi Layer Perceptron for classification

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
data = datasets.load_wine()
print(data)
df = pd.DataFrame(data.data, columns=data.feature_names)
df['class']=data.target
print(df.iloc[:,0:4])
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,0:4],df['class'],test_size=0.35, random_state=42)
clf = MLPClassifier(random_state=1, max_iter=100).fit(X_train, y_train)
print(clf.predict(X_train[0:4]))
print(clf.score(X_test, y_test))
