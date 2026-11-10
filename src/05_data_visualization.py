
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "dataset"
VISUAL_DIR = BASE_DIR / "visualizations"

# Create visualization folder if it doesn't exist
VISUAL_DIR.mkdir(parents=True, exist_ok=True)

# Load datasets
transactions = pd.read_csv(DATA_DIR / "retail_transactions_100k.csv")
customers = pd.read_csv(DATA_DIR / "customers_12k.csv")
products = pd.read_csv(DATA_DIR / "products_650.csv")
stores = pd.read_csv(DATA_DIR / "stores_35.csv")
calendar = pd.read_csv(DATA_DIR / "calendar_2023_2025.csv")

# Convert date columns
transactions["OrderDate"] = pd.to_datetime(transactions["OrderDate"])

# Visualization settings
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

print("All datasets loaded successfully!")
print("Transactions:", transactions.shape)
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Stores:", stores.shape)
print("Calendar:", calendar.shape)

print("\nVisualization environment is ready!")
print("Output Directory:", VISUAL_DIR)





# ==========================================
# 1. YEAR-WISE SALES TREND
# ==========================================

# yearly_sales = transactions.groupby("OrderYear")["NetSales"].sum()

# plt.figure(figsize=(10, 6))

# sns.barplot(
#     x=yearly_sales.index.astype(str),
#     y=yearly_sales.values
# )

# plt.title("Year-wise Net Sales Performance", fontsize=16)
# plt.xlabel("Year")
# plt.ylabel("Net Sales (₹)")
# plt.tight_layout()

# # Save chart
# plt.savefig(
#     VISUAL_DIR / "01_yearly_sales_trend.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nYear-wise Sales Chart Generated Successfully!")
# print(yearly_sales)






# ==========================================
# 2. MONTHLY SALES TREND
# ==========================================

# transactions["OrderMonth"] = pd.to_datetime(
#     transactions["OrderDate"]
# ).dt.to_period("M")

# monthly_sales = transactions.groupby(
#     "OrderMonth"
# )["NetSales"].sum()

# plt.figure(figsize=(14, 6))

# sns.lineplot(
#     x=monthly_sales.index.astype(str),
#     y=monthly_sales.values,
#     marker="o"
# )

# plt.title("Monthly Net Sales Trend (2023-2025)", fontsize=16)
# plt.xlabel("Month")
# plt.ylabel("Net Sales (₹)")
# plt.xticks(rotation=90)

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "02_monthly_sales_trend.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nMonthly Sales Chart Generated Successfully!")
# print(monthly_sales)





# ==========================================
# 3. CATEGORY-WISE SALES ANALYSIS
# ==========================================

# category_data = transactions.merge(
#     products[["ProductID", "Category"]],
#     on="ProductID",
#     how="left"
# )

# category_sales = category_data.groupby(
#     "Category"
# )["NetSales"].sum().sort_values(ascending=False)

# plt.figure(figsize=(12, 6))

# sns.barplot(
#     x=category_sales.values,
#     y=category_sales.index
# )

# plt.title("Category-wise Net Sales Performance", fontsize=16)
# plt.xlabel("Net Sales (₹)")
# plt.ylabel("Product Category")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "03_category_sales.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nCategory Sales Chart Generated Successfully!")
# print(category_sales)




# ==========================================
# 4. TOP 10 BRANDS BY SALES
# ==========================================

# brand_data = transactions.merge(
#     products[["ProductID", "Brand"]],
#     on="ProductID",
#     how="left"
# )

# brand_sales = (
#     brand_data.groupby("Brand")["NetSales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# plt.figure(figsize=(12, 7))

# sns.barplot(
#     x=brand_sales.values,
#     y=brand_sales.index
# )

# plt.title("Top 10 Brands by Net Sales", fontsize=16)
# plt.xlabel("Net Sales (₹)")
# plt.ylabel("Brand")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "04_top_10_brands.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nTop 10 Brands Chart Generated Successfully!")
# print(brand_sales)



