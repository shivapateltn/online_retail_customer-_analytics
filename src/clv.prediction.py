import pandas as pd

df = pd.read_csv('../data/cleaned/feature_data.csv')

clv_data = (df.groupby('CustomerID')
            .agg({
            'InvoiceNo':'nunique',
             'total_price':'sum'}).reset_index())

clv_data.columns = ['CustomerID','TotalOrders','TotalRevenue']
print(clv_data.head(10))

#customer lifetime value
#average order value
clv_data['average_order_value'] = (clv_data['TotalRevenue'] / clv_data['TotalOrders'])
#purchase frequency
purchase_frequency =(clv_data['TotalOrders'].sum() / clv_data['CustomerID'].nunique())
# CLV TABLE
clv_data['CLV'] = (clv_data['average_order_value'] * purchase_frequency)
print(clv_data.round(2).head(10))

#top customers by CLV
top_clv_customers = (clv_data.sort_values('CLV', ascending=False).round(2).head(10))
print(top_clv_customers.reset_index(drop=True))

clv_data.to_csv('../data/cleaned/clv_data.csv',index=False)
top_clv_customers.to_csv('../data/cleaned/top_clv_customers.csv',index=False)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

top_clv_customers['CustomerID'] = (top_clv_customers['CustomerID'].astype(int).astype(str))
top_clv_customers['CLV_k'] = (top_clv_customers['CLV'] / 1000)
top_clv_customers_sorted = (top_clv_customers.sort_values(by='CLV_k', ascending=False))

sns.set_theme(style="whitegrid")
plt.figure(figsize=(14,10))

ax = sns.barplot(
    data=top_clv_customers_sorted,
    x='CLV_k',
    y='CustomerID',
    color = 'purple'
)

ticks = ax.get_xticks()
plt.xticks(ticks, [f'{int(t)}k' for t in ticks])

plt.title('Top 10 Customers by Customer life time value', fontsize=14, fontweight='bold')
plt.xlabel('customer life time value', fontsize=11)
plt.ylabel('CustomerID', fontsize=11)
plt.grid(axis='x', linestyle='--', linewidth=1,alpha=0.5)
sns.despine()
plt.tight_layout()
plt.savefig('../visualizations/top_clv_customers.png')
plt.show()