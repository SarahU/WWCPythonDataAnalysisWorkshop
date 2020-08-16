# https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv
# http://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv
# http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls
# https://raw.githubusercontent.com/Grossmend/CSV/master/cars93/Cars93_missing.csv
#
#  Read   file and  transfer it into DataFrame

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv')
df2 = pd.read_csv('http://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv')
df3 = pd.read_excel('http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls')
df4 = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/cars93/Cars93_missing.csv')

print(df1)
print(df2)
print(df3)
print(df4)
