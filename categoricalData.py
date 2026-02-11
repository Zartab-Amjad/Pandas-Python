import pandas as pd 
from pandas.api.types import CategoricalDtype

# Categorical series...
s = pd.Series(data = ["p",8, "q", "r",6, "s"], dtype = "category") 
print("Categorical series:\n",s) 

# # Categorical Dataframe....................
# # by using dtype...
df = pd.DataFrame(data = {
    "cat1" : list("pqrs"),
    "cat2" : list("pqst"),
    "cat3" : list("prst"),
}, dtype = "category")
print("\nCategorical Dataframe:\n",df)

# # by astype...
df1 = pd.DataFrame({
    "gender" : ["male", "female", "male"]
})
df1["gender"] = df1["gender"].astype("category")
print("Categical Dataframe by using astype: \n", df1) 

print("\nData type:",df1.dtypes) 

# with defined categories and ordering...
df2 = pd.DataFrame({
    'size': ['medium', 'small', 'large']
})

size_type = CategoricalDtype(categories=['small', 'medium', 'large'], ordered=True)
df2['size'] = df2['size'].astype(size_type) 
print("\nCategorical dataframe with Categorical Dtype:\n",df2) 
print("\nData type:", df2.dtypes) 

# Append new category...
s = pd.Series(data = ["p", "q", "r"], dtype = "category")
s_add = s.cat.add_categories("s")
print("\nAppend new category:\n",s_add) 

# remove category...
s_remove = s.cat.remove_categories("q")
print("\nAfter removing a category:\n", s_remove)

# rename category...
s = s.cat.rename_categories(["b", "c", "a"]) 
print("\nRename the category:\n", s) 
 
# reordering the cteogory...
s = s.cat.reorder_categories(["a", "b", "c"], ordered=True)
print("\nReording the category:\n", s)  


