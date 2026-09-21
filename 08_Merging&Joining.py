'''
1. Merging
# type of join  
a inner 
b outer 
c left 
d right 
e 

pd.merge(df1, df2, on="column_Name", how="type of join")


1df = m rows 
2df = n rows
m*n rows


2. Concatenation 

Vertically (row-wise)
horizontally (column wise)

pd.concate([df1, df2],axis=0 , ignore_index=True)   
 # axis = 0 ( row wise ) -- Concatenate Vertically  
 # axis = 1 (column wise) -- Concatenate Horizontally
 
 
'''