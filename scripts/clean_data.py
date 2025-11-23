import pandas as pd
import numpy as np

def clean_data(df):
    """Clean and prepare the sales data"""
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna()
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Add derived features
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['quarter'] = df['date'].dt.quarter
    
    return df

if __name__ == "__main__":
    # Load raw data
    df = pd.read_csv('data/sales_data.csv')
    print(f"Original data shape: {df.shape}")
    
    # Clean data
    cleaned_df = clean_data(df)
    print(f"Cleaned data shape: {cleaned_df.shape}")
    
    # Save cleaned data
    cleaned_df.to_csv('data/clean_sales_data.csv', index=False)
    print("Cleaned data saved successfully")

