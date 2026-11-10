# Retail Sales Analysis — Data Visualization Report

## 1. Project Overview
This report summarizes the visual analysis of a synthetic retail sales dataset covering January 2023 to December 2025.

## 2. Dataset Overview
- Transactions: 100,000 records
- Customers: 12,000 records
- Products: 650 records
- Stores: 35 records
- Calendar: 1,096 records

## 3. Visualizations Created

| No. | Visualization | File |
|---|---|---|
| 1 | Year-wise Sales Trend | 01_yearly_sales_trend.png |
| 2 | Monthly Sales Trend | 02_monthly_sales_trend.png |
| 3 | Category-wise Sales | 03_category_sales.png |
| 4 | Top 10 Brands | 04_top_10_brands.png |
| 5 | Top 10 Products | 05_top_10_products.png |
| 6 | Customer Segment Sales | 06_customer_segment_sales.png |
| 7 | Regional Sales | 07_regional_sales.png |
| 8 | Payment Mode Sales | 08_payment_mode_sales.png |
| 9 | Sales Channel Sales | 09_sales_channel_sales.png |
| 10 | Discount Impact on Profit Margin | 10_discount_impact_profit_margin.png |
| 11 | Return Rate by Category | 11_return_rate_by_category.png |
| 12 | Correlation Heatmap | 12_correlation_heatmap.png |

## 4. Key Visual Findings

1. HomeNest is the highest-selling brand, generating approximately ₹25.40 crore in net sales.
2. Electronics Item 109 is the top product, generating approximately ₹2.07 crore.
3. Consumer customers contribute approximately ₹147.31 crore in net sales.
4. East is the highest-performing region, generating approximately ₹54.95 crore.
5. UPI is the leading payment mode, with approximately ₹80.77 crore in net sales.
6. Mobile App is the leading sales channel, generating approximately ₹61.46 crore.
7. Electronics has the highest category return rate at approximately 4.17%.
8. Profit margin decreases across higher discount categories in this dataset, from approximately 46.73% with no discount to 27.83% above 20% discount.
9. Net Sales and Profit have a strong positive correlation of 0.94.

## 5. Technical Implementation

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

All visualizations were generated using Python scripts and saved as high-resolution PNG files.

## 6. Verification

All 12 expected visualization files were successfully verified in the `visualizations/` directory.

**Verification Result: 12/12 charts found.**

## 7. Conclusion

The visualization phase provides a graphical overview of retail sales performance across time, products, brands, customers, regions, payment modes, and sales channels. It also highlights patterns involving discounts, returns, and numerical relationships.

These visualizations can support business reporting and the development of an interactive Power BI dashboard.

*Note: The dataset is synthetic. Correlation does not establish causation, and observed patterns should not be interpreted as proof of real-world business causes.*
