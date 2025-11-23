#!/usr/bin/env python3
"""
Static Sales Analytics Dashboard using Plotly
Creates professional static visualizations that can be saved as images
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def load_data():
    """Load the cleaned sales data"""
    df = pd.read_csv('data/clean_sales_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

def create_kpi_summary():
    """Create and display KPI summary"""
    df = load_data()
    
    kpis = {
        'Total Revenue': f"${df['total_sales'].sum():,.0f}",
        'Total Quantity': f"{df['quantity'].sum():,}",
        'Avg Order Value': f"${df['total_sales'].mean():,.0f}",
        'Total Transactions': f"{len(df):,}",
        'Date Range': f"{df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}",
        'Products': f"{df['product'].nunique()} products",
        'Regions': f"{df['region'].nunique()} regions"
    }
    
    print("📊 SALES ANALYTICS DASHBOARD - KEY METRICS")
    print("=" * 50)
    for metric, value in kpis.items():
        print(f"{metric:20}: {value}")
    print("=" * 50)
    
    return df

def create_main_dashboard():
    """Create comprehensive dashboard with multiple charts"""
    df = load_data()
    
    # Create subplots
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=[
            'Monthly Revenue Trends', 'Sales by Region',
            'Revenue by Product', 'Year-over-Year Comparison', 
            'Top Sales Performers', 'Price vs Quantity Analysis'
        ],
        specs=[
            [{"type": "scatter"}, {"type": "pie"}],
            [{"type": "bar"}, {"type": "bar"}],
            [{"type": "bar"}, {"type": "scatter"}]
        ],
        vertical_spacing=0.08
    )
    
    # 1. Monthly Revenue Trends
    monthly_data = df.groupby('month')['total_sales'].sum().reset_index()
    fig.add_trace(
        go.Scatter(x=monthly_data['month'], y=monthly_data['total_sales'],
                  mode='lines+markers', name='Monthly Revenue',
                  line=dict(color='#3498db', width=3),
                  marker=dict(size=8)),
        row=1, col=1
    )
    
    # 2. Sales by Region
    regional_data = df.groupby('region')['total_sales'].sum().reset_index()
    fig.add_trace(
        go.Pie(labels=regional_data['region'], values=regional_data['total_sales'],
               name="Regional Sales"),
        row=1, col=2
    )
    
    # 3. Revenue by Product
    product_data = df.groupby('product')['total_sales'].sum().sort_values(ascending=True).reset_index()
    fig.add_trace(
        go.Bar(y=product_data['product'], x=product_data['total_sales'],
               orientation='h', name='Product Revenue',
               marker=dict(color='#2ecc71')),
        row=2, col=1
    )
    
    # 4. Year-over-Year Comparison
    yearly_data = df.groupby('year')['total_sales'].sum().reset_index()
    fig.add_trace(
        go.Bar(x=yearly_data['year'], y=yearly_data['total_sales'],
               name='Yearly Revenue',
               marker=dict(color=['#e74c3c', '#27ae60'])),
        row=2, col=2
    )
    
    # 5. Top Sales Performers
    performer_data = df.groupby('salesperson')['total_sales'].sum().sort_values(ascending=True).tail(5).reset_index()
    fig.add_trace(
        go.Bar(y=performer_data['salesperson'], x=performer_data['total_sales'],
               orientation='h', name='Top Performers',
               marker=dict(color='#f39c12')),
        row=3, col=1
    )
    
    # 6. Price vs Quantity Scatter
    sample_data = df.sample(n=min(1000, len(df)))  # Sample for better performance
    fig.add_trace(
        go.Scatter(x=sample_data['unit_price'], y=sample_data['quantity'],
                  mode='markers', name='Price vs Quantity',
                  marker=dict(color=sample_data['total_sales'], 
                            colorscale='Viridis', size=8,
                            colorbar=dict(title="Total Sales"))),
        row=3, col=2
    )
    
    # Update layout
    fig.update_layout(
        height=1200, 
        showlegend=False,
        title={
            'text': '🚀 Sales Analytics Dashboard - Comprehensive Overview',
            'x': 0.5,
            'font': {'size': 24}
        }
    )
    
    # Update axes labels
    fig.update_xaxes(title_text="Month", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($)", row=1, col=1)
    fig.update_xaxes(title_text="Revenue ($)", row=2, col=1)
    fig.update_yaxes(title_text="Product", row=2, col=1)
    fig.update_xaxes(title_text="Year", row=2, col=2)
    fig.update_yaxes(title_text="Revenue ($)", row=2, col=2)
    fig.update_xaxes(title_text="Revenue ($)", row=3, col=1)
    fig.update_yaxes(title_text="Salesperson", row=3, col=1)
    fig.update_xaxes(title_text="Unit Price ($)", row=3, col=2)
    fig.update_yaxes(title_text="Quantity", row=3, col=2)
    
    return fig

def create_individual_charts():
    """Create individual charts for detailed analysis"""
    df = load_data()
    charts = {}
    
    # 1. Monthly Revenue Trends
    monthly_data = df.groupby('month')['total_sales'].sum().reset_index()
    charts['monthly'] = px.line(
        monthly_data, x='month', y='total_sales',
        title='📈 Monthly Revenue Trends',
        labels={'total_sales': 'Total Sales ($)', 'month': 'Month'}
    )
    charts['monthly'].update_traces(line=dict(color='#3498db', width=4), marker=dict(size=10))
    
    # 2. Product Performance
    product_data = df.groupby('product')['total_sales'].sum().sort_values(ascending=False).reset_index()
    charts['products'] = px.bar(
        product_data, x='product', y='total_sales',
        title='🏆 Revenue by Product',
        color='total_sales',
        color_continuous_scale='Blues'
    )
    
    # 3. Regional Distribution
    regional_data = df.groupby('region')['total_sales'].sum().reset_index()
    charts['regions'] = px.pie(
        regional_data, values='total_sales', names='region',
        title='🌍 Sales Distribution by Region',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    # 4. Year-over-Year Analysis
    yearly_data = df.groupby('year')['total_sales'].sum().reset_index()
    yearly_data['growth'] = yearly_data['total_sales'].pct_change() * 100
    charts['yearly'] = px.bar(
        yearly_data, x='year', y='total_sales',
        title='📅 Year-over-Year Revenue Comparison',
        text='total_sales'
    )
    charts['yearly'].update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
    
    return charts

def save_charts():
    """Save all charts as images"""
    os.makedirs('assets/screenshots', exist_ok=True)
    
    print("\n📸 Creating and saving dashboard screenshots...")
    
    # Main dashboard
    main_fig = create_main_dashboard()
    main_fig.write_html('assets/screenshots/plotly_dashboard.html')
    main_fig.write_image('assets/screenshots/dashboard_overview.png', width=1400, height=1200)
    print("✅ Saved: dashboard_overview.png")
    
    # Individual charts
    charts = create_individual_charts()
    
    charts['monthly'].write_image('assets/screenshots/monthly_trends.png', width=800, height=500)
    print("✅ Saved: monthly_trends.png")
    
    charts['products'].write_image('assets/screenshots/product_analysis.png', width=800, height=500)
    print("✅ Saved: product_analysis.png")
    
    charts['regions'].write_image('assets/screenshots/regional_sales.png', width=800, height=500)
    print("✅ Saved: regional_sales.png")
    
    charts['yearly'].write_image('assets/screenshots/year_comparison.png', width=800, height=500)
    print("✅ Saved: year_comparison.png")
    
    print(f"\n🎉 All charts saved to: assets/screenshots/")
    print("📱 Interactive HTML dashboard: assets/screenshots/plotly_dashboard.html")

def main():
    """Main function to create dashboard and display insights"""
    print("🚀 Creating Sales Analytics Dashboard with Plotly...")
    
    # Display KPI summary
    df = create_kpi_summary()
    
    # Create and save charts
    save_charts()
    
    # Display key insights
    print("\n📊 KEY INSIGHTS DISCOVERED:")
    print("-" * 40)
    
    # Revenue insights
    total_revenue = df['total_sales'].sum()
    print(f"💰 Total Revenue: ${total_revenue:,.0f}")
    
    # Top product
    top_product = df.groupby('product')['total_sales'].sum().sort_values(ascending=False).iloc[0]
    top_product_name = df.groupby('product')['total_sales'].sum().sort_values(ascending=False).index[0]
    print(f"🏆 Top Product: {top_product_name} (${top_product:,.0f})")
    
    # Top region
    top_region = df.groupby('region')['total_sales'].sum().sort_values(ascending=False).iloc[0]
    top_region_name = df.groupby('region')['total_sales'].sum().sort_values(ascending=False).index[0]
    print(f"🌍 Top Region: {top_region_name} (${top_region:,.0f})")
    
    # Growth calculation
    yearly_revenue = df.groupby('year')['total_sales'].sum()
    if len(yearly_revenue) > 1:
        years = sorted(yearly_revenue.index)
        growth = ((yearly_revenue[years[1]] - yearly_revenue[years[0]]) / yearly_revenue[years[0]]) * 100
        print(f"📈 YoY Growth: {growth:.1f}% ({years[0]} to {years[1]})")
    
    # Peak month
    monthly_revenue = df.groupby('month')['total_sales'].sum()
    peak_month = monthly_revenue.idxmax()
    print(f"📅 Peak Month: Month {peak_month} (${monthly_revenue[peak_month]:,.0f})")
    
    print("\n✨ Dashboard creation complete!")
    print("🖥️  Open 'assets/screenshots/plotly_dashboard.html' in your browser for interactive dashboard")
    print("📷 Static images saved for portfolio use")

if __name__ == '__main__':
    main()
