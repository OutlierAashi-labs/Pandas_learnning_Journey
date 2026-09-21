import pandas as pd 

df = pd.read_csv("officeEmployees.csv")

# print(df)


# 1) Adding Columns

# 1) using Assigment -- not any specific location
# Square brackcets df["Column_Name"] = some_Data

df["Bonus"] = df['salary'] * 0.1
# print(df)

# 2) Using Insert Method() -- specific location 
# loc = location 
# df.insert(loc, "Column_Name", some_data)
df.insert(0, "Employee ID",[10,20,30,40,50,60,70,80,90,100])
# print(df)

df = pd.read_csv("officeEmployees.csv")
# print(df)



# 2) Updating columns

# .loc[] -- it is a method to excess or modify a specific cell , roll , column etc  
# df.loc[row_index, "Column Name"] = new_value
df.loc[4, 'salary'] = 95000
# print(df)

# increasing salary by 5%
df['salary'] = df['salary'] * 1.05
# print(df)



# 3) Removing 

# df.drop(columns = ["ColumnName1", "ColumnName2"] , inplace = True)
df.drop(columns = ["age"], inplace=True)
print(df)


# 


df = pd.read_csv("officeEmployees.csv")
print(df)

# 
