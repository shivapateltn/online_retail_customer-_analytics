import pandas as pd

df = pd.read_csv("../data/cleaned/feature_data.csv")

#converting invoicedate to datetime (recency)

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
today = df['InvoiceDate'].max()
print(today)

#recency calculation
recency = df.groupby('CustomerID')['InvoiceDate'].max()
recency = (today - recency).dt.days
recency = recency.reset_index(name='days')
recency = recency.sort_values(by='days',ascending=True)
recency = recency.reset_index(drop=True)
print("\nCustomer recency")
print(recency.head(10))

#frequency calculation
frequency = df.groupby('CustomerID')['InvoiceNo'].nunique()
frequency = frequency.reset_index(name='frequency')
frequency = frequency.sort_values(by='frequency',ascending=False)
frequency = frequency.reset_index(drop=True)
print("\nCustomer frequency")
print(frequency.head(10))

#monetary calculation
monetary = df.groupby('CustomerID')['total_price'].sum()
monetary =monetary.reset_index(name='monetary')
monetary = monetary.sort_values(by='monetary',ascending=False)
monetary = monetary.reset_index(drop=True)
print("\nMonetary price")
print(monetary.round(2).head(10))

#combine rfm tables
rfm = recency.merge(frequency, on='CustomerID')
rfm = rfm.merge(monetary, on='CustomerID')
print("\nRFM TABLE")
print(rfm.head(10))

#R score
rfm['R_score'] = pd.qcut(rfm['days'],5,labels=[5,4,3,2,1])

#F score
rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'),5,labels=[1,2,3,4,5],duplicates='drop')

#M score
rfm['M_score'] = pd.qcut(rfm['monetary'],5,labels=[1,2,3,4,5])

print("\nRFM SCORES")
print(rfm.head(10))

#combining scores
rfm['RFM_score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)
print("\nRFM score merge table")
print(rfm.head(10))

#CUSTOMER SEGMENTS
rfm['segment'] = 'Regular'
rfm.loc[rfm['RFM_score'].str.startswith('5'),'segment'] = 'Loyal'
rfm.loc[rfm['RFM_score'].str.startswith('1'),'segment'] = 'At Risk'
rfm.loc[rfm['RFM_score']=='555','segment'] = 'VIP'

print("\ncustomer segments")
print(rfm[['CustomerID','RFM_score','segment']].round(2).head(10))

#count customer segments
segment_count = rfm['segment'].value_counts()
segment_count = segment_count.reset_index(name='count')
print("\ncustomer segment count")
print(segment_count)

rfm.to_csv('../data/cleaned/rfm_data.csv',index=False)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12,8))
ax = sns.barplot(
    data = segment_count,
    x = 'segment',
    y ='count',
    hue = 'segment',
    palette = 'viridis',
    legend = False
)

plt.title('Customer Segment Distribution',fontsize=18,fontweight='bold')
plt.ylabel('Count',fontsize=14)
plt.xlabel('Segment',fontsize=14)
for container in ax.containers:
    ax.bar_label(container)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.grid(axis='y',linestyle='-',linewidth=0.5,alpha=0.5,color='black')
sns.despine()
plt.tight_layout()
plt.show()