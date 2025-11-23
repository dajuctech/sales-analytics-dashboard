import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_statistics(df):
    """Generate basic statistics for the dataset"""
    return df.describe()

def plot_monthly_sales(df):
    """Plot monthly sales trends"""
    monthly_sales = df.groupby(['year', 'month'])['total_sales'].sum()
    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='line')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.show()

def plot_sales_by_region(df):
    """Plot sales by region"""
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='region', y='total_sales')
    plt.title('Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Sales')
    plt.show()

