# Retail Sales Analysis – Data Understanding Report

## 1. Project Overview

This project analyzes synthetic retail sales data covering the period from 1 January 2023 to 31 December 2025.

The objective of this phase is to understand the datasets, inspect their structure, validate data quality, identify relationships, and investigate unusual numerical values.

## 2. Dataset Overview

| Dataset | Rows | Columns |
|---|---:|---:|
| Transactions | 100,000 | 20 |
| Customers | 12,000 | 6 |
| Products | 650 | 7 |
| Stores | 35 | 6 |
| Calendar | 1,096 | 7 |

Total records across datasets: 113,781.

## 3. Data Quality Checks

The following validations were performed:

- Checked dataset shapes and column names.
- Checked missing values.
- Checked blank and whitespace values.
- Checked duplicate records.
- Validated primary and foreign keys.
- Validated transaction dates against the calendar.
- Checked numerical columns for invalid negative values.
- Validated discount percentages.
- Checked GrossSales, DiscountAmount, NetSales, and Profit formulas.
- Validated return-related fields.
- Validated OrderMonth and OrderYear.

### Validation Results

- Missing values: 0 across all datasets.
- Duplicate rows: 0 across all datasets.
- Duplicate dimension keys: 0.
- Invalid foreign keys: 0.
- Invalid transaction dates: 0.
- Formula mismatches: 0.
- Invalid return conditions: 0.
- Invalid OrderMonth values: 0.
- Invalid OrderYear values: 0.

## 4. Dataset Relationships

Transactions is the central fact table.

It connects to four dimension tables:

| Fact Table | Dimension Table | Relationship |
|---|---|---|
| Transactions.CustomerID | Customers.CustomerID | Many-to-One |
| Transactions.ProductID | Products.ProductID | Many-to-One |
| Transactions.StoreID | Stores.StoreID | Many-to-One |
| Transactions.OrderDate | Calendar.Date | Many-to-One |

## 5. Categorical Analysis

The following observations were identified:

- UPI is the most frequently used payment mode.
- Mobile App is the most frequent sales channel.
- Consumer is the largest customer segment.
- Five product categories contain 109 products each.
- AeroFit has the highest product count among brands.
- East has the highest number of stores.
- Flagship is the most common store type.

No obvious inconsistent categorical values were identified.

## 6. Numerical and Outlier Analysis

The Interquartile Range (IQR) method was used to detect statistical outliers.

Outliers were observed in:

- UnitPrice: 7,105
- GrossSales: 9,642
- DiscountAmount: 11,871
- NetSales: 9,797
- COGS: 10,138
- Profit: 10,404

No IQR outliers were detected in Quantity or DiscountPercent.

The highest UnitPrice was investigated and identified as product P00072, an Electronics Audio product.

The lowest-profit transactions were also investigated. Negative profit values were consistent with the Profit calculation.

No outlier records were removed.

## 7. Profitability Analysis

| Profit Category | Transactions |
|---|---:|
| Profitable | 97,666 |
| Zero Profit | 2,241 |
| Loss-making | 93 |
| Total | 100,000 |

- Profitable transactions: 97.67%.
- Zero-profit transactions: 2.241%.
- Loss-making transactions: 0.093%.
- Total net loss across loss-making transactions: ₹15,679.95.

## 8. Final Dataset Profile

| Dataset | Missing Values | Duplicate Rows | Memory Usage |
|---|---:|---:|---:|
| Transactions | 0 | 0 | 46.46 MB |
| Customers | 0 | 0 | 3.42 MB |
| Products | 0 | 0 | 0.19 MB |
| Stores | 0 | 0 | 0.01 MB |
| Calendar | 0 | 0 | 0.20 MB |

Total memory usage: 50.28 MB.

## 9. Conclusion

The Data Understanding phase established the structure, characteristics, quality, and relationships of the five retail datasets.

All performed validation checks passed. Statistical outliers were investigated without deleting records.

The datasets are ready to proceed to the next project phase, Data Cleaning, where any additional preparation requirements will be handled if identified.