# ==========================================
# 5. TOP 10 PRODUCTS BY SALES
# ==========================================

# product_data = transactions.merge(
#     products[["ProductID", "ProductName"]],
#     on="ProductID",
#     how="left"
# )

# product_sales = (
#     product_data.groupby("ProductName")["NetSales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# plt.figure(figsize=(12, 7))

# sns.barplot(
#     x=product_sales.values,
#     y=product_sales.index
# )

# plt.title("Top 10 Products by Net Sales", fontsize=16)
# plt.xlabel("Net Sales (₹)")
# plt.ylabel("Product Name")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "05_top_10_products.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nTop 10 Products Chart Generated Successfully!")
# print(product_sales)



# ==========================================
# 6. CUSTOMER SEGMENT SALES
# ==========================================

# customer_data = transactions.merge(
#     customers[["CustomerID", "CustomerSegment"]],
#     on="CustomerID",
#     how="left"
# )

# segment_sales = (
#     customer_data.groupby("CustomerSegment")["NetSales"]
#     .sum()
#     .sort_values(ascending=False)
# )

# plt.figure(figsize=(10, 6))

# sns.barplot(
#     x=segment_sales.index,
#     y=segment_sales.values
# )

# plt.title("Customer Segment-wise Net Sales", fontsize=16)
# plt.xlabel("Customer Segment")
# plt.ylabel("Net Sales (₹)")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "06_customer_segment_sales.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nCustomer Segment Sales Chart Generated Successfully!")
# print(segment_sales)





# ==========================================
# 7. REGIONAL SALES PERFORMANCE
# ==========================================

# regional_data = transactions.merge(
#     stores[["StoreID", "Region"]],
#     on="StoreID",
#     how="left"
# )

# region_sales = (
#     regional_data.groupby("Region")["NetSales"]
#     .sum()
#     .sort_values(ascending=False)
# )

# plt.figure(figsize=(10, 6))

# sns.barplot(
#     x=region_sales.index,
#     y=region_sales.values
# )

# plt.title("Region-wise Net Sales Performance", fontsize=16)
# plt.xlabel("Region")
# plt.ylabel("Net Sales (₹)")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "07_regional_sales.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nRegional Sales Chart Generated Successfully!")
# print(region_sales)



# ==========================================
# 8. PAYMENT MODE SALES ANALYSIS
# ==========================================

# payment_sales = (
#     transactions.groupby("PaymentMode")["NetSales"]
#     .sum()
#     .sort_values(ascending=False)
# )

# plt.figure(figsize=(10, 6))

# sns.barplot(
#     x=payment_sales.index,
#     y=payment_sales.values
# )

# plt.title("Payment Mode-wise Net Sales", fontsize=16)
# plt.xlabel("Payment Mode")
# plt.ylabel("Net Sales (₹)")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "08_payment_mode_sales.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nPayment Mode Sales Chart Generated Successfully!")
# print(payment_sales)




# ==========================================
# 9. SALES CHANNEL ANALYSIS
# ==========================================

# channel_sales = (
#     transactions.groupby("SalesChannel")["NetSales"]
#     .sum()
#     .sort_values(ascending=False)
# )

# plt.figure(figsize=(10, 6))

# sns.barplot(
#     x=channel_sales.index,
#     y=channel_sales.values
# )

# plt.title("Sales Channel-wise Net Sales", fontsize=16)
# plt.xlabel("Sales Channel")
# plt.ylabel("Net Sales (₹)")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "09_sales_channel_sales.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nSales Channel Chart Generated Successfully!")
# print(channel_sales)



# ==========================================
# 10. DISCOUNT IMPACT ON PROFIT MARGIN
# ==========================================

# transactions["DiscountCategory"] = pd.cut(
#     transactions["DiscountPercent"],
#     bins=[-0.001, 0, 0.05, 0.10, 0.20, 1],
#     labels=[
#         "No Discount",
#         "0-5%",
#         "5-10%",
#         "10-20%",
#         "Above 20%"
#     ]
# )

