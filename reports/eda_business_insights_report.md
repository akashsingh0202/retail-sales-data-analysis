# Retail Sales Analysis – Exploratory Data Analysis (EDA) Report

## 1. Project Overview

### Project Description

The Retail Sales Analysis project focuses on analyzing three years of retail transaction data (2023–2025) to understand business performance, sales trends, customer purchasing behaviour, product performance, and profitability.

The objective of this analysis is to extract meaningful business insights from retail datasets and support data-driven decision-making.

### Project Objectives

- Analyze overall sales and profit performance.
- Identify yearly, quarterly, monthly, and daily sales trends.
- Evaluate product category, subcategory, and brand performance.
- Understand customer purchasing behaviour and revenue contribution.
- Analyze regional, state, city, and store performance.
- Evaluate payment methods and sales channels.
- Understand the impact of discounts on profitability.
- Analyze product returns and their financial impact.
- Identify correlations and statistical outliers.
- Develop actionable business recommendations.

### Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Visual Studio Code

### Analysis Approach

The project follows a structured Exploratory Data Analysis approach:

1. Dataset loading and understanding.
2. Data quality assessment.
3. Data cleaning and validation.
4. Descriptive statistical analysis.
5. Business-focused exploratory analysis.
6. Correlation and outlier analysis.
7. Business insights and recommendations.






## 2. Dataset Summary

The project uses five interconnected datasets representing retail transactions, customers, products, stores, and calendar information.

| Dataset | Total Rows | Total Columns |
|---|---:|---:|
| Transactions | 100,000 | 20 |
| Customers | 12,000 | 6 |
| Products | 650 | 7 |
| Stores | 35 | 6 |
| Calendar | 1,096 | 7 |
| **Total** | **113,781** | **46** |

### Dataset Details

**1. Transactions Dataset**
- Contains 100,000 retail transaction records.
- Includes order dates, customer IDs, product IDs, quantities, sales, discounts, returns, costs, and profits.
- Covers the period from January 2023 to December 2025.

**2. Customers Dataset**
- Contains 12,000 customer records.
- Includes customer names, cities, states, customer segments, and signup dates.

**3. Products Dataset**
- Contains 650 product records.
- Includes product names, categories, subcategories, brands, selling prices, and costs.

**4. Stores Dataset**
- Contains 35 store records.
- Includes store names, cities, states, regions, and store types.

**5. Calendar Dataset**
- Contains 1,096 daily calendar records.
- Includes year, quarter, month, day name, and weekend information.

### Dataset Relationships

The Transactions dataset is connected to the four supporting datasets through common keys:

- Transactions[CustomerID] → Customers[CustomerID]
- Transactions[ProductID] → Products[ProductID]
- Transactions[StoreID] → Stores[StoreID]
- Transactions[OrderDate] → Calendar[Date]

All four relationships follow a Many-to-One structure from Transactions to the respective dimension datasets.


## 3. Overall Business Performance

### 3.1 Overall Sales Performance

The retail business generated the following results across 100,000 transactions during 2023–2025.

| Metric | Value |
|---|---:|
| Total Orders | 100,000 |
| Total Quantity Sold | 214,621 |
| Gross Sales | ₹219.48 Crore |
| Total Discount | ₹21.41 Crore |
| Total Return Amount | ₹4.71 Crore |
| Net Sales | ₹193.36 Crore |

### 3.2 Overall Profit Performance

| Metric | Value |
|---|---:|
| Total COGS | ₹114.17 Crore |
| Total Profit | ₹79.19 Crore |
| Profit Margin | 40.95% |
| Average Profit per Order | ₹7,918.62 |

### 3.3 Key Business Findings

1. The business generated approximately ₹193.36 crore in Net Sales.
2. Total Profit was approximately ₹79.19 crore.
3. The overall profit margin was 40.95%.
4. Discounts accounted for approximately ₹21.41 crore.
5. Returns accounted for approximately ₹4.71 crore.
6. The average quantity sold per order was approximately 2.15 units.

### 3.4 Business Interpretation

The business demonstrates substantial sales and profitability across the three-year period. However, discounts and product returns represent important areas for monitoring because they affect the final financial performance.

The profit figures are based on the dataset's defined Profit and COGS fields and should not be interpreted as net income after all operating expenses and taxes.


