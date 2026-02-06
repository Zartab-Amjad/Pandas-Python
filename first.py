import pandas as pd

data = {
    "Name" : ["Ali", "Sara", "Zara", "Raza", "Ahad"],
    "Marks" : [89, 76, 93, 72, 81]
}

df = pd.DataFrame(data)

print("Show records:\n", df) 

#Change index..............
df = pd.DataFrame(data, index = ["Row1", "Row2", "Row3", "Row4", "Row5"]) 
print(f"\nDataFrame after changing index: \n {df}") 

#Access rows or cols.........
print("\nAccessing row2:\n",df.loc["Row2"])  

#Acess specific values of key............
print("\nName of first row:", df.loc["Row1", "Name"])
print("Marks of first row:", df.loc["Row1", "Marks"]) 
