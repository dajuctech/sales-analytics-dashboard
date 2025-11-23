#!/usr/bin/env python3
"""
Streamlit Sales Analytics Dashboard
Interactive web application for sales data analysis and visualization
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import os

# Set page config
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    """Load and cache the cleaned sales data"""
    df = pd.read_csv('data/clean_sales_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

def create_kpi_metrics(df):
    """Create KPI metrics display"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = df['total_sales'].sum()
        st.metric(
            label="💰 Total Revenue",
            value=f"${total_revenue:,.0f}"
        )
    
    with col2:
        total_transactions = len(df)
        st.metric(
            label="📋 Total Transactions",
            value=f"{total_transactions:,}"
        )
    
    with col3:
        avg_order_value = df['total_sales'].mean()
        st.metric(
            label="📈 Avg Order Value",
            value=f"${avg_order_value:,.0f}"
        )
    
    with col4:
        total_quantity = df['quantity'].sum()
        st.metric(
            label="📦 Total Quantity",
            value=f"{total_quantity:,}"
        )

def create_sidebar_filters(df):
    """Create sidebar filters"""
    st.sidebar.header("🔧 Dashboard Filters")
    
    # Date range filter
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Product filter
    products = ['All'] + sorted(df['product'].unique().tolist())
    selected_products = st.sidebar.multiselect(
        "Select Products",
        products,
        default=['All']
    )
    
    # Region filter
    regions = ['All'] + sorted(df['region'].unique().tolist())
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        regions,
        default=['All']
    )
    
    # Year filter
    years = ['All'] + sorted(df['year'].unique().tolist())
    selected_years = st.sidebar.multiselect(
        "Select Years",
        years,
        default=['All']
    )
    
    return {
        'date_range': date_range,
        'products': selected_products,
        'regions': selected_regions,
        'years': selected_years
    }

def apply_filters(df, filters):
    """Apply selected filters to dataframe"""
    filtered_df = df.copy()
    
    # Apply date filter
    if len(filters['date_range']) == 2:
        start_date = pd.to_datetime(filters['date_range'][0])
        end_date = pd.to_datetime(filters['date_range'][1])
        filtered_df = filtered_df[
            (filtered_df['date'] >= start_date) & 
            (filtered_df['date'] <= end_date)
        ]
    
    # Apply product filter
    if 'All' not in filters['products'] and len(filters['products']) > 0:
        filtered_df = filtered_df[filtered_df['product'].isin(filters['products'])]
    
    # Apply region filter
    if 'All' not in filters['regions'] and len(filters['regions']) > 0:
        filtered_df = filtered_df[filtered_df['region'].isin(filters['regions'])]
    
    # Apply year filter
    if 'All' not in filters['years'] and len(filters['years']) > 0:
        filtered_df = filtered_df[filtered_df['year'].isin(filters['years'])]
    
    return filtered_df

def create_monthly_trends_chart(df):
    """Create monthly trends chart"""
    monthly_data = df.groupby('month')['total_sales'].sum().reset_index()
    
    fig = px.line(
        monthly_data, 
        x='month', 
        y='total_sales',
        title='📈 Monthly Revenue Trends',
        labels={'total_sales': 'Revenue ($)', 'month': 'Month'}
    )
    
    fig.update_traces(
        line=dict(color='#3498db', width=4),
        marker=dict(size=10)
    )
    
    fig.update_layout(
        height=400,
        title_font_size=16
    )
    
    return fig

def create_product_analysis_chart(df):
    """Create product analysis chart"""
    product_data = df.groupby('product')['total_sales'].sum().sort_values(ascending=False).reset_index()
    
    fig = px.bar(
        product_data,
        x='product',
        y='total_sales',
        title='🏆 Revenue by Product',
        color='total_sales',
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        height=400,
        title_font_size=16
    )
    
    return fig

