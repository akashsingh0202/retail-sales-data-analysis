# ==========================================
# RETAIL SALES ANALYSIS
# PHASE 3: EXPLORATORY DATA ANALYSIS
# ==========================================

# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path


# Project Directory

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "dataset"


# Load Datasets

transactions = pd.read_csv(
    DATA_DIR / "retail_transactions_100k.csv"
)

customers = pd.read_csv(
    DATA_DIR / "customers_12k.csv"
)

products = pd.read_csv(
    DATA_DIR / "products_650.csv"
)

stores = pd.read_csv(
    DATA_DIR / "stores_35.csv"
)

calendar = pd.read_csv(
    DATA_DIR / "calendar_2023_2025.csv"
)


# Convert Date Columns

transactions["OrderDate"] = pd.to_datetime(
    transactions["OrderDate"]
)

customers["SignupDate"] = pd.to_datetime(
    customers["SignupDate"]
)

calendar["Date"] = pd.to_datetime(
    calendar["Date"]
)


# EDA Setup Confirmation

print("\n========== EDA SETUP ==========")

print("Transactions:", transactions.shape)
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Stores:", stores.shape)
print("Calendar:", calendar.shape)

print("\nAll datasets loaded successfully!")

print("\nEDA environment is ready!")



# ==========================================
# STEP 2: OVERALL SALES PERFORMANCE ANALYSIS
# ==========================================

print("\n========== OVERALL SALES PERFORMANCE ==========")

# 1. Total Orders
total_orders = transactions["OrderID"].nunique()

# 2. Total Quantity Sold
total_quantity = transactions["Quantity"].sum()

# 3. Gross Sales
gross_sales = transactions["GrossSales"].sum()

# 4. Total Discount
total_discount = transactions["DiscountAmount"].sum()

# 5. Total Return Amount
total_returns = transactions["ReturnAmount"].sum()

# 6. Net Sales
net_sales = transactions["NetSales"].sum()


# Display Results

print("Total Orders:", total_orders)

print("Total Quantity Sold:", total_quantity)

print("Gross Sales:", round(gross_sales, 2))

print("Total Discount:", round(total_discount, 2))

print("Total Return Amount:", round(total_returns, 2))

print("Net Sales:", round(net_sales, 2))




# ==========================================
# STEP 3: OVERALL PROFIT PERFORMANCE
# ==========================================

print("\n========== OVERALL PROFIT PERFORMANCE ==========")

# 1. Total Cost of Goods Sold
total_cogs = transactions["COGS"].sum()

# 2. Total Profit
total_profit = transactions["Profit"].sum()

# 3. Profit Margin
profit_margin = (total_profit / net_sales) * 100

# 4. Average Profit per Order
average_profit_per_order = total_profit / total_orders


# Display Results

print("Total COGS:", round(total_cogs, 2))

print("Total Profit:", round(total_profit, 2))

print("Profit Margin (%):", round(profit_margin, 2))

print(
    "Average Profit per Order:",
    round(average_profit_per_order, 2)
)


# ==========================================
# STEP 4: DESCRIPTIVE STATISTICS ANALYSIS
# ==========================================

print("\n========== DESCRIPTIVE STATISTICS ==========")

columns = [
    "Quantity",
    "GrossSales",
    "DiscountAmount",
    "ReturnAmount",
    "NetSales",
    "COGS",
    "Profit"
]

statistics = transactions[columns].describe()

print(statistics.round(2))




# ==========================================
# STEP 5: YEARLY SALES ANALYSIS
# ==========================================

print("\n========== YEARLY SALES ANALYSIS ==========")

