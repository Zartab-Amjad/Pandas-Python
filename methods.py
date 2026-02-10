import pandas as pd

data1 = {
    "Name" : ["Ali", "Sara", "Zara", "Raza", "Ahad", "Fahad", "Minahil", "Fatima"],
    "Rollno." : [101, 102, 103, 104, 105, 106, 107, 108],
}

data2 = {
    "Marks" : [89, 76, 93, 72, 84, 82, 95, 98],
    "Grade" : ["A", "B", "A+", "B", "A","A", "A+", "A+"],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("\nDataframe 1:\n", df1)
print("\nDataframe 2:\n", df2)

#..................Pandas built-in methods.......................
# 1. head(), return first 5 rows (by defualt)...
print("\nHead of df:\n", df1.head())

print("\nReturn first 3 rows:\n ", df1.head(3)) 

# 2. tail(), return last 5 rows (by default)...
print("\nTail of df:\n", df1.tail())

print("\nReturn last 2 rows:\n", df1.tail(2))  

# 3. join(), used to join two dataframes...
joindf = df1.join(df2)
print("\nJoining two dataframes:\n", joindf)

# 4. concat(), concatenate content of 2 dfs...
data3 = {
    "Id" : [1, 2, 3, 4, 5],
    "Name" : ["Jonh", "Tom", "Maria", "Sara", "David"]
}

data4 = {
    "Id" : [6, 7, 8],
    "Name" : ["Dove", "Merry", "Sam"]
}

df3 = pd.DataFrame(data3, index = ["St1", "St2", "St3", "St4", "St5"])
df4 = pd.DataFrame(data4, index = ["St6", "St7", "St8"]) 

print("\nDataframe 3:\n", df3)
print("\nDataframe 4:\n", df4)

concat = pd.concat([df3, df4]) 
print("Concatenate df3 & df4:\n", concat)

