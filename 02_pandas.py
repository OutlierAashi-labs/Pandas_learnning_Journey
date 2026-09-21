#3 *****************--------------------------------------------*******************

'''            
Describe method
'''

# Describe method
import pandas as pd
df = pd.read_csv("data.csv")
print("Descriptive Statistics")
print(df.describe())



#4 *****************--------------------------------------------*******************

'''
1) How big is your dataset
2) What are the names of column

Shape and columns
'''

import pandas as pd
df = pd.read_csv("data.csv")
print(df)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')

#5 *****************--------------------------------------------*******************

'''
1) How to select specific column
2) How to filter rows on specific condition
3) combine multiple conditions
'''

import pandas as pd

#1 How to select specific column

# Selecting single column
see = pd.read_csv("data.csv")
print("names (single column return series)")
print(df["name"])

# selecting multiple column
subset = df[["name","price"]]
print('\nSubset with name and price')
print(subset)

#2 How to filter rows on specific condition

# filter rows on single condition
high_price = df[df['price'] > 1000]
print('\nHigh price > 700')
print(high_price)

# filter rows on multiple conditions

# using And condition
filtered = df[(df['price'] > 700) & (df['category'] == 'Home & Kitchen')]
print(f'High price > 700 + category = Home & Kitchen')
print(filtered)

# using OR condition
filtered_or = df[(df['price'] > 700) | (df['category'] == 'Home & Kitchen')]
print('High price > 700 or category = Home & Kitchen')
print(filtered_or)





