
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dataset"

# Load datasets
transactions = pd.read_csv(DATA_DIR / "retail_transactions_100k.csv")
products = pd.read_csv(DATA_DIR / "products_650.csv")
customers = pd.read_csv(DATA_DIR / "customers_12k.csv")
stores = pd.read_csv(DATA_DIR / "stores_35.csv")

# Overall business performance
total_orders = transactions["OrderID"].nunique()
total_sales = transactions["NetSales"].sum()
total_profit = transactions["Profit"].sum()
total_discount = transactions["DiscountAmount"].sum()
total_returns = transactions["ReturnAmount"].sum()

profit_margin = (total_profit / total_sales) * 100

print("\n========== BUSINESS INSIGHTS ==========")

print("\n1. OVERALL BUSINESS PERFORMANCE")
print("Total Orders:", total_orders)
print("Net Sales: ₹", round(total_sales, 2))
print("Total Profit: ₹", round(total_profit, 2))
print("Profit Margin:", round(profit_margin, 2), "%")
print("Total Discounts: ₹", round(total_discount, 2))
print("Total Returns: ₹", round(total_returns, 2))

# Category performance
category_data = transactions.merge(
    products[["ProductID", "Category"]],
    on="ProductID",
    how="left"
)

category_sales = category_data.groupby("Category")["NetSales"].sum()

print("\n2. CATEGORY PERFORMANCE")
print(category_sales.sort_values(ascending=False))

print(
    "Best Performing Category:",
    category_sales.idxmax()
)

# Brand performance
brand_data = transactions.merge(
    products[["ProductID", "Brand"]],
    on="ProductID",
    how="left"
)

brand_sales = brand_data.groupby("Brand")["NetSales"].sum()

print("\n3. BRAND PERFORMANCE")
print("Top Brand:", brand_sales.idxmax())
print("Top Brand Sales: ₹", round(brand_sales.max(), 2))

# Customer segment performance
customer_data = transactions.merge(
    customers[["CustomerID", "CustomerSegment"]],
    on="CustomerID",
    how="left"
)

segment_sales = customer_data.groupby(
    "CustomerSegment"
)["NetSales"].sum()

print("\n4. CUSTOMER SEGMENT PERFORMANCE")
print(segment_sales.sort_values(ascending=False))
print("Top Customer Segment:", segment_sales.idxmax())

# Regional performance
regional_data = transactions.merge(
    stores[["StoreID", "Region"]],
    on="StoreID",
    how="left"
)

region_sales = regional_data.groupby("Region")["NetSales"].sum()

print("\n5. REGIONAL PERFORMANCE")
print(region_sales.sort_values(ascending=False))
print("Top Performing Region:", region_sales.idxmax())

# Payment mode analysis
payment_sales = transactions.groupby("PaymentMode")["NetSales"].sum()

print("\n6. PAYMENT MODE")
print("Most Successful Payment Mode:", payment_sales.idxmax())

# Sales channel analysis
channel_sales = transactions.groupby("SalesChannel")["NetSales"].sum()

print("\n7. SALES CHANNEL")
print("Top Sales Channel:", channel_sales.idxmax())

# Return analysis
returned_orders = transactions[
    transactions["ReturnFlag"] == True
]["OrderID"].nunique()

return_rate = (returned_orders / total_orders) * 100

print("\n8. RETURN ANALYSIS")
print("Returned Orders:", returned_orders)
print("Return Rate:", round(return_rate, 2), "%")

print("\n========== BUSINESS INSIGHTS COMPLETED ==========")
