import pandas as pd

#.......................Dataframe............................
# create dataframe...
data = {
    "Name" : ["Ali", "Sara", "Zara", "Raza", "Ahad"],
    "Marks" : [89, 76, 93, 72, 81]
}

df = pd.DataFrame(data)

print("Show records:\n", df) 

#Change index...
df = pd.DataFrame(data, index = ["Row1", "Row2", "Row3", "Row4", "Row5"]) 
print(f"\nDataFrame after changing index: \n {df}") 

#Access rows or cols...
print("\nAccessing row2:\n",df.loc["Row2"])  

#Acess specific values of key...
print("\nName of first row:", df.loc["Row1", "Name"])
print("Marks of first row:", df.loc["Row1", "Marks"]) 

#Access values by integers...
print("\nAccess row 4 and 5\n",df.iloc[[3,4]])


#.......................................Series...............................
# create series...
data = [10, 20, 30, 40]

s = pd.Series(data)

print("Series:\n", s)

# access values...
print("\nValue at index 2:", s[2])

# change index ...
s1 = pd.Series(data, index = ["Num1", "Num2", "Num3", "Num4"])
print("\nSeries after changing the index:\n", s1)

# access value with label (custom index)...
print("\nAccess value of Row3 by label:",s1["Num3"])
