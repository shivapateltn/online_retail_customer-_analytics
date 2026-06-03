import pandas as pd

#load feauture enginerred data
df = pd.read_csv('../data/cleaned/feature_data.csv')



#which countries generate highest revenues?
#revenue by country
country_revenue = df.groupby('Country')['total_price'].sum()

#highest revenue
country_revenue = country_revenue.sort_values(ascending=False)
print(country_revenue.head(10))

#revenue by customer
customer_revenue = df.groupby(['CustomerID','Country'])['total_price'].sum()
customer_revenue = customer_revenue.sort_values(ascending=False)
print(customer_revenue.head(10))

#monthly revenue
monthly_revenue = (df.groupby('month')['total_price'].sum().reset_index(name='revenue'))

print("\nmonthly revenue")
print(monthly_revenue.head(10))


#top products by revenue
product_revenue = df.groupby('Description')['total_price'].sum()
product_revenue = product_revenue.sort_values(ascending=False)
print("\nTop revenue generating products")
print(product_revenue.head(10))

#top products by quantity
product_quantity = df.groupby('Description')['Quantity'].sum()
product_quantity = product_quantity.sort_values(ascending=False)
print("\nTop quantity sold products")
print(product_quantity.head(10))

#comparing products by revenue and quality
product_compare = df.groupby('Description')[['Quantity','total_price']].sum()
product_compare = product_compare.sort_values(by='total_price',ascending=False)
print("\nTop quantity sold products compared with revenue")
print(product_compare.head(10))

#repeated customers
repeated_customers = df.groupby('CustomerID')['InvoiceNo'].nunique()
repeated_customers = repeated_customers.reset_index(name='purchases')
repeated_customers = repeated_customers.sort_values(by='purchases',ascending=False)
repeated_customers = repeated_customers.reset_index(drop=True)
print("\nTop repeated customers")
print(repeated_customers.head(10))

#highest and lowest sales month
highest_month = monthly_revenue.idxmax()
lowest_month = monthly_revenue.idxmin()

print("\nhighest monthly revenue:", highest_month)
print("revenue:", monthly_revenue.max())
print("lowest monthly revenue:", lowest_month)
print("revenue:", monthly_revenue.min())

#average monthly order value
avg_monthly_value = df.groupby('month')['total_price'].mean()
highest_avg_month = avg_monthly_value.idxmax()
print("\nhighest average monthly revenue:", highest_avg_month)
print("average order value:", avg_monthly_value.max())

#average order value by country
avg_country_order = df.groupby('Country')['total_price'].mean()
avg_country_order = avg_country_order.reset_index(name='average values')
avg_country_order = avg_country_order.sort_values(by='average values',ascending=False)
avg_country_order = avg_country_order.reset_index(drop=True)
print("\nTop countries by average order value")
print(avg_country_order.head(10))

#top customer contribution
top_customers = df.groupby('CustomerID')['total_price'].sum()
top_customers = top_customers.sort_values(ascending=False)

top10_customers = top_customers.head(10).sum()
total_revenue = df['total_price'].sum()

contribution = (top10_customers/total_revenue) * 100
print("\nTop 10 customers with high contribution (%)")
print(f"{round(contribution,1)}%")

#high revenue low quality products
high_value_products = df.groupby('Description')[['Quantity','total_price']].sum()
high_value_products = high_value_products.sort_values(by='total_price',ascending=False)
high_value_products = high_value_products[
high_value_products['Quantity'] < high_value_products['Quantity'].median()]
print("\nHigh revenue but low quantity products")
print(high_value_products.head(10))

#rarely sold products
rare_products = df.groupby('Description')['Quantity'].sum()
rare_products = rare_products.sort_values(ascending=True)
print("\nRarely sold products")
print(rare_products.head(10))

import matplotlib.pyplot as plt
import seaborn as sns

#set theme
sns.set_theme(style='whitegrid')

plt.figure(figsize=(13,6))

sns.lineplot(data=monthly_revenue,x='month',y='revenue',marker='o',linewidth=3,color='purple')

#fill area under line
plt.fill_between(monthly_revenue['month'],monthly_revenue['revenue'],alpha=0.2,color='purple')

plt.title('Monthly Revenue Trend',fontsize=18,fontweight='bold',pad=15)
plt.xlabel('Month',fontsize=12)
plt.ylabel('Revenue',fontsize=12)
plt.xticks(rotation=45)

plt.grid(linestyle='--',alpha=0.4)
sns.despine()
plt.ticklabel_format(style='plain',axis='y')
plt.tight_layout()
plt.savefig('../visualizations/monthly_revenue_trend.png')

plt.show()