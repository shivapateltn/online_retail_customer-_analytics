import pandas as pd

# load online retail datasheet
df = pd.read_excel("../data/raw/Online Retail.xlsx")

print(df.head())

#dataset dimensions
print("\ndataset shape")
print(df.shape)

#column names
print("columns")
print("\ncolumns")
print(df.columns)

#datatypes
print("\ndatatypes")
print(df.dtypes)

#missing values
print("\nmissingvalues")
print(df.isnull().sum())