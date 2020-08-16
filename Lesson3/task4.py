# Delete upper and lowe 5% in object DataFrame - NOT DONE
# Create two data frames using the two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.

import pandas as pd
#1 - NOT DONE

#2
dict1 = {
    'i  dx': [1,2,3,4],
    'col1': [43, 564, 453, 234],
    'col2': [767, 32, 1, 785],
    'col3': [6763, 2, 234, 456]
}

dict2 = {
    'idx': [6],
    'col1': [12]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print('Merge')
merged = pd.merge(df1, df2, 'outer', left_on='idx', right_on='idx')
print(merged)

print('Append')
appended = df1.append(df2)
print(appended)

print('Contacted')
contacted = pd.concat([df1, df2])
print(contacted)
