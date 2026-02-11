import pandas as pd

data = {
    "Name" : ["Ali", "Sara", "Zara", "Raza", "Ahad", "Fahad", "Minahil", "Fatima"],
    "Rollno." : [101, 102, 103, 104, 105, 106, 107, 108],
}

df = pd.DataFrame(data)
print("Dataframe:\n", df)

#..................Pandas built-in attributes of dataframes.......................
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

df1 = pd.DataFrame(data, index = ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7", "Row8"]) 
print("\nAfter changing the Index of df: ", df1.index) 

# 6. T, transpose of df...
print("\nTranspose of df:\n ", df.T)