## 4. Time-Based Sales Trends

### 4.1 Yearly Sales Performance

| Year | Total Orders | Net Sales | Total Profit |
|---|---:|---:|---:|
| 2023 | 33,132 | ₹65.07 Cr | ₹26.55 Cr |
| 2024 | 33,400 | ₹64.56 Cr | ₹26.58 Cr |
| 2025 | 33,468 | ₹63.73 Cr | ₹26.06 Cr |

**Key Findings:**
- 2023 recorded the highest Net Sales.
- 2024 recorded the highest Total Profit.
- Orders increased slightly each year, while Net Sales declined.

### 4.2 Year-over-Year Growth

| Year | Sales Growth | Profit Growth | Orders Growth |
|---|---:|---:|---:|
| 2024 | -0.77% | +0.12% | +0.81% |
| 2025 | -1.28% | -1.94% | +0.20% |

Sales declined in both 2024 and 2025 despite an increase in order volume. This may indicate a decline in average sales value per order.

### 4.3 Quarterly Sales Trends

- Highest quarterly Net Sales: 2023 Q4 — approximately ₹17.48 crore.
- Highest quarterly Profit: 2023 Q4 — approximately ₹7.16 crore.
- Lowest quarterly Net Sales: 2025 Q2 — approximately ₹15.66 crore.
- Highest order count: 2024 Q4 — 8,471 orders.

### 4.4 Monthly Sales Trends

- Highest sales month: October 2023 — approximately ₹6.03 crore.
- Lowest sales month: February 2024 — approximately ₹4.79 crore.
- February showed relatively low sales across the observed years.

### 4.5 Daily Sales Trends

| Metric | Value |
|---|---:|
| Average Daily Net Sales | ₹17.64 Lakh |
| Average Daily Profit | ₹7.23 Lakh |
| Highest Sales Date | 19 January 2024 |
| Highest Daily Net Sales | ₹32.46 Lakh |
| Lowest Sales Date | 2 February 2025 |
| Lowest Daily Net Sales | ₹8.22 Lakh |

### 4.6 Business Interpretation

The yearly analysis shows a gradual decline in Net Sales even though order counts increased. This suggests that average order value and product mix should be investigated further.

The quarterly and monthly results also show variations in sales performance. October 2023 and the fourth quarter of 2023 were particularly strong. These patterns may be useful for future inventory and promotional planning, but seasonal causes cannot be confirmed from this analysis alone.



## 5. Product, Category & Brand Performance

### 5.1 Category-wise Sales Performance

| Category | Net Sales | Total Profit |
|---|---:|---:|
| Electronics | ₹95.65 Cr | ₹38.73 Cr |
| Home & Kitchen | ₹46.78 Cr | ₹20.11 Cr |
| Sports | ₹24.67 Cr | ₹9.78 Cr |
| Fashion | ₹12.40 Cr | ₹4.95 Cr |
| Beauty | ₹11.44 Cr | ₹4.61 Cr |
| Grocery | ₹2.42 Cr | ₹1.00 Cr |

**Key Findings:**
- Electronics was the leading category, contributing approximately 49.5% of total Net Sales.
- Home & Kitchen ranked second in Net Sales.
- Grocery recorded the lowest Net Sales.

### 5.2 Subcategory Performance

- Smartphones recorded the highest subcategory Net Sales at approximately ₹29.71 crore.
- Electronics Accessories ranked second at approximately ₹24.86 crore.
- Laptops ranked third at approximately ₹20.87 crore.
- Grocery / Personal Care recorded the lowest subcategory Net Sales at approximately ₹52.81 lakh.

### 5.3 Brand Performance

- HomeNest recorded the highest Net Sales at approximately ₹25.40 crore and the highest Profit at approximately ₹10.34 crore.
- AeroFit recorded the highest order count.
- Nova ranked second in Total Profit.
- GlowLab recorded the lowest Net Sales and Total Profit.

### 5.4 Top and Bottom Product Performance

**Top Products by Net Sales:**

| Product ID | Net Sales | Total Profit |
|---|---:|---:|
| P00109 | ₹2.07 Cr | ₹1.13 Cr |
| P00005 | ₹2.03 Cr | — |
| P00083 | ₹1.91 Cr | — |

