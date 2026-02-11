import pandas as pd
import numpy as np

data1 = [10, 20, 5, 78, 9]

s1 = pd.Series(data1, index = ["Num1", "Num2", "Num3", "Num4", "Num5"])

print("Series:\n", s1)

#..............Built-in attributes of series...............
# 1. dtpye, return data ttype...
print("\nData type of series: ", s1.dtype)

# 2.ndim...
print("\nNo. of dimensions: ", s1.ndim) 

# 3. size, return no. of elements...
print("\nSize of dataframe: ", s1.size)

# 4. name, return name of series...
data2 = ['a', 'b', 'c', 'd', 'e']

s2 = pd.Series(data2, name = "Alphabetic series")
print("\nName of series1 is ",s1.name) 
print("\nName of series2 is ",s2.name) 

# 5. hasnans, return true if series has NaN value...
data3 = [7, 9, 34, np.nan, 52] 
s3 = pd.Series(data3, index = ["odd1", "odd2", "odd3", "odd4", "odd5"])

print("\nSeries1 has NaN value: ",s1.hasnans)
print("\nSeries2 has NaN value: ",s2.hasnans)
print("\nSeries3 has NaN value: ",s3.hasnans)            #return true

# 6. index, return index...
print("\nIndices of series1: \n", s1.index)
print("\nIndices of series2: \n", s2.index)
print("\nIndices of series3: \n", s3.index)

