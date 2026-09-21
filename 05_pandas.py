# 1) loc
# loc row aur column ke naam se data nikalta hai.
# loc → Label (name/index) se select karta hai.

# 2) iloc
# iloc → Position (0, 1, 2, ...) se select karta hai.
# iloc position se data select karta hai.


import pandas as pd
df = pd.read_csv("officeEmployees.csv")

print(df.loc[0])

print(df.loc[:, "name"])

print(df.loc[1, "salary"])

print(df.loc[0:2])



print('iloc start')

# print(df.iloc[0])

print(df.iloc[0,1])
print(df.iloc[0:2])

print(df.iloc[0:2, 0:3])
print(df.iloc[0:1, 0:3])
print(df.iloc[0:1, 0:2])
