import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_sales_data():
    """Generate mock sales data"""
    # Date range: last 2 years
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    
    # Generate random dates
    date_range = pd.date_range(start_date, end_date, freq='D')
    
    # Products
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    
    # Regions
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    # Salespeople
    salespeople = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie Wilson']
    
    data = []
    for _ in range(10000):  # Generate 10,000 records
        record = {
            'date': random.choice(date_range),
            'product': random.choice(products),
            'region': random.choice(regions),
            'salesperson': random.choice(salespeople),
            'quantity': random.randint(1, 100),
            'unit_price': round(random.uniform(10, 1000), 2),
        }
        record['total_sales'] = record['quantity'] * record['unit_price']
        data.append(record)
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Generate data
    sales_data = generate_sales_data()
    
    # Save to CSV
    sales_data.to_csv('data/sales_data.csv', index=False)
    print(f"Generated {len(sales_data)} sales records")
    print(sales_data.head())
