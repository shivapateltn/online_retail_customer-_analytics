import pandas as pd
df = pd.read_csv("../data/cleaned/feature_data.csv",parse_dates=["InvoiceDate"])
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')

#find first purchase month of each customer
df['cohort_month'] =(df.groupby('CustomerID')['InvoiceMonth'].transform('min'))

print(df[["CustomerID","InvoiceMonth","cohort_month"]].reset_index(drop=True).head(10))

#calculate how many months passed since the customer's first purchase.
df['cohort_index'] = ((df["InvoiceMonth"].dt.year - df["cohort_month"].dt.year) * 12
                      +
                      (df["InvoiceMonth"].dt.month - df["cohort_month"].dt.month) + 1)

print(df[["CustomerID","InvoiceMonth","cohort_month","cohort_index"]]
      .drop_duplicates().sort_values(['CustomerID','InvoiceMonth']).reset_index(drop=True).head(10))

#how many customers returned in each month(count active customers)
cohort_data = (df.groupby(['cohort_month','cohort_index'])
                     ['CustomerID'].nunique().reset_index())

print(cohort_data.head(10))

#cohort table
cohort_table = cohort_data.pivot_table(
    index = 'cohort_month',
    columns = 'cohort_index',
    values = 'CustomerID'
)
cohort_table = cohort_table.fillna(0).astype(int)
print(cohort_table.head())

# customer retention percentage
customer_retention = (cohort_table.divide(cohort_table[1],axis=0) * 100)
print(customer_retention.round(1).head())

customer_retention.to_csv('../data/cleaned/customer_retention.csv',index=True)
cohort_table.to_csv('../data/cleaned/cohort_table.csv',index=True)

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.figure(figsize=(14,8))
customer_retention = customer_retention.replace(0, np.nan)

sns.heatmap(
    customer_retention,
    annot= customer_retention.round(1).astype(str)+ '%',
    fmt='',
    cmap='Blues',
    cbar_kws = {'label': 'customer retention rate (%)'},
    linewidths= 0.5,
    linecolor = 'white',
    mask=customer_retention.isna()
)

plt.title('customer retention heatmap',
          fontsize = 16,
          fontweight = 'bold'),
plt.xlabel('months since first purchase')
plt.ylabel('customer cohort month')
plt.tight_layout()
plt.savefig( "../visualizations/cohort_heatmap.png",bbox_inches='tight')
plt.show()
