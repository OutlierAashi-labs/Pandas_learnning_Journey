#1. *****************--------------------------------------------****************************
'''
1. head 
2. tail

'''

import pandas as pd
df = pd.read_csv("data.csv")

print('Display 10 rows of first')
print (df.head())
# print(df.head(10))

print ('Display 10 rows of last')
print (df.tail())

# print(df.tail(20))


#2   *****************--------------------------------------------**************************

'''
if We want to know

1 number of rows and columns ?

2 column name

3 int62 float 64 object

4 non-null counts

5 memory usage of the dataframe

so we can know these things by info() method

'''

import pandas as pd
df = pd.read_csv("data.csv")
print('Displaying the info of data set')
df.info()
