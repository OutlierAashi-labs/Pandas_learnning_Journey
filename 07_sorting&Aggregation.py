'''

1. sorting data
arrange in order 
Sorting Data 1 column sort_value()

df.sort_value(by="ColumnName", ascending=True/False)

df.sort_value(by=["ColumnName1","ColumnName2"], ascending=[True,False])

2. Aggregation data 
* Summary
df["ColumnName"].mean()
df["ColumnName"].median()
df["ColumnName"].max()
df["ColumnName"].min()
df["ColumnName"].sum()
df["ColumnName"].mode()
df["ColumnName"].std()
df["ColumnName"].count()


grouped = df.groupby("Age")["Salary"].sum()
grouped = df.groupby(["Age" ,"Name"])["Salary"].sum()



'''