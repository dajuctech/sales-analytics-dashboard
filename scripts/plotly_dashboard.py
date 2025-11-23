#!/usr/bin/env python3
"""
Interactive Sales Analytics Dashboard using Plotly Dash
Professional Power BI-style dashboard with interactive filtering
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Load and prepare data
def load_data():
    """Load the cleaned sales data"""
    df = pd.read_csv('data/clean_sales_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['month_name'] = df['date'].dt.strftime('%B')
    df['quarter_label'] = 'Q' + df['quarter'].astype(str)
    return df

# Calculate KPIs
def calculate_kpis(df):
    """Calculate key performance indicators"""
    return {
        'total_revenue': df['total_sales'].sum(),
        'total_quantity': df['quantity'].sum(),
        'avg_order_value': df['total_sales'].mean(),
        'total_transactions': len(df),
        'unique_products': df['product'].nunique(),
        'unique_regions': df['region'].nunique()
    }

# Create KPI cards
def create_kpi_cards(kpis):
    """Create KPI cards for dashboard header"""
    cards = [
        dbc.Card([
            dbc.CardBody([
                html.H2(f"${kpis['total_revenue']:,.0f}", className="card-title text-primary"),
                html.P("Total Revenue", className="card-text"),
                html.Small("💰", className="text-muted")
            ])
        ], className="mb-3 text-center", style={"background-color": "#f8f9fa"}),
        
        dbc.Card([
            dbc.CardBody([
                html.H2(f"{kpis['total_quantity']:,}", className="card-title text-success"),
                html.P("Total Quantity", className="card-text"),
                html.Small("📦", className="text-muted")
            ])
        ], className="mb-3 text-center", style={"background-color": "#f8f9fa"}),
        
        dbc.Card([
            dbc.CardBody([
                html.H2(f"${kpis['avg_order_value']:,.0f}", className="card-title text-warning"),
                html.P("Avg Order Value", className="card-text"),
                html.Small("💳", className="text-muted")
            ])
        ], className="mb-3 text-center", style={"background-color": "#f8f9fa"}),
        
        dbc.Card([
            dbc.CardBody([
                html.H2(f"{kpis['total_transactions']:,}", className="card-title text-info"),
                html.P("Total Transactions", className="card-text"),
                html.Small("📊", className="text-muted")
            ])
        ], className="mb-3 text-center", style={"background-color": "#f8f9fa"}),
    ]
    return cards

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Sales Analytics Dashboard"

# Load data
df = load_data()
kpis = calculate_kpis(df)

# Define the layout
app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H1("🚀 Sales Analytics Dashboard", 
                   className="text-center mb-4",
                   style={"color": "#2c3e50", "font-weight": "bold"})
        ])
    ]),
    
    # KPI Cards
    dbc.Row([
        dbc.Col(card, width=3) for card in create_kpi_cards(kpis)
    ], className="mb-4"),
    
    # Filters Row
    dbc.Row([
        dbc.Col([
            html.Label("Select Year:", style={"font-weight": "bold"}),
            dcc.Dropdown(
                id='year-filter',
                options=[{'label': 'All Years', 'value': 'all'}] + 
                       [{'label': str(year), 'value': year} for year in sorted(df['year'].unique())],
                value='all',
                clearable=False
            )
        ], width=3),
        
        dbc.Col([
            html.Label("Select Region:", style={"font-weight": "bold"}),
            dcc.Dropdown(
                id='region-filter',
                options=[{'label': 'All Regions', 'value': 'all'}] + 
                       [{'label': region, 'value': region} for region in sorted(df['region'].unique())],
                value='all',
                clearable=False
            )
        ], width=3),
        
        dbc.Col([
            html.Label("Select Product:", style={"font-weight": "bold"}),
            dcc.Dropdown(
                id='product-filter',
                options=[{'label': 'All Products', 'value': 'all'}] + 
                       [{'label': product, 'value': product} for product in sorted(df['product'].unique())],
                value='all',
                clearable=False
            )
        ], width=3),
        
        dbc.Col([
            html.Div([
                html.Button("Reset Filters", id="reset-btn", className="btn btn-outline-secondary btn-sm mt-4")
            ])
        ], width=3)
    ], className="mb-4"),
    
    # Charts Row 1
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='monthly-trends')
        ], width=8),
        
        dbc.Col([
            dcc.Graph(id='regional-distribution')
        ], width=4)
    ], className="mb-4"),
    
    # Charts Row 2
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='product-performance')
        ], width=6),
        
        dbc.Col([
            dcc.Graph(id='yearly-comparison')
        ], width=6)
    ], className="mb-4"),
    
    # Charts Row 3
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='top-performers')
        ], width=6),
        
        dbc.Col([
            dcc.Graph(id='price-quantity-scatter')
        ], width=6)
    ]),
    
    # Footer
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.P("Sales Analytics Dashboard | Built with Plotly Dash | Data: 2022-2023 Sales Records",
                  className="text-center text-muted small")
        ])
    ])
], fluid=True)

# Callback to filter data
def filter_data(df, year, region, product):
    """Filter dataframe based on selected filters"""
    filtered_df = df.copy()
    
    if year != 'all':
        filtered_df = filtered_df[filtered_df['year'] == year]
    if region != 'all':
        filtered_df = filtered_df[filtered_df['region'] == region]
    if product != 'all':
        filtered_df = filtered_df[filtered_df['product'] == product]
    
    return filtered_df

# Reset filters callback
@app.callback(
    [Output('year-filter', 'value'),
     Output('region-filter', 'value'),
     Output('product-filter', 'value')],
    [Input('reset-btn', 'n_clicks')]
)
def reset_filters(n_clicks):
    return 'all', 'all', 'all'

# Main callback for updating all charts
@app.callback(
    [Output('monthly-trends', 'figure'),
     Output('regional-distribution', 'figure'),
     Output('product-performance', 'figure'),
     Output('yearly-comparison', 'figure'),
     Output('top-performers', 'figure'),
     Output('price-quantity-scatter', 'figure')],
    [Input('year-filter', 'value'),
     Input('region-filter', 'value'),
     Input('product-filter', 'value')]
)
def update_charts(year, region, product):
    # Filter data
    filtered_df = filter_data(df, year, region, product)
    
    # 1. Monthly Trends
    monthly_data = filtered_df.groupby('month')['total_sales'].sum().reset_index()
    fig1 = px.line(monthly_data, x='month', y='total_sales',
                   title='Monthly Revenue Trends',
                   labels={'total_sales': 'Total Sales ($)', 'month': 'Month'})
    fig1.update_traces(line=dict(color='#3498db', width=3), marker=dict(size=8))
    fig1.update_layout(height=400, title_font_size=16)
    
    # 2. Regional Distribution
    regional_data = filtered_df.groupby('region')['total_sales'].sum().reset_index()
    fig2 = px.pie(regional_data, values='total_sales', names='region',
                  title='Sales by Region',
                  color_discrete_sequence=px.colors.qualitative.Set3)
    fig2.update_layout(height=400, title_font_size=16)
    
    # 3. Product Performance
    product_data = filtered_df.groupby('product')['total_sales'].sum().sort_values(ascending=True).reset_index()
    fig3 = px.bar(product_data, x='total_sales', y='product', orientation='h',
                  title='Revenue by Product',
                  labels={'total_sales': 'Total Sales ($)', 'product': 'Product'})
    fig3.update_traces(marker_color='#2ecc71')
    fig3.update_layout(height=400, title_font_size=16)
    
    # 4. Yearly Comparison
    yearly_data = filtered_df.groupby('year')['total_sales'].sum().reset_index()
    fig4 = px.bar(yearly_data, x='year', y='total_sales',
                  title='Annual Revenue Comparison',
                  labels={'total_sales': 'Total Sales ($)', 'year': 'Year'})
    fig4.update_traces(marker_color=['#e74c3c', '#27ae60'])
    fig4.update_layout(height=400, title_font_size=16)
    
    # 5. Top Performers (by salesperson)
    top_performers = filtered_df.groupby('salesperson')['total_sales'].sum().sort_values(ascending=True).tail(5).reset_index()
    fig5 = px.bar(top_performers, x='total_sales', y='salesperson', orientation='h',
                  title='Top 5 Sales Performers',
                  labels={'total_sales': 'Total Sales ($)', 'salesperson': 'Salesperson'})
    fig5.update_traces(marker_color='#f39c12')
    fig5.update_layout(height=400, title_font_size=16)
    
    # 6. Price vs Quantity Scatter
    fig6 = px.scatter(filtered_df, x='unit_price', y='quantity',
                      color='product', size='total_sales',
                      title='Price vs Quantity Analysis',
                      labels={'unit_price': 'Unit Price ($)', 'quantity': 'Quantity'})
    fig6.update_layout(height=400, title_font_size=16)
    
    return fig1, fig2, fig3, fig4, fig5, fig6

if __name__ == '__main__':
    print("🚀 Starting Sales Analytics Dashboard...")
    print("📊 Dashboard will open at: http://127.0.0.1:8050")
    print("🔄 Press Ctrl+C to stop the server")
    app.run(debug=True, port=8050)
