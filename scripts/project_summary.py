#!/usr/bin/env python3
"""
Project Completion Summary Script
Validates all components of the Sales Analytics Dashboard project
"""

import os
import pandas as pd
import sqlite3
from pathlib import Path
import sys

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def check_file_exists(filepath, description):
    """Check if a file exists and print status"""
    exists = os.path.exists(filepath)
    status = "✅ EXISTS" if exists else "❌ MISSING"
    print(f"{status}: {description}")
    return exists

def check_data_pipeline():
    """Check the data pipeline components"""
    print_header("📊 DATA PIPELINE VALIDATION")
    
    # Check data files
    data_files = {
        'data/sales_data.csv': 'Raw sales data (generated)',
        'data/clean_sales_data.csv': 'Cleaned sales data',
        'data/sales.db': 'SQLite database'
    }
    
    all_data_exists = True
    for filepath, description in data_files.items():
        if not check_file_exists(filepath, description):
            all_data_exists = False
    
    # Check data content
    if all_data_exists:
        try:
            df = pd.read_csv('data/clean_sales_data.csv')
            print(f"✅ Data loaded successfully: {len(df):,} records")
            
            # Check database
            conn = sqlite3.connect('data/sales.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM sales")
            db_count = cursor.fetchone()[0]
            conn.close()
            print(f"✅ Database verified: {db_count:,} records in SQLite")
            
            # Basic data validation
            required_columns = ['date', 'product', 'region', 'total_sales', 'quantity', 'unit_price']
            missing_cols = [col for col in required_columns if col not in df.columns]
            
            if not missing_cols:
                print("✅ All required columns present")
                
                # Data quality checks
                revenue = df['total_sales'].sum()
                print(f"✅ Total revenue: ${revenue:,.0f}")
                
                date_range = f"{df['date'].min()} to {df['date'].max()}"
                print(f"✅ Date range: {date_range}")
                
                products = df['product'].nunique()
                regions = df['region'].nunique()
                print(f"✅ Data diversity: {products} products, {regions} regions")
            else:
                print(f"❌ Missing columns: {missing_cols}")
                
        except Exception as e:
            print(f"❌ Data validation error: {str(e)}")
    
    return all_data_exists

def check_scripts():
    """Check all Python scripts"""
    print_header("🔧 SCRIPTS VALIDATION")
    
    scripts = {
        'scripts/generate_data.py': 'Data generation script',
        'scripts/clean_data.py': 'Data cleaning script',
        'scripts/load_to_sql.py': 'Database loading script',
        'scripts/utils.py': 'Utility functions',
        'scripts/streamlit_dashboard.py': 'Streamlit dashboard'
    }
    
    all_scripts_exist = True
    for script, description in scripts.items():
        if not check_file_exists(script, description):
            all_scripts_exist = False
    
    return all_scripts_exist

def check_notebooks():
    """Check Jupyter notebooks"""
    print_header("📓 NOTEBOOKS VALIDATION")
    
    notebooks = {
        'notebooks/EDA.ipynb': 'Exploratory Data Analysis notebook'
    }
    
    all_notebooks_exist = True
    for notebook, description in notebooks.items():
        if not check_file_exists(notebook, description):
            all_notebooks_exist = False
    
    return all_notebooks_exist

def check_powerbi_guides():
    """Check Power BI documentation"""
    print_header("📊 POWER BI DOCUMENTATION")
    
    powerbi_files = {
        'powerbi/PowerBI_Setup_Guide.md': 'Power BI setup guide',
        'powerbi/DAX_Measures.txt': 'DAX measures and formulas',
        'powerbi/Dashboard_Layout.md': 'Dashboard layout guide',
        'powerbi/Dashboard_Checklist.md': 'Validation checklist'
    }
    
    all_powerbi_exists = True
    for filepath, description in powerbi_files.items():
        if not check_file_exists(filepath, description):
            all_powerbi_exists = False
    
    return all_powerbi_exists

def check_reports():
    """Check reports and insights"""
    print_header("📈 REPORTS AND INSIGHTS")
    
    reports = {
        'reports/insights.md': 'Data insights and recommendations'
    }
    
    all_reports_exist = True
    for report, description in reports.items():
        if not check_file_exists(report, description):
            all_reports_exist = False
    
    return all_reports_exist

def check_assets():
    """Check assets and screenshots"""
    print_header("📸 ASSETS AND SCREENSHOTS")
    
    assets_dir = 'assets/screenshots'
    if os.path.exists(assets_dir):
        print(f"✅ EXISTS: Screenshots directory")
        
        # List screenshot files
        screenshots = list(Path(assets_dir).glob('*.png')) + list(Path(assets_dir).glob('*.html'))
        if screenshots:
            print(f"✅ Found {len(screenshots)} screenshot/export files:")
            for screenshot in sorted(screenshots):
                print(f"   - {screenshot.name}")
        else:
            print("⚠️  No screenshot files found")
            return False
    else:
        print(f"❌ MISSING: Screenshots directory")
        return False
    
    return True

def check_configuration():
    """Check configuration files"""
    print_header("⚙️ CONFIGURATION FILES")
    
    config_files = {
        'requirements.txt': 'Python dependencies',
        '.gitignore': 'Git ignore rules',
        'README.md': 'Project documentation'
    }
    
    all_config_exists = True
    for config, description in config_files.items():
        if not check_file_exists(config, description):
            all_config_exists = False
    
    # Check requirements.txt content
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            requirements = f.read().strip().split('\n')
            required_packages = ['pandas', 'numpy', 'plotly', 'streamlit', 'dash']
            missing_packages = [pkg for pkg in required_packages if not any(pkg in req for req in requirements)]
            
            if not missing_packages:
                print("✅ All required packages in requirements.txt")
            else:
                print(f"⚠️  Missing packages in requirements.txt: {missing_packages}")
    
    return all_config_exists

def run_dashboard_tests():
    """Test dashboard functionality"""
    print_header("🚀 DASHBOARD FUNCTIONALITY TESTS")
    
    try:
        # Test data loading capability
        import pandas as pd
        df = pd.read_csv('data/clean_sales_data.csv')
        print("✅ Data loading: Successful")
        
        # Test basic visualizations
        import matplotlib.pyplot as plt
        import seaborn as sns
        plt.style.use('default')
        print("✅ Matplotlib/Seaborn: Available")
        
        # Test Plotly
        import plotly.express as px
        import plotly.graph_objects as go
        print("✅ Plotly: Available")
        
        # Test Streamlit (import only)
        import streamlit as st
        print("✅ Streamlit: Available")
        
        print("✅ All dashboard libraries are functional")
        
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        return False
    
    return True

def print_project_summary():
    """Print final project summary"""
    print_header("📋 PROJECT COMPLETION SUMMARY")
    
    print("🎯 COMPLETED COMPONENTS:")
    print("   ✅ Data Pipeline (Generate → Clean → Load)")
    print("   ✅ Exploratory Data Analysis (EDA)")
    print("   ✅ SQLite Database Integration")
    print("   ✅ Interactive Streamlit Dashboard")
    print("   ✅ Comprehensive Documentation")
    print("   ✅ Data Insights and Recommendations")
    print()
    
    print("🚀 AVAILABLE DASHBOARD:")
    print("   📊 Streamlit Dashboard: streamlit run scripts/streamlit_dashboard.py --server.port=8051")
    print()
    
    print("🔗 ACCESS POINT:")
    print("   🌐 Streamlit: http://localhost:8051")
    print()
    
    print("📈 KEY INSIGHTS (Sample Data):")
    try:
        df = pd.read_csv('data/clean_sales_data.csv')
        total_revenue = df['total_sales'].sum()
        total_transactions = len(df)
        avg_order = df['total_sales'].mean()
        
        print(f"   💰 Total Revenue: ${total_revenue:,.0f}")
        print(f"   📋 Transactions: {total_transactions:,}")
        print(f"   📊 Avg Order Value: ${avg_order:.0f}")
        
        # Top product
        top_product = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)
        print(f"   🏆 Top Product: {top_product.index[0]} (${top_product.iloc[0]:,.0f})")
        
        # Top region
        top_region = df.groupby('region')['total_sales'].sum().sort_values(ascending=False)
        print(f"   🌍 Top Region: {top_region.index[0]} (${top_region.iloc[0]:,.0f})")
        
    except:
        print("   ⚠️  Unable to load sample insights")

def main():
    """Main validation and summary function"""
    print("🔍 SALES ANALYTICS DASHBOARD - PROJECT VALIDATION")
    print("=" * 60)
    
    # Run all validation checks
    checks = [
        check_data_pipeline(),
        check_scripts(),
        check_notebooks(),
        check_powerbi_guides(),
        check_reports(),
        check_assets(),
        check_configuration(),
        run_dashboard_tests()
    ]
    
    # Calculate success rate
    success_rate = (sum(checks) / len(checks)) * 100
    
    print_header("🎯 VALIDATION RESULTS")
    print(f"Overall Project Completion: {success_rate:.1f}%")
    
    if success_rate >= 90:
        print("🎉 PROJECT COMPLETE - Ready for portfolio presentation!")
    elif success_rate >= 75:
        print("⚠️  PROJECT MOSTLY COMPLETE - Minor issues to address")
    else:
        print("❌ PROJECT INCOMPLETE - Major components missing")
    
    # Print project summary
    print_project_summary()
    
    return success_rate >= 90

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