P00109 was the top-performing product in both Net Sales and Total Profit.

**Bottom Product Findings:**
- P00399 recorded the lowest Net Sales at approximately ₹8,604.
- P00378 and P00369 were also among the lowest-revenue products.
- Most products in the bottom 10 revenue list belonged to the Grocery category.

### 5.5 Business Interpretation

Electronics is the strongest revenue-generating category and deserves close attention in inventory and product planning. HomeNest is the leading brand by both sales and profit,



## 6. Customer Analysis & Purchasing Behaviour

### 6.1 Customer Segment Performance

| Customer Segment | Unique Customers | Net Sales | Total Profit |
|---|---:|---:|---:|
| Consumer | 9,120 | ₹147.31 Cr | ₹60.35 Cr |
| Corporate | 1,667 | ₹26.53 Cr | ₹10.87 Cr |
| Small Business | 1,212 | ₹19.52 Cr | ₹7.96 Cr |

**Key Findings:**
- Consumer customers contributed approximately 76.2% of total Net Sales.
- Consumer was the largest segment by customers, revenue, and profit.
- Corporate ranked second in Net Sales.

### 6.2 Customer Purchasing Behaviour

| Metric | Value |
|---|---:|
| Total Registered Customers | 12,000 |
| Active Customers | 11,999 |
| Average Orders per Active Customer | 8.33 |
| Repeat Customers | 11,986 |
| One-Time Customers | 13 |
| Repeat Customer Percentage | 99.89% |
| One-Time Customer Percentage | 0.11% |

**Key Findings:**
- Almost all active customers placed more than one order during the three-year observation period.
- The highest order count by a single customer was 20.
- One registered customer had no recorded transactions.

### 6.3 Customer Revenue Contribution

- The top 10 customers contributed approximately ₹75.14 lakh, representing 0.39% of total Net Sales.
- The top 20% of active customers (2,399 customers) contributed approximately 41.48% of total Net Sales.
- Customer revenue was distributed across a broad customer base rather than being concentrated entirely among a small group.

### 6.4 Business Interpretation

The Consumer segment is the primary revenue driver and should remain an important focus for customer engagement and marketing strategies.

The high repeat-customer percentage indicates frequent purchasing activity during the observed three-year period. However, this is a transaction-based repeat-purchase measure, not a formal customer retention or cohort analysis.

The top 20% of customers contributed 41.48% of revenue, so the dataset does not show the classic 80/20 revenue contribution pattern.


## 7. Regional, State, City & Store Performance

### 7.1 Regional Sales Performance

| Region | Net Sales | Total Profit |
|---|---:|---:|
| East | ₹54.95 Cr | ₹22.62 Cr |
| West | ₹50.41 Cr | ₹20.61 Cr |
| North | ₹39.04 Cr | ₹15.96 Cr |
| South | ₹32.66 Cr | ₹13.30 Cr |
| Central | ₹16.30 Cr | ₹6.70 Cr |

**Key Findings:**
- East recorded the highest Net Sales and Total Profit.
- West ranked second in both metrics.
- Central recorded the lowest Net Sales.

### 7.2 State-wise Sales Performance

- Maharashtra recorded the highest Net Sales at approximately ₹44.52 crore.
- Gujarat ranked second at approximately ₹32.95 crore.
- Rajasthan recorded the lowest Net Sales at approximately ₹5.36 crore.

### 7.3 City-wise Sales Performance

- Ahmedabad recorded the highest city-wise Net Sales at approximately ₹27.55 crore.
- Bengaluru and Lucknow followed closely.
- Jaipur recorded the lowest city-wise Net Sales.

### 7.4 Store Performance

- S017 (Retail Store 17, West Flagship) recorded the highest Net Sales at approximately ₹5.89 crore and Profit of ₹2.43 crore.
- S011 (Retail Store 11, South Mall) recorded the lowest Net Sales.

### 7.5 Business Interpretation

The East region is the strongest regional contributor, while Maharashtra leads state-wise performance. Ahmedabad is the leading city by Net Sales.

The store analysis identifies S017 as the highest-performing store. Management can investigate the operational practices and sales mix of high-performing stores to identify practices that may be useful elsewhere.

*Note: Geographic results are based on store locations, not customer residential locations.*

---

## 8. Payment Mode & Sales Channel Analysis