# discount_analysis = transactions.groupby(
#     "DiscountCategory",
#     observed=False
# ).agg(
#     Total_Sales=("NetSales", "sum"),
#     Total_Profit=("Profit", "sum")
# )

# discount_analysis["Profit_Margin"] = (
#     discount_analysis["Total_Profit"]
#     / discount_analysis["Total_Sales"]
# ) * 100

# plt.figure(figsize=(11, 6))

# sns.barplot(
#     x=discount_analysis.index.astype(str),
#     y=discount_analysis["Profit_Margin"]
# )

# plt.title("Discount Impact on Profit Margin", fontsize=16)
# plt.xlabel("Discount Category")
# plt.ylabel("Profit Margin (%)")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "10_discount_impact_profit_margin.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nDiscount Impact Chart Generated Successfully!")
# print(discount_analysis)


# ==========================================
# 11. RETURN RATE BY CATEGORY
# ==========================================

# return_data = transactions.merge(
#     products[["ProductID", "Category"]],
#     on="ProductID",
#     how="left"
# )

# category_returns = return_data.groupby("Category").agg(
#     Total_Orders=("OrderID", "nunique"),
#     Returned_Orders=("ReturnFlag", "sum")
# )

# category_returns["Return_Rate"] = (
#     category_returns["Returned_Orders"]
#     / category_returns["Total_Orders"]
# ) * 100

# category_returns = category_returns.sort_values(
#     "Return_Rate",
#     ascending=False
# )

# plt.figure(figsize=(11, 6))

# sns.barplot(
#     x=category_returns.index,
#     y=category_returns["Return_Rate"]
# )

# plt.title("Return Rate by Product Category", fontsize=16)
# plt.xlabel("Product Category")
# plt.ylabel("Return Rate (%)")

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "11_return_rate_by_category.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nReturn Rate Chart Generated Successfully!")
# print(category_returns)





# ==========================================
# 12. CORRELATION HEATMAP
# ==========================================

# correlation_data = transactions[
#     [
#         "Quantity",
#         "GrossSales",
#         "DiscountAmount",
#         "ReturnAmount",
#         "NetSales",
#         "COGS",
#         "Profit"
#     ]
# ]

# correlation_matrix = correlation_data.corr()

# plt.figure(figsize=(12, 8))

# sns.heatmap(
#     correlation_matrix,
#     annot=True,
#     cmap="coolwarm",
#     fmt=".2f",
#     linewidths=0.5
# )

# plt.title("Retail Sales Correlation Heatmap", fontsize=16)

# plt.tight_layout()

# plt.savefig(
#     VISUAL_DIR / "12_correlation_heatmap.png",
#     dpi=300,
#     bbox_inches="tight"
# )

# plt.show()

# print("\nCorrelation Heatmap Generated Successfully!")
# print(correlation_matrix.round(2))


# ==========================================
# FINAL VISUALIZATION VERIFICATION
# ==========================================

expected_charts = [
    "01_yearly_sales_trend.png",
    "02_monthly_sales_trend.png",
    "03_category_sales.png",
    "04_top_10_brands.png",
    "05_top_10_products.png",
    "06_customer_segment_sales.png",
    "07_regional_sales.png",
    "08_payment_mode_sales.png",
    "09_sales_channel_sales.png",
    "10_discount_impact_profit_margin.png",
    "11_return_rate_by_category.png",
    "12_correlation_heatmap.png"
]

print("\n========== FINAL CHART VERIFICATION ==========")

for chart in expected_charts:
    chart_path = VISUAL_DIR / chart

    if chart_path.exists():
        print(f"{chart} : FOUND")
    else:
        print(f"{chart} : MISSING")

total_found = sum(
    (VISUAL_DIR / chart).exists()
    for chart in expected_charts
)

print("\nTotal Charts Found:", total_found, "/ 12")
print("\nVisualization Verification Completed!")







