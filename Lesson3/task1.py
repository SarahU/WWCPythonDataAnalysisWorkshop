# Transfer  object Series into index column of the dataframe
# Change the data in the column of DataFrame according to some condition

import pandas as pd

data = [12,-34,232,-23,]
s = pd.Series(['a', 'b', 'c', 'd'])

original_frame = pd.DataFrame(data, index=s)

new_frame = original_frame.isin([12,232])
print(new_frame)