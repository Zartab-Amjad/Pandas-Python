import pandas as pd

data = {
    "Name" : ["Ali", "Sara", "Zara", "Raza", "Ahad"],
    "Marks" : [89, 76, 93, 72, 81]
}

df = pd.DataFrame(data)

print("Show records:\n", df) 

#Change index..............
df = pd.DataFrame(data, index = ["Row1", "Row2", "Row3"])
print(f"DataFrame: \n {df}") 