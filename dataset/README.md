# Retail Sales Data Analysis Project Dataset

Synthetic retail dataset created for learning and portfolio practice.

## Files
- retail_transactions_100k.csv: 100,000 transaction rows (main fact table)
- customers_12k.csv: 12,000 customer records
- products_650.csv: 650 product records
- stores_35.csv: 35 store records
- calendar_2023_2025.csv: daily calendar table (2023-01-01 to 2025-12-31)

## Relationships
- retail_transactions_100k.CustomerID -> customers_12k.CustomerID
- retail_transactions_100k.ProductID -> products_650.ProductID
- retail_transactions_100k.StoreID -> stores_35.StoreID
- retail_transactions_100k.OrderDate -> calendar_2023_2025.Date

## Important measures
- GrossSales = Quantity * UnitPrice
- DiscountAmount = GrossSales * DiscountPercent
- NetSales = GrossSales - DiscountAmount - ReturnAmount
- COGS = UnitCost * (Quantity - ReturnQuantity)
- Profit = NetSales - COGS

## Notes
- All records are synthetic; no real customer or company data is included.
- Dataset covers three years: 2023, 2024 and 2025.
- Currency values are in INR (₹).
- The dataset is designed to be mostly clean so we can focus first on EDA and business analysis.