### 8.1 Payment Mode Performance

| Payment Mode | Total Orders | Net Sales |
|---|---:|---:|
| UPI | 41,686 | ₹80.77 Cr |
| Credit Card | 22,065 | ₹42.59 Cr |
| Debit Card | 16,186 | ₹30.79 Cr |
| Cash | 8,023 | ₹15.75 Cr |
| Net Banking | 7,041 | ₹13.77 Cr |
| Wallet | 4,999 | ₹9.68 Cr |

**Key Findings:**
- UPI was the most frequently used payment mode.
- UPI contributed approximately 41.8% of total Net Sales.
- Wallet recorded the lowest order count and Net Sales.

### 8.2 Sales Channel Performance

| Sales Channel | Total Orders | Net Sales |
|---|---:|---:|
| Mobile App | 32,008 | ₹61.46 Cr |
| Online | 28,118 | ₹53.84 Cr |
| In-store | 24,874 | ₹48.71 Cr |
| Marketplace | 15,000 | ₹29.35 Cr |

**Key Findings:**
- Mobile App generated the highest Net Sales and order count.
- Mobile App contributed approximately 31.8% of total Net Sales.
- Marketplace recorded the lowest Net Sales.

### 8.3 Business Interpretation

UPI is the leading payment method, and the Mobile App is the leading sales channel. The business can continue improving its mobile shopping experience and payment convenience while monitoring the performance of other channels.

---

## 9. Discount Impact & Return Analysis

### 9.1 Discount Impact Analysis

| Discount Category | Total Orders | Net Sales | Profit Margin |
|---|---:|---:|---:|
| No Discount | 30,046 | ₹63.64 Cr | 46.73% |
| 0–5% | 12,082 | ₹24.44 Cr | 43.66% |
| 5–10% | 22,053 | ₹42.92 Cr | 40.89% |
| 10–20% | 27,878 | ₹49.82 Cr | 35.60% |
| Above 20% | 7,941 | ₹12.53 Cr | 27.83% |

**Key Findings:**
- Orders without discounts recorded the highest profit margin of 46.73%.
- Profit margin declined as discount levels increased across the analyzed groups.
- Orders receiving discounts above 20% recorded the lowest profit margin of 27.83%.

### 9.2 Return Analysis

| Metric | Value |
|---|---:|
| Total Orders | 100,000 |
| Returned Orders | 3,956 |
| Return Rate | 3.96% |
| Total Return Quantity | 5,083 |
| Total Return Amount | ₹4.71 Cr |
| Return Amount as % of Gross Sales | 2.14% |

**Category-wise Return Findings:**
- Electronics recorded the highest return amount at approximately ₹2.35 crore and a return rate of 4.17%.
- Beauty recorded a return rate of 4.16%.
- Grocery recorded the lowest return amount at approximately ₹5.75 lakh.

### 9.3 Business Interpretation

The analysis shows an association between higher discount levels and lower profit margins. However, this does not establish that discounts alone caused the reduction; product mix, pricing, and order characteristics may also contribute.

Electronics deserves further investigation because it has the highest return amount and return rate among the categories. Product quality, customer feedback, and return reasons should be examined before deciding on corrective actions.

---

## 10. Correlation & Outlier Analysis

### 10.1 Correlation Analysis

Important correlations identified in the dataset:

| Variable Relationship | Correlation |
|---|---:|
| Gross Sales and Net Sales | 0.99 |
| Net Sales and Profit | 0.94 |
| Gross Sales and Profit | 0.92 |
| Gross Sales and COGS | 0.97 |
| Discount Amount and Gross Sales | 0.71 |
| Discount Amount and Profit | 0.47 |
| Quantity and Profit | 0.35 |
| Return Amount and Profit | 0.02 |

**Key Findings:**
- Gross Sales and Net Sales have a very strong positive linear relationship.
- Net Sales and Profit also show a strong positive relationship.
- Discount Amount and Profit show a moderate positive correlation in the overall transaction data.
- Return Amount and Profit show almost no linear correlation.

Correlation measures association, not causation. Some strong relationships are expected because the financial variables are mathematically related.

### 10.2 Outlier Analysis

The Interquartile Range (IQR) method was used to identify statistically unusual observations.