yearly_sales = transactions.groupby("OrderYear").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Gross_Sales=("GrossSales", "sum"),
    Total_Discount=("DiscountAmount", "sum"),
    Total_Returns=("ReturnAmount", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

print(yearly_sales.round(2))



# ==========================================
# STEP 6: QUARTERLY SALES ANALYSIS
# ==========================================

print("\n========== QUARTERLY SALES ANALYSIS ==========")

transactions["OrderQuarter"] = (
    transactions["OrderDate"].dt.to_period("Q")
)

quarterly_sales = transactions.groupby(
    transactions["OrderDate"].dt.to_period("Q")
).agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Gross_Sales=("GrossSales", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

print(quarterly_sales.round(2))




# ==========================================
# STEP 7: MONTHLY SALES TREND ANALYSIS
# ==========================================

print("\n========== MONTHLY SALES TREND ANALYSIS ==========")

monthly_sales = transactions.groupby(
    transactions["OrderDate"].dt.to_period("M")
).agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Gross_Sales=("GrossSales", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

print(monthly_sales.round(2))


# Highest and Lowest Sales Months

highest_sales_month = monthly_sales["Net_Sales"].idxmax()

lowest_sales_month = monthly_sales["Net_Sales"].idxmin()

print("\nHighest Sales Month:", highest_sales_month)

print("Highest Monthly Net Sales:",
      round(monthly_sales["Net_Sales"].max(), 2))

print("\nLowest Sales Month:", lowest_sales_month)

print("Lowest Monthly Net Sales:",
      round(monthly_sales["Net_Sales"].min(), 2))



# ==========================================
# STEP 8: DAILY SALES TREND ANALYSIS
# ==========================================

print("\n========== DAILY SALES TREND ANALYSIS ==========")

daily_sales = transactions.groupby("OrderDate").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nDaily Sales Summary:")
print(daily_sales.describe().round(2))


# Highest and Lowest Sales Days

highest_sales_day = daily_sales["Net_Sales"].idxmax()

lowest_sales_day = daily_sales["Net_Sales"].idxmin()

print("\nHighest Sales Date:", highest_sales_day)

print(
    "Highest Daily Net Sales:",
    round(daily_sales["Net_Sales"].max(), 2)
)

print("\nLowest Sales Date:", lowest_sales_day)

print(
    "Lowest Daily Net Sales:",
    round(daily_sales["Net_Sales"].min(), 2)
)







# ==========================================
# STEP 9: SALES GROWTH ANALYSIS
# ==========================================

print("\n========== SALES GROWTH ANALYSIS ==========")

yearly_growth = transactions.groupby("OrderYear").agg(
    Total_Orders=("OrderID", "nunique"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

# Calculate Year-over-Year Growth

yearly_growth["Sales_Growth_%"] = (
    yearly_growth["Net_Sales"].pct_change() * 100
)

yearly_growth["Profit_Growth_%"] = (
    yearly_growth["Total_Profit"].pct_change() * 100
)

yearly_growth["Orders_Growth_%"] = (
    yearly_growth["Total_Orders"].pct_change() * 100
)

print(yearly_growth.round(2))




# ==========================================
# STEP 10: PRODUCT CATEGORY SALES ANALYSIS
# ==========================================

print("\n========== PRODUCT CATEGORY SALES ANALYSIS ==========")

# Transactions ko Products dataset ke saath merge karna
category_data = transactions.merge(
    products[["ProductID", "Category"]],
    on="ProductID",
    how="left"
)

# Category-wise performance
category_sales = category_data.groupby("Category").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

# Highest sales category
category_sales = category_sales.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nCategory-wise Sales Performance:")
print(category_sales.round(2))

print("\nHighest Sales Category:")
print(category_sales["Net_Sales"].idxmax())

print("\nLowest Sales Category:")
print(category_sales["Net_Sales"].idxmin())



# ==========================================
# STEP 11: SUBCATEGORY SALES ANALYSIS
# ==========================================

print("\n========== SUBCATEGORY SALES ANALYSIS ==========")

subcategory_data = transactions.merge(
    products[["ProductID", "Category", "SubCategory"]],
    on="ProductID",
    how="left"
)

subcategory_sales = subcategory_data.groupby(
    ["Category", "SubCategory"]
).agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

subcategory_sales = subcategory_sales.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nSubcategory-wise Sales Performance:")
print(subcategory_sales.round(2))

print("\nTop Performing Subcategory:")
print(subcategory_sales["Net_Sales"].idxmax())

print("\nLowest Performing Subcategory:")
print(subcategory_sales["Net_Sales"].idxmin())






# ==========================================
# STEP 12: TOP & BOTTOM PRODUCTS ANALYSIS
# ==========================================

print("\n========== TOP & BOTTOM PRODUCTS ANALYSIS ==========")

product_data = transactions.merge(
    products[["ProductID", "ProductName", "Category"]],
    on="ProductID",
    how="left"
)

product_sales = product_data.groupby(
    ["ProductID", "ProductName", "Category"]
).agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

# Top 10 products by Net Sales
top_products = product_sales.sort_values(
    by="Net_Sales",
    ascending=False
).head(10)

print("\nTop 10 Products by Net Sales:")
print(top_products.round(2))


# Bottom 10 products by Net Sales
bottom_products = product_sales.sort_values(
    by="Net_Sales",
    ascending=True
).head(10)

print("\nBottom 10 Products by Net Sales:")
print(bottom_products.round(2))


# Top 10 products by Profit
top_profit_products = product_sales.sort_values(
    by="Total_Profit",
    ascending=False
).head(10)

print("\nTop 10 Products by Profit:")
print(top_profit_products.round(2))






# ==========================================
# STEP 13: BRAND PERFORMANCE ANALYSIS
# ==========================================

print("\n========== BRAND PERFORMANCE ANALYSIS ==========")

brand_data = transactions.merge(
    products[["ProductID", "Brand"]],
    on="ProductID",
    how="left"
)

brand_performance = brand_data.groupby("Brand").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

brand_performance = brand_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nBrand-wise Performance:")
print(brand_performance.round(2))

print("\nHighest Revenue Brand:")
print(brand_performance["Net_Sales"].idxmax())

print("\nLowest Revenue Brand:")
print(brand_performance["Net_Sales"].idxmin())

print("\nHighest Profit Brand:")
print(brand_performance["Total_Profit"].idxmax())





# ==========================================
# STEP 14: CUSTOMER SEGMENT ANALYSIS
# ==========================================

print("\n========== CUSTOMER SEGMENT ANALYSIS ==========")

segment_data = transactions.merge(
    customers[["CustomerID", "CustomerSegment"]],
    on="CustomerID",
    how="left"
)

segment_performance = segment_data.groupby("CustomerSegment").agg(
    Total_Orders=("OrderID", "nunique"),
    Unique_Customers=("CustomerID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

segment_performance = segment_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nCustomer Segment Performance:")
print(segment_performance.round(2))

print("\nHighest Revenue Segment:")
print(segment_performance["Net_Sales"].idxmax())

print("\nLowest Revenue Segment:")
print(segment_performance["Net_Sales"].idxmin())

print("\nHighest Profit Segment:")
print(segment_performance["Total_Profit"].idxmax())







# ==========================================
# STEP 15: CUSTOMER PURCHASING BEHAVIOUR
# ==========================================

print("\n========== CUSTOMER PURCHASING BEHAVIOUR ==========")

customer_behavior = transactions.groupby("CustomerID").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nCustomer Behaviour Summary:")
print(customer_behavior.describe().round(2))


# Repeat and One-Time Customers

repeat_customers = (
    customer_behavior["Total_Orders"] > 1
).sum()

one_time_customers = (
    customer_behavior["Total_Orders"] == 1
).sum()

total_customers = customer_behavior.shape[0]

print("\nTotal Active Customers:", total_customers)
print("Repeat Customers:", repeat_customers)
print("One-Time Customers:", one_time_customers)

print(
    "Repeat Customer Percentage:",
    round((repeat_customers / total_customers) * 100, 2)
)

print(
    "One-Time Customer Percentage:",
    round((one_time_customers / total_customers) * 100, 2)
)


# Top 10 Customers by Orders

top_customers = customer_behavior.sort_values(
    by="Total_Orders",
    ascending=False
).head(10)

print("\nTop 10 Customers by Orders:")
print(top_customers.round(2))







# ==========================================
# STEP 16: CUSTOMER REVENUE CONTRIBUTION
# ==========================================

print("\n========== CUSTOMER REVENUE CONTRIBUTION ==========")

customer_revenue = transactions.groupby("CustomerID").agg(
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

customer_revenue = customer_revenue.sort_values(
    by="Net_Sales",
    ascending=False
)

total_revenue = customer_revenue["Net_Sales"].sum()

# Top 10 customers
top_10_revenue = customer_revenue.head(10)["Net_Sales"].sum()

top_10_percentage = (top_10_revenue / total_revenue) * 100

print("\nTop 10 Customers Revenue:", round(top_10_revenue, 2))
print("Top 10 Customers Revenue Contribution:", round(top_10_percentage, 2), "%")


# Top 20% customers
top_20_percent_count = int(len(customer_revenue) * 0.20)

top_20_customers_revenue = (
    customer_revenue.head(top_20_percent_count)["Net_Sales"].sum()
)

top_20_percentage = (
    top_20_customers_revenue / total_revenue
) * 100

print("\nTop 20% Customers Count:", top_20_percent_count)

print(
    "Top 20% Customers Revenue Contribution:",
    round(top_20_percentage, 2),
    "%"
)


# Top 10 customers details
print("\nTop 10 Revenue Generating Customers:")
print(customer_revenue.head(10).round(2))





# ==========================================
# STEP 17: REGIONAL SALES ANALYSIS
# ==========================================

print("\n========== REGIONAL SALES ANALYSIS ==========")

regional_data = transactions.merge(
    stores[["StoreID", "Region"]],
    on="StoreID",
    how="left"
)

regional_performance = regional_data.groupby("Region").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

regional_performance = regional_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nRegion-wise Sales Performance:")
print(regional_performance.round(2))

print("\nHighest Revenue Region:")
print(regional_performance["Net_Sales"].idxmax())

print("\nLowest Revenue Region:")
print(regional_performance["Net_Sales"].idxmin())

print("\nHighest Profit Region:")
print(regional_performance["Total_Profit"].idxmax())





# ==========================================
# STEP 18: STATE & CITY SALES ANALYSIS
# ==========================================

print("\n========== STATE & CITY SALES ANALYSIS ==========")

# Merge transaction data with store information
location_data = transactions.merge(
    stores[["StoreID", "State", "City"]],
    on="StoreID",
    how="left"
)

# State-wise analysis
state_performance = location_data.groupby("State").agg(
    Total_Orders=("OrderID", "nunique"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

state_performance = state_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nState-wise Sales Performance:")
print(state_performance.round(2))

print("\nHighest Revenue State:")
print(state_performance["Net_Sales"].idxmax())

print("\nLowest Revenue State:")
print(state_performance["Net_Sales"].idxmin())


# City-wise analysis
city_performance = location_data.groupby("City").agg(
    Total_Orders=("OrderID", "nunique"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

city_performance = city_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nTop 10 Cities by Revenue:")
print(city_performance.head(10).round(2))

print("\nLowest Revenue City:")
print(city_performance["Net_Sales"].idxmin())




# ==========================================
# STEP 19: STORE PERFORMANCE ANALYSIS
# ==========================================

print("\n========== STORE PERFORMANCE ANALYSIS ==========")

store_data = transactions.merge(
    stores[["StoreID", "StoreName", "Region", "StoreType"]],
    on="StoreID",
    how="left"
)

store_performance = store_data.groupby(
    ["StoreID", "StoreName", "Region", "StoreType"]
).agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

store_performance = store_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nTop 10 Stores by Revenue:")
print(store_performance.head(10).round(2))

print("\nHighest Revenue Store:")
print(store_performance["Net_Sales"].idxmax())

print("\nLowest Revenue Store:")
print(store_performance["Net_Sales"].idxmin())

print("\nHighest Profit Store:")
print(store_performance["Total_Profit"].idxmax())




# ==========================================
# STEP 20: PAYMENT MODE ANALYSIS
# ==========================================

print("\n========== PAYMENT MODE ANALYSIS ==========")

payment_performance = transactions.groupby("PaymentMode").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

payment_performance = payment_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nPayment Mode Performance:")
print(payment_performance.round(2))

print("\nHighest Revenue Payment Mode:")
print(payment_performance["Net_Sales"].idxmax())

print("\nLowest Revenue Payment Mode:")
print(payment_performance["Net_Sales"].idxmin())

print("\nMost Used Payment Mode:")
print(payment_performance["Total_Orders"].idxmax())




# ==========================================
# STEP 21: SALES CHANNEL ANALYSIS
# ==========================================

print("\n========== SALES CHANNEL ANALYSIS ==========")

channel_performance = transactions.groupby("SalesChannel").agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Quantity=("Quantity", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

channel_performance = channel_performance.sort_values(
    by="Net_Sales",
    ascending=False
)

print("\nSales Channel Performance:")
print(channel_performance.round(2))

print("\nHighest Revenue Channel:")
print(channel_performance["Net_Sales"].idxmax())

print("\nLowest Revenue Channel:")
print(channel_performance["Net_Sales"].idxmin())

print("\nMost Used Sales Channel:")
print(channel_performance["Total_Orders"].idxmax())



# ==========================================
# STEP 22: DISCOUNT IMPACT ANALYSIS
# ==========================================

print("\n========== DISCOUNT IMPACT ANALYSIS ==========")

# Create discount groups
transactions["DiscountCategory"] = pd.cut(
    transactions["DiscountPercent"],
    bins=[-0.001, 0, 0.05, 0.10, 0.20, 1],
    labels=[
        "No Discount",
        "0-5%",
        "5-10%",
        "10-20%",
        "Above 20%"
    ]
)

discount_performance = transactions.groupby(
    "DiscountCategory",
    observed=False
).agg(
    Total_Orders=("OrderID", "nunique"),
    Total_Discount=("DiscountAmount", "sum"),
    Net_Sales=("NetSales", "sum"),
    Total_Profit=("Profit", "sum")
)

discount_performance["Profit_Margin_%"] = (
    discount_performance["Total_Profit"] /
    discount_performance["Net_Sales"].replace(0, np.nan)
) * 100

print("\nDiscount Category Performance:")
print(discount_performance.round(2))

print("\nHighest Revenue Discount Category:")
print(discount_performance["Net_Sales"].idxmax())

print("\nHighest Profit Discount Category:")
print(discount_performance["Total_Profit"].idxmax())






# ==========================================
# STEP 23: RETURN ANALYSIS
# ==========================================

print("\n========== RETURN ANALYSIS ==========")

# Overall return analysis
total_orders = transactions["OrderID"].nunique()

returned_orders = transactions.loc[
    transactions["ReturnFlag"] == True,
    "OrderID"
].nunique()

return_rate = (returned_orders / total_orders) * 100

total_return_quantity = transactions["ReturnQuantity"].sum()

total_return_amount = transactions["ReturnAmount"].sum()

total_gross_sales = transactions["GrossSales"].sum()

return_amount_percentage = (
    total_return_amount / total_gross_sales
) * 100

print("\nTotal Orders:", total_orders)
print("Returned Orders:", returned_orders)

print("Return Rate:", round(return_rate, 2), "%")

print("Total Return Quantity:", total_return_quantity)

print("Total Return Amount:", round(total_return_amount, 2))

print(
    "Return Amount as % of Gross Sales:",
    round(return_amount_percentage, 2),
    "%"
)


# Category-wise return analysis
return_data = transactions.merge(
    products[["ProductID", "Category"]],
    on="ProductID",
    how="left"
)

category_returns = return_data.groupby("Category").agg(
    Total_Orders=("OrderID", "nunique"),
    Returned_Orders=("ReturnFlag", "sum"),
    Return_Quantity=("ReturnQuantity", "sum"),
    Return_Amount=("ReturnAmount", "sum")
)

category_returns["Return_Rate_%"] = (
    category_returns["Returned_Orders"] /
    category_returns["Total_Orders"]
) * 100

category_returns = category_returns.sort_values(
    by="Return_Amount",
    ascending=False
)

print("\nCategory-wise Return Analysis:")
print(category_returns.round(2))

print("\nHighest Return Amount Category:")
print(category_returns["Return_Amount"].idxmax())






# ==========================================
# STEP 24: CORRELATION & OUTLIER ANALYSIS
# ==========================================

print("\n========== CORRELATION ANALYSIS ==========")

numeric_columns = [
    "Quantity",
    "GrossSales",
    "DiscountAmount",
    "ReturnAmount",
    "NetSales",
    "COGS",
    "Profit"
]

correlation_matrix = transactions[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))


# ==========================================
# OUTLIER ANALYSIS USING IQR
# ==========================================

# ==========================================
# STEP 24: CORRELATION & OUTLIER ANALYSIS
# ==========================================

print("\n========== CORRELATION ANALYSIS ==========")

numeric_columns = [
    "Quantity",
    "GrossSales",
    "DiscountAmount",
    "ReturnAmount",
    "NetSales",
    "COGS",
    "Profit"
]

correlation_matrix = transactions[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))


# ==========================================
# OUTLIER ANALYSIS USING IQR
# ==========================================

print("\n========== OUTLIER ANALYSIS ==========")

outlier_columns = [
    "GrossSales",
    "DiscountAmount",
    "NetSales",
    "Profit"
]

for column in outlier_columns:

    Q1 = transactions[column].quantile(0.25)

    Q3 = transactions[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR

    upper_limit = Q3 + 1.5 * IQR

    outliers = transactions[
        (transactions[column] < lower_limit) |
        (transactions[column] > upper_limit)
    ]

    print(f"\n{column}")

    print("Lower Limit:", round(lower_limit, 2))

    print("Upper Limit:", round(upper_limit, 2))

    print("Outlier Count:", len(outliers))

    print(
        "Outlier Percentage:",
        round((len(outliers) / len(transactions)) * 100, 2),
        "%"
    )