#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings ## used to ignore warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv(r'C:\Users\MBR\Downloads\DATA SCIENCE\archivee\Sample - Superstore.csv', encoding='windows-1252')


# In[4]:


# Set the maximum number of columns to display
pd.options.display.max_columns = None

# Set the maximum number of rows to display
pd.options.display.max_rows = None


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.info()


# In[8]:


df.isna().sum()


# In[9]:


df.describe()


# In[10]:


# what about duplication 
df.duplicated().sum()


# In[11]:


df_cat = df[[ 'Ship Mode', 'Customer ID', 'Customer Name',
             'Segment', 'Country', 'City', 'State', 'Region',
             'Product ID', 'Category', 'Sub-Category', 'Product Name']]


# In[12]:


df_cat.head()


# In[13]:


# shown the number of unique values in categorical data
for feature in df_cat.columns:
    print(feature,':',df[feature].nunique())


# In[14]:


df['Order Date'].nunique()


# In[15]:


df['Ship Date'].nunique()


# In[16]:


#What are the top selling products in the superstore?
# Group the data by Product Name and sum up the sales by product
product_group = df.groupby(["Product Name"]).sum()["Sales"]


# In[17]:


product_group.head()


# In[18]:


# Sort the data by sales in descending order
top_selling_products = product_group.sort_values(ascending=False)


# In[19]:


top_5_selling_products = pd.DataFrame(top_selling_products[:5])


# In[20]:


top_5_selling_products


# In[21]:


top_5_selling_products.plot(kind="bar")

# Add a title to the plot
plt.title("Top 5 Profit Products in Superstore")

# Add labels to the x and y axes
plt.xlabel("Product Name")
plt.ylabel("Total Profit")

# Show the plot
plt.show()


# In[23]:


#top-profitable products 
product_group = df.groupby(["Product Name"]).sum()["Profit"]

top_profit_products = product_group.sort_values(ascending=False)

top_5_profit_products =pd.DataFrame(top_profit_products[:5])
top_5_profit_products


# In[24]:


top_5_profit_products.plot(kind="bar")

plt.title("Top 5 Profit Products in Superstore")

plt.xlabel("Product Name")
plt.ylabel("Total Profit")

plt.show()


# In[26]:


#Are the top-selling products the most profitable?
top_5_profit_products.index


# In[27]:


top_5_profit_products.index==top_5_selling_products.index


# In[28]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,5))

# Plot the top 5 selling products in the first column
top_5_selling_products.plot(kind="bar", y="Sales", ax=ax1)

# Set the title for the first plot
ax1.set_title("Top 5 Selling Products")

# Plot the top 5 profit products in the second column
top_5_profit_products.plot(kind="bar", y="Profit", ax=ax2)

# Set the title for the second plot
ax2.set_title("Top 5 Profit Products")

# Show the plot
plt.show()


# In[29]:


list(top_5_profit_products.index)


# In[31]:


"""
Now we can conclude some things
top_5_selling_products:
- Canon imageCLASS 2200 Advanced Copier
- Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind
- Cisco TelePresence System EX90 Videoconferencing Unit
- HON 5400 Series Task Chairs for Big and Tall
- GBC DocuBind TL300 Electric Binding System

top_5_profit_products:
- Canon imageCLASS 2200 Advanced Copier
- Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind
- Hewlett Packard LaserJet 3310 Copier
- Canon PC1060 Personal Laser Copier
- HP Designjet T520 Inkjet Large Format Printer - 24

The highest selling products, and the most profitable
- Canon imageCLASS 2200 Advanced Copier
- Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind
"""


# In[33]:


df.Region.value_counts()


# In[34]:


import matplotlib.pyplot as plt

# Filter the data to only include the Canon imageCLASS 2200 Advanced Copier
product = df[df["Product Name"] == "Canon imageCLASS 2200 Advanced Copier"]

# Group the data by Region and calculate the mean of Sales and Profit
region_group = product.groupby("Region")[["Sales", "Profit"]].mean()

# Plotting
region_group.plot(kind="bar")
plt.title('Average Sales and Profit by Region for Canon imageCLASS 2200 Advanced Copier')
plt.ylabel('Average Value')
plt.xlabel('Region')
plt.show()


# In[35]:


# Filter the data to only include the specific product
product = df[df["Product Name"] == "Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind"]

# Group the data by Region and calculate the mean of Sales and Profit
region_group = product.groupby("Region")[["Sales", "Profit"]].mean()

# Plot the average sales and profit by region
region_group.plot(kind="bar", figsize=(10, 6), color=['skyblue', 'lightgreen'])

# Adding title and labels
plt.title('Average Sales and Profit by Region for Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind')
plt.xlabel('Region')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.legend(title='Metrics')

# Show the plot
plt.tight_layout()
plt.show()


# In[36]:


product = df[(df["Product Name"] == "Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind") & (df["Region"] == "Central")]
product


# In[37]:


product = df[(df["Product Name"] == "Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind") & (df["Region"] == "Central")]

# Plot a histogram of the discounts offered for the product in the central region
product["Discount"].plot(kind="bar")

# Show the plot
plt.show()


# In[39]:


# What is the sales trend over time (monthly, yearly)?
df['Order Date'] = pd.to_datetime(df['Order Date'])
monthly_sales = df.groupby(['Order Date'], as_index=False).sum()

