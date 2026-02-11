import pandas as pd

data1 = [10, 20, 30, 40, 50, 60, 70]

s1 = pd.Series(data1, name = "Numbers")
print("Pandas seires:\n", s1)

# ..........................Built-in methods of series.............................
# 1. head(), return top 5 rows by default...
print("\nHead of series:\n", s1.head()) 
print("\nHead of series with 3 rows:\n", s1.head(3))

# 2. tail(), return last 5 rows by default...
print("\nTail of series:\n", s1.tail())
print("\nTail of series with last 3 rows:\n", s1.tail(3))

# 3. info(), display summary of series...
print("\nInfo of series 1:\n")
print(s1.info()) 

# 4. combine(), combine 2 series with specific function...
# example 1:
data2 = [3, 89, 56, 23, 11, 99, 7]
s2 = pd.Series(data2)

def demo(x1, x2):
    if (x1 > x2):
        return x1
    else:
        return x2
    
res = s1.combine(s2, demo)
print("\nGreater value by comparing two series: \n", res) 

# example 2:
s3 = pd.Series({'a':1, 'b':2, 'c':3, 'd':4})
s4 = pd.Series({'b':5, 'c':6, 'd':7, 'e':8}) 

def demo2(val1, val2):
    return max(val1, val2)

res2 = s3.combine(s4, demo2, fill_value=0)
print("\nMax of values by combinig two series:\n", res2) 