| Column | Outlier Count | Outlier Percentage |
|---|---:|---:|
| GrossSales | 9,642 | 9.64% |
| DiscountAmount | 11,871 | 11.87% |
| NetSales | 9,797 | 9.80% |
| Profit | 10,404 | 10.40% |

**Key Findings:**
- DiscountAmount had the highest outlier percentage.
- Profit also contained a notable proportion of statistically unusual values.
- Outliers were not automatically removed because unusual financial values may represent valid high-value or low-value transactions.

---

## 11. Key Business Insights

The complete Exploratory Data Analysis produced the following major insights:

1. The business generated approximately ₹193.36 crore in Net Sales and ₹79.19 crore in Profit.
2. The overall profit margin was 40.95%.
3. Net Sales declined slightly across the three observed years, despite increasing order counts.
4. Electronics was the leading category, contributing approximately 49.5% of total Net Sales.
5. HomeNest was the top-performing brand by Net Sales and Profit.
6. The Consumer segment contributed approximately 76.2% of total Net Sales.
7. Repeat customers represented 99.89% of active customers during the observation period.
8. The East region generated the highest regional Net Sales.
9. Maharashtra was the highest-performing state by Net Sales.
10. UPI was the leading payment mode, while Mobile App was the leading sales channel.
11. Higher discount groups showed lower profit margins.
12. The overall return rate was 3.96%, with Electronics recording the highest category return rate.
13. DiscountAmount had the highest outlier percentage among the analyzed financial columns.

---

## 12. Business Recommendations

Based on the analysis, the following recommendations can be considered:

### 12.1 Improve Sales Growth
Investigate the decline in Net Sales despite increasing order counts. Monitor average order value, product mix, and customer spending patterns.

### 12.2 Focus on High-Performing Categories
Maintain strong inventory planning for Electronics and other high-revenue categories while exploring opportunities to improve lower-performing categories.

### 12.3 Review Discount Strategies
Evaluate the profitability of different discount bands. Avoid relying on large discounts without measuring their impact on profit margins.

### 12.4 Improve Return Management
Investigate the reasons behind Electronics and Beauty returns. Use product-level return information to identify recurring issues.

### 12.5 Strengthen Customer Engagement
Continue engaging repeat customers and develop suitable strategies for different customer segments.

### 12.6 Learn from High-Performing Stores
Study the sales mix and operational practices of top-performing stores such as S017 to identify potentially reusable practices.

### 12.7 Improve Digital Sales Experience
Continue improving the Mobile App experience and monitor the performance of Online and Marketplace channels.

### 12.8 Monitor Regional Performance
Study the factors contributing to the strong performance of the East and West regions and investigate improvement opportunities in Central.

---

## 13. Project Limitations

1. The dataset is synthetic and does not represent verified real-world retail company performance.
2. The analysis covers the period from 1 January 2023 to 31 December 2025.
3. Geographic analysis is based on store locations rather than customer residential locations.
4. The repeat-customer percentage is based on transactions across the complete observation period and is not a formal cohort-retention calculation.
5. Correlation does not establish causation.
6. The profit figures follow the dataset's defined Profit and COGS fields and may not include all operating expenses, taxes, or other financial adjustments.
7. Seasonal patterns and business causes require further investigation before making definitive conclusions.

---

## 14. Conclusion

The Retail Sales Analysis project examined 100,000 retail transactions along with customer, product, store, and calendar datasets covering 2023–2025.

Using Python, Pandas, NumPy, Matplotlib, and Seaborn, the project explored overall sales and profit performance, time-based trends, product and brand performance, customer purchasing behaviour, regional and store performance, payment methods, sales channels, discounts, returns, correlations, and outliers.

The analysis identified Electronics as the leading category, Consumer as the largest customer segment, East as the highest-performing region, UPI as the most-used payment method, and Mobile App as the leading sales channel.

The project also highlighted areas requiring further attention, including declining Net Sales, discount-related margin differences, and product returns.

Overall, this project demonstrates a structured data analysis workflow, including dataset understanding, data quality validation, exploratory analysis, business interpretation, and actionable recommendations.

---

## 15. Tools & Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub
- **Database:** MySQL
- **Dashboarding:** Power BI

**Project Repository:**  
https://github.com/akashsingh0202/retail-sales-data-analysis