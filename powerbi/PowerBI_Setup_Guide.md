# Power BI Dashboard Setup Guide

## Phase 6 - Power BI Dashboard Creation

### Prerequisites
1. **Power BI Desktop** - Download from [Microsoft Power BI](https://powerbi.microsoft.com/desktop/)
2. **Data Source** - `../data/clean_sales_data.csv` (already prepared)

---

## Step 1: Import Data into Power BI

### Data Connection
1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Navigate to: `data/clean_sales_data.csv`
4. Click **Load**

### Verify Data Import
- **Rows**: Should show ~10,000 records
- **Columns**: date, product, region, salesperson, quantity, unit_price, total_sales, month, year, quarter

---

## Step 2: Create Calculated Measures (DAX)

### Go to **Modeling** tab → **New Measure** and create:

```dax
# Total Revenue
Total Revenue = SUM(sales[total_sales])

# Total Quantity
Total Quantity = SUM(sales[quantity])

# Average Order Value
Average Order Value = DIVIDE([Total Revenue], [Total Quantity], 0)

# Total Transactions
Total Transactions = COUNTROWS(sales)

# Revenue Growth YoY
Revenue Growth YoY = 
VAR CurrentYear = SUM(sales[total_sales])
VAR PreviousYear = CALCULATE(SUM(sales[total_sales]), SAMEPERIODLASTYEAR(sales[date]))
RETURN DIVIDE(CurrentYear - PreviousYear, PreviousYear, 0)

# Top Product
Top Product = 
CALCULATE(
    MAX(sales[product]),
    TOPN(1, 
        SUMMARIZE(sales, sales[product], "Revenue", SUM(sales[total_sales])),
        [Revenue], DESC
    )
)
```

---

## Step 3: Create Dashboard Visuals

### Page Layout: **Sales Analytics Dashboard**

#### **KPI Cards Row** (Top of dashboard)
1. **Total Revenue Card**
   - Visual: Card
   - Field: Total Revenue
   - Format: Currency ($)

2. **Total Quantity Card**
   - Visual: Card  
   - Field: Total Quantity
   - Format: Whole Number

3. **Average Order Value Card**
   - Visual: Card
   - Field: Average Order Value
   - Format: Currency ($)

4. **Total Transactions Card**
   - Visual: Card
   - Field: Total Transactions
   - Format: Whole Number

#### **Charts Section**

5. **Monthly Revenue Trend** (Line Chart)
   - Visual: Line Chart
   - X-Axis: month
   - Y-Axis: Total Revenue
   - Title: "Monthly Revenue Trends"

6. **Top Products by Revenue** (Bar Chart)
   - Visual: Horizontal Bar Chart
   - Y-Axis: product
   - X-Axis: Total Revenue
   - Title: "Revenue by Product"
   - Sort: Descending by Total Revenue

7. **Sales by Region** (Pie Chart)
   - Visual: Pie Chart
   - Legend: region
   - Values: Total Revenue
   - Title: "Sales Distribution by Region"
   - Show percentages: ON

8. **Year-over-Year Analysis** (Clustered Column Chart)
   - Visual: Clustered Column Chart
   - X-Axis: year
   - Y-Axis: Total Revenue
   - Title: "Annual Revenue Comparison"

#### **Filters Section** (Right side)
9. **Year Slicer**
   - Visual: Slicer
   - Field: year
   - Style: List

10. **Region Slicer**
    - Visual: Slicer
    - Field: region
    - Style: List

11. **Product Slicer**
    - Visual: Slicer
    - Field: product
    - Style: Dropdown

---

## Step 4: Dashboard Formatting

### Color Scheme
- **Primary**: Blue (#1f77b4)
- **Secondary**: Orange (#ff7f0e)
- **Accent**: Green (#2ca02c)
- **Background**: White (#ffffff)

### Formatting Guidelines
1. **Title**: "Sales Analytics Dashboard" - Size 24, Bold
2. **Chart Titles**: Size 14, Bold
3. **Background**: Light gray (#f8f9fa)
4. **Grid Lines**: Light gray, minimal
5. **Font**: Segoe UI throughout

---

## Step 5: Interactivity Setup

### Cross-Filtering
- Enable cross-filtering between all visuals
- Year slicer affects all charts
- Region slicer affects all charts
- Product slicer affects all charts
- Clicking on charts filters other visuals

### Drill-Through (Optional)
1. Create second page: "Product Details"
2. Add drill-through from product bar chart
3. Show detailed metrics for selected product

---

## Step 6: Save and Export

### Save Dashboard
1. **File** → **Save As**
2. Save to: `powerbi/Sales_Analytics_Dashboard.pbix`

### Export Options
1. **Export to PDF**: File → Export → Export to PDF
2. **Save screenshots**: Use Snipping Tool for each visual
3. **Publish to web**: File → Publish to web (if sharing needed)

---

## Step 7: Screenshot Documentation

### Required Screenshots for Portfolio
1. **Full Dashboard View** → Save to `../assets/screenshots/dashboard_overview.png`
2. **KPI Cards** → Save to `../assets/screenshots/kpi_cards.png`
3. **Monthly Trends Chart** → Save to `../assets/screenshots/monthly_trends.png`
4. **Product Analysis** → Save to `../assets/screenshots/product_analysis.png`
5. **Regional Distribution** → Save to `../assets/screenshots/regional_sales.png`

---

## Expected Results

### Key Insights You Should See:
- **Total Revenue**: ~$254M across 2022-2023
- **Product D**: Highest revenue (~$55.8M)
- **West Region**: Leading region (~21.6% of sales)
- **Month 8**: Peak sales month
- **YoY Growth**: ~3.5% from 2022 to 2023
- **Avg Order Value**: ~$2,541

### Dashboard Features:
✅ Interactive filtering
✅ Cross-chart highlighting  
✅ Professional formatting
✅ Key business metrics
✅ Trend analysis
✅ Geographic insights
✅ Product performance ranking

---

## Troubleshooting

### Common Issues:
1. **Data not loading**: Check file path and permissions
2. **Date formatting**: Ensure date column is recognized as Date type
3. **Measures not calculating**: Verify DAX syntax
4. **Charts not filtering**: Check relationships and interactions

### Tips:
- Use **Data view** to verify data import
- Use **Model view** to check relationships
- Test slicers individually
- Save frequently during development

---

## Next Steps After Creation:
1. Take screenshots for portfolio
2. Update insights.md with Power BI findings
3. Add dashboard images to README.md
4. Commit Power BI file to Git repository
