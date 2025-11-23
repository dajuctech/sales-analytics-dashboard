import pandas as pd
from sqlalchemy import create_engine

def load_to_database(csv_file, database_path):
    """Load cleaned data to SQLite database"""
    # Read cleaned data
    df = pd.read_csv(csv_file)
    
    # Create SQLite engine
    engine = create_engine(f'sqlite:///{database_path}')
    
    # Load to database
    df.to_sql('sales', engine, if_exists='replace', index=False)
    print(f"Data loaded to database: {database_path}")

if __name__ == "__main__":
    load_to_database('data/clean_sales_data.csv', 'data/sales.db')