# Set the Order Date column as the index of the dataframe
monthly_sales = monthly_sales.set_index('Order Date')

# Resample the data into monthly intervals
monthly_sales = monthly_sales.resample('M').sum() # M for month

# Plot
plt.figure(figsize=(25,8))
plt.plot(monthly_sales['Sales'])
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()


# In[40]:


yearly_sales = monthly_sales.resample('Y').sum() 


plt.figure(figsize=(25,8))
plt.plot(yearly_sales['Sales'])
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.title("yearly Sales Trend")
plt.show()


# In[41]:


monthly_sales = df.groupby(['Order Date'], as_index=False).sum()

# Set the Order Date column as the index of the dataframe
monthly_sales = monthly_sales.set_index('Order Date')

# Resample the data into monthly intervals
monthly_sales = monthly_sales.resample('M').sum() # M for month

# Plot
plt.figure(figsize=(25,8))
plt.plot(monthly_sales['Profit'])
plt.xlabel("Order Date")
plt.ylabel("Profit")
plt.title("Monthly Profit Trend")
plt.show()


# In[42]:


# Which region & place generates the most sales?


# In[43]:


df_places = df[['Country','City','State','Region']]
df_places.head()


# In[44]:


for place in df_places.columns:
    print(place,':',df_places[place].nunique())


# In[46]:


df_places = df[['City','State','Region','Sales','Profit']]
df_places.head()


# In[47]:


# Group the data by Region and City and calculate the total sales for each group
grouped_data = df_places.groupby(['Region'], as_index=False).sum()
grouped_data.sort_values(by='Sales', ascending=False, inplace=True)

# Plot the total sales geProfitnerated by each region and city
plt.figure(figsize=(10,5))
plt.bar(grouped_data['Region'], grouped_data['Sales'], align='center',)
plt.xlabel("Region")
plt.ylabel("Sales")
plt.title("Sales Generated by State")
plt.xticks(rotation=90)

plt.show()


# In[48]:


# Group the data by Region and City and calculate the total sales for each group
grouped_data = df_places.groupby(['Region'], as_index=False).sum()
grouped_data.sort_values(by='Profit', ascending=False, inplace=True)

# Plot the total sales generated by each region and city
plt.figure(figsize=(10,5))
plt.bar(grouped_data['Region'], grouped_data['Profit'], align='center',)
plt.xlabel("Region")
plt.ylabel("Profit")
plt.title("Profit Generated by State")
plt.xticks(rotation=90)

plt.show()


# In[49]:


grouped_data = df_places.groupby(['State'], as_index=False).sum()
grouped_data.sort_values(by='Sales', ascending=False, inplace=True)


plt.figure(figsize=(22,10))
plt.bar(grouped_data['State'], grouped_data['Sales'], align='center',)
plt.xlabel("State")
plt.ylabel("Sales")
plt.title("Sales Generated by State")
plt.xticks(rotation=90)

plt.show()


# In[50]:


grouped_data = df_places.groupby('City', as_index=False).sum()

# Sort the data by Sales in descending order
grouped_data.sort_values(by='Sales', ascending=False, inplace=True)

# Select the top 5 cities
top_5_cities = grouped_data.head()

plt.bar(top_5_cities['City'], top_5_cities['Sales'], align='center')
plt.xlabel("City")
plt.ylabel("Sales")
plt.title("Top 5 Cities by Sales")
plt.xticks(rotation=90)

plt.show()


# In[51]:


grouped_data = df_places.groupby('City', as_index=False).sum()

# Sort the data by Sales in descending order
grouped_data.sort_values(by='Profit', ascending=False, inplace=True)

# Select the top 5 cities
top_5_cities = grouped_data.head()

plt.bar(top_5_cities['City'], top_5_cities['Profit'], align='center')
plt.xlabel("City")
plt.ylabel("Profit")
plt.title("Top 5 Cities by Profit")
plt.xticks(rotation=90)

plt.show()


# In[52]:


top_5_cities.City


# In[54]:


#top placies are :
#Cities: [New York City, Los Angeles, Seattle, San Francisco, Detroit]
#State : [california, New York]
#Region : [West]


# In[ ]:





# In[61]:


# Group the data by product category and calculate the average profit for each category
avg_profit_margin_by_category = df.groupby('Category')['Profit'].mean()

print(avg_profit_margin_by_category)


# In[62]:


df['Profit Margin'] = df['Profit'] / df['Sales']

# Group the data by product category and calculate the average profit margin for each category
avg_profit_margin_by_category = df.groupby('Category')['Profit Margin'].mean()

# Plot the average profit margin for each category as a bar chart
avg_profit_margin_by_category.plot(kind='bar')

# Add a title and labels to the chart
plt.title("Average Profit Margin by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Profit Margin")

plt.show()


# In[63]:


#Customers


# In[64]:


df.head()


# In[65]:


df.Segment.value_counts()


# In[66]:


df['Ship Mode'].value_counts()


# In[68]:


pivot_table = df.pivot_table(index='Segment', columns='Ship Mode', values='Sales', aggfunc='sum')
pivot_table


# In[69]:


pivot_table.plot(kind='bar', stacked=False)

plt.show()


# In[70]:


pivot_table = df.pivot_table(index='Segment', columns='Ship Mode', values='Profit', aggfunc='sum')

pivot_table.plot(kind='bar', stacked=False)

# Show the plot
plt.show()


# In[ ]:




