import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/cleaned/cleaned_retail.csv")


# Create total transaction value
df['total_price'] = ( df['Quantity']*df['UnitPrice'])

print("\nSample Total Prices")
print(df[['Quantity','UnitPrice','total_price'] ].head())


# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# Create month column
df['month'] = (df['InvoiceDate'].dt.to_period('M'))

print("\nSample Month Values")
print(df[['InvoiceDate','month']].head())

#round total_price to 2 decimal places
df['total_price'] = df['total_price'].round(2)


# Save feature engineered data
df.to_csv("../data/cleaned/feature_data.csv",index=False)

print("\nFeature engineering complete")
print(df.shape)
print(df.columns.tolist())