# Get names of the DataFrame columns and sum of losted values  DF
# Replay ( Apply) missed values in the Column with average values.
# Calculate basic statistics for 2 columns
# For any column create histogram
# Create Linear Regression plot for 2 column

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

frame = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv')
# print(frame)

print('Columns')
column_names = frame.corr().columns
print(column_names)

mean_frame = frame.mean()

# #fill NAs
frame = frame.fillna(value=mean_frame)
print(frame)


# basic stats
print(frame.describe())
print(frame.corr())

# histogram
plt.hist(frame['Age'])
plt.show()

#linear regression

plt.figure(figsize=(10,15))
ax = sns.regplot(x='Age', y='Fare', data=frame, color='purple')
plt.show()