def create_regional_distribution_chart(df):
    """Create regional distribution pie chart"""
    regional_data = df.groupby('region')['total_sales'].sum().reset_index()
    
    fig = px.pie(
        regional_data,
        values='total_sales',
        names='region',
        title='🌍 Sales Distribution by Region',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_layout(
        height=400,
        title_font_size=16
    )
    
    return fig

def create_yearly_comparison_chart(df):
    """Create year-over-year comparison chart"""
    yearly_data = df.groupby('year')['total_sales'].sum().reset_index()
    
    fig = px.bar(
        yearly_data,
        x='year',
        y='total_sales',
        title='📅 Year-over-Year Revenue Comparison',
        text='total_sales',
        color='total_sales',
        color_continuous_scale='Greens'
    )
    
    fig.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
    fig.update_layout(
        height=400,
        title_font_size=16
    )
    
    return fig

def create_top_performers_chart(df):
    """Create top sales performers chart"""
    performer_data = df.groupby('salesperson')['total_sales'].sum().sort_values(ascending=False).head(10).reset_index()
    
    fig = px.bar(
        performer_data,
        x='total_sales',
        y='salesperson',
        orientation='h',
        title='👥 Top Sales Performers',
        color='total_sales',
        color_continuous_scale='Oranges'
    )
    
    fig.update_layout(
        height=500,
        title_font_size=16
    )
    
    return fig

def create_price_quantity_scatter(df):
    """Create price vs quantity scatter plot"""
    # Sample for better performance
    sample_data = df.sample(n=min(1000, len(df)))
    
    fig = px.scatter(
        sample_data,
        x='unit_price',
        y='quantity',
        color='total_sales',
        title='💲 Price vs Quantity Analysis',
        color_continuous_scale='Viridis',
        hover_data=['product', 'region']
    )
    
    fig.update_layout(
        height=400,
        title_font_size=16
    )
    
    return fig

def create_comprehensive_dashboard(df):
    """Create comprehensive dashboard with subplots"""
    # Create subplots
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=[
            'Monthly Trends', 'Product Performance', 'Regional Distribution',
            'Yearly Comparison', 'Top Performers', 'Price vs Quantity'
        ],
        specs=[
            [{"type": "scatter"}, {"type": "bar"}, {"type": "pie"}],
            [{"type": "bar"}, {"type": "bar"}, {"type": "scatter"}]
        ]
    )
    
    # Monthly trends
    monthly_data = df.groupby('month')['total_sales'].sum().reset_index()
    fig.add_trace(
        go.Scatter(x=monthly_data['month'], y=monthly_data['total_sales'],
                  mode='lines+markers', name='Monthly Revenue'),
        row=1, col=1
    )
    
    # Product performance
    product_data = df.groupby('product')['total_sales'].sum().sort_values(ascending=False).reset_index()
    fig.add_trace(
        go.Bar(x=product_data['product'], y=product_data['total_sales'],
               name='Product Revenue'),
        row=1, col=2
    )
    
    # Regional distribution
    regional_data = df.groupby('region')['total_sales'].sum().reset_index()
    fig.add_trace(
        go.Pie(labels=regional_data['region'], values=regional_data['total_sales'],
               name="Regional Sales"),
        row=1, col=3
    )
    
    # Yearly comparison
    yearly_data = df.groupby('year')['total_sales'].sum().reset_index()
    fig.add_trace(
        go.Bar(x=yearly_data['year'], y=yearly_data['total_sales'],
               name='Yearly Revenue'),
        row=2, col=1
    )
    
    # Top performers
    performer_data = df.groupby('salesperson')['total_sales'].sum().sort_values(ascending=False).head(5).reset_index()
    fig.add_trace(
        go.Bar(x=performer_data['total_sales'], y=performer_data['salesperson'],
               orientation='h', name='Top Performers'),
        row=2, col=2
    )
    
    # Price vs quantity
    sample_data = df.sample(n=min(500, len(df)))
    fig.add_trace(
        go.Scatter(x=sample_data['unit_price'], y=sample_data['quantity'],
                  mode='markers', name='Price vs Quantity'),
        row=2, col=3
    )
    
    fig.update_layout(
        height=800,
        title_text="📊 Comprehensive Sales Analytics Dashboard",
        showlegend=False
    )
    
    return fig

