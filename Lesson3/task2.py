# 1. Create DataFrame from dictionary
# 2. Apply method
# def doubler(x):
#    if x % 2 == 0:
#        return x
#    else:
#        return x * 2
# to any numeric column
import pandas as pd


def odd_doubler(x):
    if x % 2 == 0:
        return x
    else:
        return x * 2


data = {'row1': [234, 6456, -349, 565],
        'row2': [-34, -433, 900, 85],
        'row3': [4555, 56, -12, 9]
        }

frame = pd.DataFrame(data)

print('Original')
print(frame)

# doubled_frame = original_frame.applymap(odd_doubler)
frame['row1'] = frame['row1'].apply(lambda x: odd_doubler(x))

print('Row 1 Odd numbers Doubled')
print(frame)