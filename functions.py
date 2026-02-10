import pandas as pd

data1 = {
    "Name" : ["Ali", "Sara", "Zara", "Raza", "Ahad", "Fahad", "Minahil", "Fatima"],
    "Rollno." : [101, 102, 103, 104, 105, 106, 107, 108],
}

data2 = {
    "Marks" : [89, 76, 93, 72, 84, 82, 95, 98],
    "Grade" : ["A", "B", "A+", "B", "A","A", "A+", "A+"],
}

df = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

#..................Pandas built-in attributes.......................
# 1. dtypes, to find data type...
print("\n Differents data types of df:\n",df.dtypes) 

# 2. ndim, return no. of dimensions...
print("\nNo. of dimensions: ", df.ndim) 

# 3. size, return no. of elements...
print("\nSize of dataframe: ", df.size)

# 4. shape, return dimensionality of df in tuple form...
print("\nShape of df:", df.shape)

# 5. index, return index...
print("\nIndex of df: ", df.index) 

df1 = pd.DataFrame(data1, index = ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7", "Row8"]) 
print("\nAfter changing the Index of df: ", df1.index) 

# 6. T, transpose of df...
print("\nTranspose of df:\n ", df.T)

#..................Pandas built-in methods.......................
# 1. head(), return first 5 rows (by defualt)...
print("\nHead of df:\n", df.head())

print("\nReturn first 3 rows:\n ", df.head(3)) 

# 2. tail(), return last 5 rows (by default)...
print("\nTail of df:\n", df.tail())

print("\nReturn last 2 rows:\n", df.tail(2))  

# 3. join(), used to join two dataframes...
joindf = df.join(df2)
print("\nJoining two dataframes:\n", joindf)

