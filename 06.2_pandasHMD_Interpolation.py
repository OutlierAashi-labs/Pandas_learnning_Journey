import pandas as pd 
df = pd.read_csv("officeEmployees.csv")
print(df)

# linear interpolation 
# polynomial interpolation 
# time interpolation 

# why use interpolation
# 1 - preserve data integrity
# 2 - smooth trends 
# 3 - avoid data loss


# df.interpolate(method="linear",axis=0)
# df["Age"] = df["Age"].interpolate(method="linear")

'''

 It use in 

1- time series data 
2 - numeric data with trends
3-  avoid dropping rows

It doesn't use in 

Categorical data like name , id etc 

'''
