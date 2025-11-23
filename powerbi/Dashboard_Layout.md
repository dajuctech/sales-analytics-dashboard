# Power BI Dashboard Visual Layout Guide

## Dashboard Canvas Layout (1280x720)

```
┌─────────────────────────────────────────────────────────────┐
│                 SALES ANALYTICS DASHBOARD                   │
├─────────────────────────────────────────────────────────────┤
│ [Total Revenue] [Total Quantity] [Avg Order] [Transactions] │
│     $254M           254K          $2,541        10K         │
├─────────────────────────────────────────────────────────────┤
│                                                    ┌──────┐ │
│ ┌─────────────────────────────────────────┐        │YEAR  │ │
│ │          Monthly Revenue Trends          │        │☐2022 │ │
│ │                                         │        │☐2023 │ │
│ │    $25M ┌─┐                            │        ├──────┤ │
│ │         │ │     ┌─┐                    │        │REGION│ │
│ │    $20M │ │ ┌─┐ │ │ ┌─┐               │        │☐North│ │
│ │         │ │ │ │ │ │ │ │               │        │☐South│ │
│ │    $15M │ │ │ │ │ │ │ │               │        │☐East │ │
│ │         └─┘ └─┘ └─┘ └─┘               │        │☐West │ │
│ │         Jan Feb Mar Apr...            │        │☐Centr│ │
│ └─────────────────────────────────────────┘        ├──────┤ │
│                                                    │PRODCT│ │
│ ┌─────────────────────┐ ┌─────────────────────┐    │ ▼ A  │ │
│ │  Revenue by Product │ │Sales by Region      │    └──────┘ │
│ │                     │ │                     │              │
│ │Product D ████████   │ │    ┌─────────────┐  │              │
│ │Product E ███████    │ │   ╱  West 21.6%  ╲ │              │
│ │Product C ██████     │ │  ╱               ╲ │              │
│ │Product B ██████     │ │ │ South  East    │ │              │
│ │Product A ██████     │ │ │ 19.7%  19.7%   │ │              │
│ │                     │ │  ╲  North 19.4% ╱  │              │
│ │   $0M  $20M  $40M   │ │   ╲ Central    ╱   │              │
│ └─────────────────────┘ │    ╲ 19.6%   ╱     │              │
│                         │     └─────────┘     │              │
│ ┌─────────────────────┐ └─────────────────────┘              │
│ │ Annual Comparison   │                                      │
│ │                     │                                      │
│ │ $140M ┌───┐  ┌───┐  │                                      │
│ │       │   │  │   │  │                                      │
│ │ $120M │2022  │2023 │  │                                      │
│ │       │   │  │   │  │                                      │
│ │ $100M └───┘  └───┘  │                                      │
│ └─────────────────────┘                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Visual Specifications

### 1. Header Section (Top 10%)
- **Title**: "SALES ANALYTICS DASHBOARD"
- **Font**: Segoe UI, 28pt, Bold
- **Color**: #2C3E50 (Dark Blue)
- **Background**: #F8F9FA (Light Gray)

### 2. KPI Cards Row (15%)
**Layout**: 4 cards horizontally aligned

#### Card 1: Total Revenue
- **Size**: 300x120px
- **Background**: Gradient blue (#3498DB → #2980B9)
- **Text Color**: White
- **Value**: "$254.1M" (32pt, Bold)
- **Label**: "Total Revenue" (14pt)
- **Icon**: 💰

#### Card 2: Total Quantity  
- **Size**: 300x120px
- **Background**: Gradient green (#27AE60 → #229954)
- **Text Color**: White
- **Value**: "254,118" (32pt, Bold)
- **Label**: "Total Quantity" (14pt)
- **Icon**: 📦

#### Card 3: Average Order Value
- **Size**: 300x120px
- **Background**: Gradient orange (#F39C12 → #E67E22)
- **Text Color**: White
- **Value**: "$2,541" (32pt, Bold)
- **Label**: "Avg Order Value" (14pt)
- **Icon**: 💳

#### Card 4: Total Transactions
- **Size**: 300x120px
- **Background**: Gradient purple (#9B59B6 → #8E44AD)
- **Text Color**: White
- **Value**: "10,000" (32pt, Bold)
- **Label**: "Transactions" (14pt)
- **Icon**: 📊

### 3. Main Charts Area (60%)

#### Monthly Revenue Trends (Top Left - 60% width)
- **Chart Type**: Line Chart
- **Size**: 760x280px
- **X-Axis**: Month (1-12)
- **Y-Axis**: Revenue ($0M - $25M)
- **Line Color**: #3498DB (Blue)
- **Markers**: Enabled, circle, 6px
- **Grid**: Horizontal only, light gray
- **Title**: "Monthly Revenue Trends" (18pt, Bold)

#### Revenue by Product (Bottom Left - 45% width)
- **Chart Type**: Horizontal Bar Chart
- **Size**: 560x240px
- **Bars**: 5 products (A, B, C, D, E)
- **Color Scheme**: Blue gradient
- **Data Labels**: Revenue values on bars
- **Title**: "Revenue by Product" (16pt, Bold)
- **Sort**: Descending by revenue

#### Sales by Region (Bottom Right - 45% width)
- **Chart Type**: Donut Chart
- **Size**: 400x240px
- **Colors**: Distinct colors for each region
- **Labels**: Region names + percentages
- **Legend**: Right side
- **Title**: "Sales Distribution by Region" (16pt, Bold)

#### Annual Comparison (Small Bottom Chart)
- **Chart Type**: Column Chart
- **Size**: 300x180px
- **Columns**: 2022, 2023
- **Color**: #27AE60 (Green)
- **Data Labels**: Revenue values on top
- **Title**: "Year over Year" (14pt, Bold)

### 4. Filters Panel (Right Side - 25%)

#### Year Slicer
- **Type**: List slicer
- **Options**: 2022, 2023
- **Multi-select**: Enabled
- **Size**: 200x80px

#### Region Slicer
- **Type**: List slicer  
- **Options**: North, South, East, West, Central
- **Multi-select**: Enabled
- **Size**: 200x150px

#### Product Slicer
- **Type**: Dropdown slicer
- **Options**: Product A, B, C, D, E
- **Multi-select**: Enabled  
- **Size**: 200x60px

---

## Color Palette

### Primary Colors
- **Blue**: #3498DB (Main theme)
- **Dark Blue**: #2C3E50 (Headers)
- **Light Blue**: #AED6F1 (Accents)

### Secondary Colors
- **Green**: #27AE60 (Positive metrics)
- **Orange**: #F39C12 (Warnings/Highlights)
- **Red**: #E74C3C (Negative metrics)
- **Purple**: #9B59B6 (Special metrics)

### Neutral Colors
- **White**: #FFFFFF (Background)
- **Light Gray**: #F8F9FA (Card backgrounds)
- **Medium Gray**: #BDC3C7 (Borders)
- **Dark Gray**: #34495E (Text)

---

## Interactive Features

### Cross-Filtering Behavior
1. **Year Slicer** → Affects all charts
2. **Region Slicer** → Affects all charts except regional breakdown
3. **Product Slicer** → Affects all charts except product ranking
4. **Chart Clicks** → Filter other visuals

### Hover Effects
- **Cards**: Slight shadow increase
- **Charts**: Highlight selected segment
- **Bars**: Show exact values in tooltip

### Animation
- **Chart Load**: 1.2 second fade-in
- **Filter Changes**: 0.8 second transition
- **Hover**: 0.3 second highlight

---

## Mobile Responsiveness (Optional)
- **Breakpoint**: 768px width
- **Layout**: Single column stack
- **Order**: KPIs → Charts → Filters
- **Touch**: Larger touch targets for mobile
