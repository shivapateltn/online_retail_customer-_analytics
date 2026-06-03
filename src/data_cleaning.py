import  pandas as pd

#load dataset
df = pd.read_excel("../data/raw/Online Retail.xlsx")

print("\nbefore cleaning")
print(df.shape)

#removing missing values
df = df.dropna(subset=['CustomerID'])

#after cleaning
print("\nafter cleaning")
print(df.shape)

invoice_check = df['InvoiceNo'].astype(str).str.startswith('C')
print(invoice_check.head(10))
df = df[~invoice_check]

print("\nAfter removing cancelled transactions")
print(df.shape)

#checking nagative quantities
nagative_quantity = df[df['Quantity']< 0 ]

print("\nNagative quantity transactions")
print(nagative_quantity.shape)

print("\nSample nagative transactions")
print(nagative_quantity.head())

#checking duplicate rows
duplicate_rows = df.duplicated()
print("\nDuplicated rows")
print(duplicate_rows.sum())

#display duplicated rows
print("\nsample duplicated rows")
print(df[duplicate_rows].head(10))

#show full duplicate roes
print(df[df.duplicated()].iloc[0])

df = df.drop_duplicates()
print("\nduplicated rows")
print(df.shape)

#checking stock codes for suspicious products
alphabet_stock = df[df["StockCode"].astype(str).str[0].str.isalpha()]
print(alphabet_stock['StockCode'].unique())

print(df[df["StockCode"]== "PADS"][['StockCode','Description','Quantity',]].drop_duplicates())

#removing non stock codes
df = df[~df['StockCode'].isin(['POST', 'C2', 'M', 'BANK CHARGES', 'PADS', 'DOT'])]
print(df.shape)

#save cleaned data
df.to_csv("../data/cleaned/cleaned_retail.csv",index=False)

print("\ncleaning complete")
print(df.shape)

