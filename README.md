# 📊 Sales Analytics Dashboard

A comprehensive sales analytics platform built with Python, SQL, and an interactive Streamlit web dashboard. This project provides a modern, user-friendly dashboard solution for sales data analysis and visualization.

## 🚀 Project Overview

This sales analytics dashboard enables businesses to analyze sales performance, track KPIs, and gain actionable insights from sales data. The project includes data generation, cleaning, analysis, and visualization components with both static and interactive dashboards.

### Key Features
- 📈 **Interactive Dashboard**: Modern Streamlit web application
- 📊 **Comprehensive Analytics**: Revenue trends, product performance, regional analysis
- 🔧 **Data Pipeline**: Complete ETL process with mock data generation
- 📋 **SQL Integration**: SQLite database with structured sales data
- 🎯 **KPI Tracking**: Key performance indicators and metrics
- 📱 **Responsive Design**: Web-based dashboard accessible on any device
- 🔍 **Interactive Filters**: Dynamic filtering by date, product, region, and year
- 📥 **Data Export**: Download filtered data as CSV files

## 🛠️ Tech Stack

- **Python**: Data processing and analysis (pandas, numpy)
- **Streamlit**: Interactive web dashboard framework
- **SQL**: SQLite for data storage and queries
- **Visualization**: Plotly for interactive charts
- **Environment**: Jupyter Notebooks for EDA
- **Version Control**: Git/GitHub

## 📁 Project Structure

```
sales-analytics-dashboard/
├── data/
│   ├── sales_data.csv          # Raw generated sales data
│   ├── clean_sales_data.csv    # Cleaned and processed data
│   └── sales.db               # SQLite database
├── scripts/
│   ├── generate_data.py       # Mock sales data generator
│   ├── clean_data.py          # Data cleaning and preprocessing
│   ├── load_to_sql.py         # Load data to SQLite database
│   ├── utils.py               # Utility functions for analysis
│   └── streamlit_dashboard.py # Interactive Streamlit dashboard
├── notebooks/
│   └── EDA.ipynb             # Exploratory Data Analysis
├── reports/
│   └── insights.md           # Data insights and recommendations
├── assets/
│   └── screenshots/          # Dashboard screenshots and exports
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd sales-analytics-dashboard
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Generate Data and Create Database
```bash
# Generate mock sales data (10,000 transactions)
python scripts/generate_data.py

# Clean and preprocess the data
python scripts/clean_data.py

# Load data into SQLite database
python scripts/load_to_sql.py
```

### 3. Run Exploratory Data Analysis
```bash
jupyter notebook notebooks/EDA.ipynb
```

### 4. Launch Interactive Dashboard

```bash
streamlit run scripts/streamlit_dashboard.py --server.port=8051
```
Access at: http://localhost:8051

Alternatively, you can run it on the default port:
```bash
streamlit run scripts/streamlit_dashboard.py
```
Access at: http://localhost:8501

## 📊 Dashboard Features

### 🎯 Key Performance Indicators (KPIs)
- **Total Revenue**: $254,118,102 (sample data)
- **Total Transactions**: 10,000
- **Average Order Value**: $25,412
- **Total Quantity Sold**: 49,893 units

### 📈 Analytics Views

#### 1. Revenue Trends
- Monthly revenue patterns and seasonality
- Year-over-year growth analysis
- Peak performance periods identification

#### 2. Product Performance
- Top-performing products by revenue
- Product-wise quantity analysis
- Price vs. quantity correlations

#### 3. Regional Analysis
- Sales distribution across regions
- Regional performance comparisons
- Geographic revenue patterns

#### 4. Sales Team Performance
- Top sales performers identification
- Individual salesperson metrics
- Performance benchmarking

### 🔧 Interactive Features
- **Dynamic Filters**: Date range, product, region, year selections
- **Real-time Updates**: Instant chart updates based on filters
- **Data Export**: Download filtered data as CSV
- **Responsive Design**: Works on desktop and mobile devices
- **Hover Details**: Interactive tooltips with detailed information

## 📊 Power BI Alternative

This Streamlit dashboard serves as a powerful alternative to traditional BI tools like Power BI, providing:

- **No License Required**: Open-source solution with no subscription costs
- **Python Integration**: Leverage the full Python ecosystem for analysis
- **Custom Analytics**: Build custom calculations and visualizations
- **Real-time Filtering**: Interactive filters with instant updates
- **Easy Deployment**: Deploy to cloud platforms like Streamlit Community Cloud
- **Extensible**: Easy to modify and add new features

## 🔍 Key Insights (Sample Data)

### Revenue Analysis
- **Total Revenue**: $254,118,102 across 2022-2023
- **Top Product**: Product D with $55,763,015 (21.9% of total revenue)
- **Peak Month**: Month 12 with $22,378,098 (8.8% of annual revenue)
- **Growth Rate**: 3.8% year-over-year growth from 2022 to 2023

### Regional Performance
- **Top Region**: West region with $54,917,160 (21.6% of total sales)
- **Balanced Distribution**: All regions within 18-22% range
- **Consistent Performance**: Minimal regional variance indicates balanced market coverage

### Product Portfolio
- **Diversified Revenue**: Products A-E each contribute 19-22% of total revenue
- **Price Points**: Range from $45-$104 average unit prices
- **Volume Leaders**: Product A with highest total quantity (10,077 units)

### Sales Team Insights
- **Top Performer**: Alice Johnson with $25,412,872 in sales
- **Team Strength**: 10 sales representatives with consistent performance
- **Average Performance**: $25,411,810 per salesperson

### Recommendations
1. **Seasonal Strategy**: Capitalize on Month 12 peak performance patterns
2. **Product Focus**: Maintain Product D's market leadership while growing other products
3. **Regional Expansion**: Leverage West region success model for other regions
4. **Team Development**: Implement best practices from top performers across the team
5. **Data-Driven Decisions**: Use the dashboard's filtering capabilities to identify specific opportunities

## 📸 Dashboard Screenshots

### Streamlit Dashboard Overview
![Streamlit Overview](assets/screenshots/streamlit_overview.png)
*Interactive Streamlit dashboard with comprehensive KPIs and filters*

### Dashboard Features
![Dashboard Features](assets/screenshots/streamlit_features.png)
*Multiple tabs showing Overview, Individual Charts, Insights, and Raw Data views*

### Interactive Analytics
![Interactive Charts](assets/screenshots/streamlit_charts.png)
*Detailed analytics with monthly trends, product performance, and regional analysis*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the GitHub repository
- Check the sample insights in `reports/insights.md`
- Review the Streamlit documentation for customization options

## 🔄 Future Enhancements

- [ ] Real-time data integration
- [ ] Advanced machine learning forecasting
- [ ] Customer segmentation analysis
- [ ] Automated report generation
- [ ] API integration for external data sources
- [ ] Mobile app development
- [ ] Advanced user authentication and role management

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLite Documentation](https://sqlite.org/docs.html)

---

**Built with ❤️ for data-driven decision making**

*This dashboard transforms raw sales data into actionable business insights through interactive visualizations and comprehensive analytics.*

