import pandas as pd

# Handling Missing Data
# NaN (not a number ) -- missing number 
# None (for object data type)

#  Find Missing data 
# is null -- find None value 

df = pd.read_csv("officeEmployees.csv")
print(df)
# print(df.isnull())
# print(df.isnull().sum())

# Fill the data in place of missing data 
# df.fillna(0, inplace = True)
df["salary"] = df["salary"].fillna(df["salary"].mean()) # don't use inplace 
print(df)



# drop the row of missing data (axis 0 -- drop row of missing value and axis = 1 means column )
# df.dropna(axis = 0 , inplace = True )          # not use always 
# df.loc[8]=df.loc[8].dropna(axis = 0 , inplace = True )
# df.["Age"] = df["Age"].dropa(0)


# print(df)












df = pd.read_csv("officeEmployees.csv")
print(df)

