# Import Libraries 
import pandas as pd ;
import numpy as np ; 
import matplotlib.pyplot as plt ; 
import seaborn as sns  ; 
# Load Data
df = pd.read_csv('Unemployment in India.csv')
# view the first few rows
print(df.head()) 
# check for data types and null values
print(df.info())  
# get summary statistics
print(df.describe())  
# Check for Missing Values
print(df.isnull().sum()) 
#THRE IS NOT NULL VALUES 
# option to drop rows with null values
# df = df.dropna() 
# Data Type Conversion
df.columns = df.columns.str.strip() 
print(list(df.columns))
df['Date'] = pd.to_datetime(df['Date']) 
df['Region'] = df['Region'].astype('category') 
df['Area'] = df['Area'].astype('category')
# print(df.info()) 
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
# Time Series Analysis 
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'], label='Estimated Unemployment Rate')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate')
plt.title('Estimated Unemployment Rate  Over Time') 
plt.legend()
plt.show()
# Regional Analysis
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Region', y='Estimated Unemployment Rate (%)')
plt.xticks(rotation=90)
plt.show() 
# Seasonal Patterns 
#df['Month'] = df['Date'].dt.month
#sns.lineplot(data=df, x='Month', y='Unemployment Rate')
# Calculate average unemployment rate by month
monthly_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values)
plt.xlabel('Month')
plt.ylabel('Average Unemployment Rate (%)')
plt.title('Average Unemployment Rate by Month')
plt.show()
# Calculate average unemployment rate by year
yearly_avg = df.groupby('Year')['Estimated Unemployment Rate (%)'].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(x=yearly_avg.index, y=yearly_avg.values)
plt.xlabel('Year')
plt.ylabel('Average Unemployment Rate (%)')
plt.title('Average Unemployment Rate by Year')
plt.show()
# Plot histogram for unemployment rate distribution
plt.figure(figsize=(10, 6))
df['Estimated Unemployment Rate (%)'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Estimated Unemployment Rate (%)')
plt.title('Distribution of Estimated Unemployment Rate')
plt.show()
# Box plot by Region
plt.figure(figsize=(12, 6))
sns.boxplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.xticks(rotation=90)
plt.title('Unemployment Rate by Region')
plt.show()
# Correlation heatmap
plt.figure(figsize=(8, 6))
# Select only numeric columns for the correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
# Plot heatmap with only numeric data
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
# plt.show()
# Filter data for a specific year COVID-19 impact in 2020 
covid_data = df[df['Year'] == 2020]
plt.figure(figsize=(10, 6))
sns.lineplot(data=covid_data, x='Date', y='Estimated Unemployment Rate (%)', label='2020')
plt.xlabel('Date')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.title('Unemployment Rate in 2020 (COVID-19 Period)')
plt.legend()
plt.show()