def display_data_insights(df):
    """Display key data insights"""
    st.subheader("🔍 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**📊 Revenue Analysis:**")
        total_revenue = df['total_sales'].sum()
        st.write(f"• Total Revenue: ${total_revenue:,.0f}")
        
        # Top product
        top_product = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)
        st.write(f"• Top Product: {top_product.index[0]} (${top_product.iloc[0]:,.0f})")
        
        # Top region
        top_region = df.groupby('region')['total_sales'].sum().sort_values(ascending=False)
        st.write(f"• Top Region: {top_region.index[0]} (${top_region.iloc[0]:,.0f})")
    
    with col2:
        st.write("**📈 Growth Analysis:**")
        
        # YoY Growth
        yearly_revenue = df.groupby('year')['total_sales'].sum()
        if len(yearly_revenue) > 1:
            years = sorted(yearly_revenue.index)
            growth = ((yearly_revenue[years[1]] - yearly_revenue[years[0]]) / yearly_revenue[years[0]]) * 100
            st.write(f"• YoY Growth: {growth:.1f}%")
        
        # Peak month
        monthly_revenue = df.groupby('month')['total_sales'].sum()
        peak_month = monthly_revenue.idxmax()
        st.write(f"• Peak Month: Month {peak_month} (${monthly_revenue[peak_month]:,.0f})")
        
        # Average order value
        avg_order = df['total_sales'].mean()
        st.write(f"• Avg Order Value: ${avg_order:,.0f}")

def display_raw_data(df):
    """Display raw data table with filters"""
    st.subheader("📋 Raw Data View")
    
    # Data summary
    st.write(f"**Dataset Overview:** {len(df):,} transactions")
    
    # Display data
    st.dataframe(
        df.round(2),
        use_container_width=True,
        height=400
    )
    
    # Download button
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name=f"sales_data_filtered_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

def main():
    """Main Streamlit application"""
    # Header
    st.title("🚀 Sales Analytics Dashboard")
    st.markdown("**Interactive Sales Data Analysis and Visualization Platform**")
    
    # Load data
    try:
        df = load_data()
    except FileNotFoundError:
        st.error("❌ Sales data not found. Please ensure 'data/clean_sales_data.csv' exists.")
        st.info("💡 Run the data generation and cleaning scripts first.")
        return
    
    # Sidebar filters
    filters = create_sidebar_filters(df)
    
    # Apply filters
    filtered_df = apply_filters(df, filters)
    
    if len(filtered_df) == 0:
        st.warning("⚠️ No data matches the selected filters. Please adjust your selection.")
        return
    
    # Show filter summary
    st.info(f"📊 Showing {len(filtered_df):,} transactions out of {len(df):,} total")
    
    # KPI Metrics
    create_kpi_metrics(filtered_df)
    
    st.markdown("---")
    
    # Main dashboard tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Individual Charts", "🔍 Insights", "📋 Raw Data"])
    
    with tab1:
        st.subheader("📊 Dashboard Overview")
        comprehensive_fig = create_comprehensive_dashboard(filtered_df)
        st.plotly_chart(comprehensive_fig, use_container_width=True)
    
    with tab2:
        st.subheader("📈 Detailed Analysis")
        
        # Row 1: Monthly trends and Product analysis
        col1, col2 = st.columns(2)
        with col1:
            monthly_fig = create_monthly_trends_chart(filtered_df)
            st.plotly_chart(monthly_fig, use_container_width=True)
        
        with col2:
            product_fig = create_product_analysis_chart(filtered_df)
            st.plotly_chart(product_fig, use_container_width=True)
        
        # Row 2: Regional distribution and Yearly comparison
        col3, col4 = st.columns(2)
        with col3:
            regional_fig = create_regional_distribution_chart(filtered_df)
            st.plotly_chart(regional_fig, use_container_width=True)
        
        with col4:
            yearly_fig = create_yearly_comparison_chart(filtered_df)
            st.plotly_chart(yearly_fig, use_container_width=True)
        
        # Row 3: Top performers and Price vs Quantity
        col5, col6 = st.columns(2)
        with col5:
            performers_fig = create_top_performers_chart(filtered_df)
            st.plotly_chart(performers_fig, use_container_width=True)
        
        with col6:
            scatter_fig = create_price_quantity_scatter(filtered_df)
            st.plotly_chart(scatter_fig, use_container_width=True)
    
    with tab3:
        display_data_insights(filtered_df)
    
    with tab4:
        display_raw_data(filtered_df)
    
    # Footer
    st.markdown("---")
    st.markdown("**📊 Sales Analytics Dashboard** | Built with Streamlit & Plotly")
    
    # Sidebar info
    st.sidebar.markdown("---")
    st.sidebar.info(
        "💡 **How to use:**\n\n"
        "1. Adjust filters to explore data\n"
        "2. Switch between tabs for different views\n"
        "3. Hover over charts for details\n"
        "4. Download filtered data as CSV"
    )

if __name__ == '__main__':
    main()
