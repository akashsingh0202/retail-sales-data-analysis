import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "dataset"

print("Project Directory:", BASE_DIR)
print("Dataset Directory:", DATA_DIR)
print("Dataset Exists:", DATA_DIR.exists())

# Load retail transactions dataset

transactions = pd.read_csv(DATA_DIR / "retail_transactions_100k.csv")

# print(transactions.head())
# Check dataset dimensions

print("Dataset Shape:", transactions.shape)

print("Total Rows:", transactions.shape[0])

print("Total Columns:", transactions.shape[1])

# Check column names

print("\nColumn Names:")
print(transactions.columns)

# Check data types

print("\nColumn Data Types:")
print(transactions.dtypes)

# Dataset information

print("\nDataset Information:")
transactions.info()

# Check missing values

print("\nMissing Values Count:")
print(transactions.isnull().sum())

print("\nTotal Missing Values:")
print(transactions.isnull().sum().sum())

# Check duplicate records

print("\nTotal Duplicate Rows:")
print(transactions.duplicated().sum())

# Check duplicate Order IDs

print("\nDuplicate Order IDs:")
print(transactions["OrderID"].duplicated().sum())


# Check blank values in string columns

string_columns = transactions.select_dtypes(include="str").columns

for column in string_columns:
    blank_count = transactions[column].str.strip().eq("").sum()
    print(f"{column}: {blank_count}")


# Load remaining retail datasets

customers = pd.read_csv(DATA_DIR / "customers_12k.csv")

products = pd.read_csv(DATA_DIR / "products_650.csv")

stores = pd.read_csv(DATA_DIR / "stores_35.csv")

calendar = pd.read_csv(DATA_DIR / "calendar_2023_2025.csv")


# Check dataset shapes

print("\nCUSTOMERS:", customers.shape)

print("PRODUCTS:", products.shape)

print("STORES:", stores.shape)

print("CALENDAR:", calendar.shape)

print("Transactions :" , transactions.shape)


# Check column names of all datasets

print("\nTRANSACTIONS COLUMNS:")
print(transactions.columns.tolist())

print("\nCUSTOMERS COLUMNS:")
print(customers.columns.tolist())

print("\nPRODUCTS COLUMNS:")
print(products.columns.tolist())

print("\nSTORES COLUMNS:")
print(stores.columns.tolist())

print("\nCALENDAR COLUMNS:")
print(calendar.columns.tolist())


# Check primary key uniqueness

print("\nCUSTOMER ID DUPLICATES:")
print(customers["CustomerID"].duplicated().sum())

print("\nPRODUCT ID DUPLICATES:")
print(products["ProductID"].duplicated().sum())

print("\nSTORE ID DUPLICATES:")
print(stores["StoreID"].duplicated().sum())

print("\nCALENDAR DATE DUPLICATES:")
print(calendar["Date"].duplicated().sum())



# Check foreign key relationships

print("\nINVALID CUSTOMER IDs:")
print(
    (~transactions["CustomerID"].isin(customers["CustomerID"])).sum()
)

print("\nINVALID PRODUCT IDs:")
print(
    (~transactions["ProductID"].isin(products["ProductID"])).sum()
)

print("\nINVALID STORE IDs:")
print(
    (~transactions["StoreID"].isin(stores["StoreID"])).sum()
)




# Check date column data types

print("\nORDER DATE DATA TYPE:")
print(transactions["OrderDate"].dtype)

print("\nCALENDAR DATE DATA TYPE:")
print(calendar["Date"].dtype)

print("\nTRANSACTION DATE SAMPLE:")
print(transactions["OrderDate"].head())

print("\nCALENDAR DATE SAMPLE:")
print(calendar["Date"].head())



# Check invalid transaction dates

print("\nINVALID ORDER DATES:")
print(
    (~transactions["OrderDate"].isin(calendar["Date"])).sum()
)

# Check transaction date range

print("\nEARLIEST ORDER DATE:")
print(transactions["OrderDate"].min())

print("\nLATEST ORDER DATE:")
print(transactions["OrderDate"].max())

print("\nCALENDAR DATE RANGE:")
print(calendar["Date"].min(), "to", calendar["Date"].max())



# Check complete duplicate rows

print("\nCOMPLETE DUPLICATE ROWS:")
print(transactions.duplicated().sum())

# Check duplicate OrderIDs

print("\nDUPLICATE ORDER IDs:")
print(transactions["OrderID"].duplicated().sum())



# Check data types of all datasets

print("\nTRANSACTIONS DATA TYPES:")
print(transactions.dtypes)

print("\nCUSTOMERS DATA TYPES:")
print(customers.dtypes)

print("\nPRODUCTS DATA TYPES:")
print(products.dtypes)

print("\nSTORES DATA TYPES:")
print(stores.dtypes)

print("\nCALENDAR DATA TYPES:")
print(calendar.dtypes)


# Convert date columns into datetime

transactions["OrderDate"] = pd.to_datetime(transactions["OrderDate"])
customers["SignupDate"] = pd.to_datetime(customers["SignupDate"])
calendar["Date"] = pd.to_datetime(calendar["Date"])

# Verify converted data types

print("\nCONVERTED DATE DATA TYPES:")

print("OrderDate:", transactions["OrderDate"].dtype)
print("SignupDate:", customers["SignupDate"].dtype)
print("Calendar Date:", calendar["Date"].dtype)

# Check missing values in all datasets

datasets = {
    "Transactions": transactions,
    "Customers": customers,
    "Products": products,
    "Stores": stores,
    "Calendar": calendar
}

for name, df in datasets.items():
    print(f"\n{name} Missing Values:")
    print(df.isnull().sum())



# Check blank and whitespace values

for name, df in datasets.items():
    text_columns = df.select_dtypes(include=["str"]).columns

    print(f"\n{name} Blank Values:")

    for col in text_columns:
        blank_count = df[col].str.strip().eq("").sum()

        if blank_count > 0:
            print(f"{col}: {blank_count}")


# Step 11: Check blank and whitespace values

for name, df in datasets.items():

    text_columns = df.select_dtypes(include=["str"]).columns

    print(f"\n{name} Blank Values:")

    for col in text_columns:

        blank_count = df[col].str.strip().eq("").sum()

        if blank_count > 0:
            print(f"{col}: {blank_count}")
        else:
            print(f"{col}: 0")


# Step 12: Numerical data statistical summary

for name, df in datasets.items():

    numeric_columns = df.select_dtypes(include=["number"])

    print(f"\n{name} Numerical Summary:")

    if numeric_columns.empty:
        print("No numerical columns available.")
    else:
        print(numeric_columns.describe())



# Step 13: Validate numerical values

non_negative_columns = [
    "Quantity",
    "UnitPrice",
    "GrossSales",
    "DiscountAmount",
    "ReturnQuantity",
    "ReturnAmount",
    "NetSales",
    "COGS"
]

print("\nNEGATIVE VALUE CHECK:")

for col in non_negative_columns:
    negative_count = (transactions[col] < 0).sum()
    print(f"{col}: {negative_count}")

# Discount percentage validation

invalid_discount = (
    (transactions["DiscountPercent"] < 0) |
    (transactions["DiscountPercent"] > 1)
).sum()

print("\nINVALID DISCOUNT PERCENTAGE:")
print(invalid_discount)




# Step 14: Business formula validation

# Check GrossSales calculation

expected_gross_sales = (
    transactions["Quantity"] * transactions["UnitPrice"]
)

gross_sales_mismatch = (
    ~np.isclose(
        transactions["GrossSales"],
        expected_gross_sales,
        atol=0.02
    )
).sum()

print("\nGROSS SALES MISMATCH:")
print(gross_sales_mismatch)


# Check DiscountAmount calculation

expected_discount = (
    transactions["GrossSales"] * transactions["DiscountPercent"]
)

discount_mismatch = (
    ~np.isclose(
        transactions["DiscountAmount"],
        expected_discount,
        atol=0.02
    )
).sum()

print("\nDISCOUNT AMOUNT MISMATCH:")
print(discount_mismatch)



# Step 15: NetSales formula validation

expected_net_sales = (
    transactions["GrossSales"]
    - transactions["DiscountAmount"]
    - transactions["ReturnAmount"]
)

net_sales_mismatch = (
    ~np.isclose(
        transactions["NetSales"],
        expected_net_sales,
        atol=0.02
    )
).sum()

print("\nNET SALES MISMATCH:")
print(net_sales_mismatch)


# Step 16: Profit formula validation

expected_profit = (
    transactions["NetSales"] - transactions["COGS"]
)

profit_mismatch = (
    ~np.isclose(
        transactions["Profit"],
        expected_profit,
        atol=0.02
    )
).sum()

print("\nPROFIT MISMATCH:")
print(profit_mismatch)




# Step 17: Return data validation

# Count returned and non-returned transactions

print("\nRETURN FLAG COUNTS:")
print(transactions["ReturnFlag"].value_counts())

# Check returned transactions with zero return quantity

invalid_return_quantity = (
    (transactions["ReturnFlag"] == True) &
    (transactions["ReturnQuantity"] == 0)
).sum()

print("\nRETURN FLAG TRUE BUT ZERO RETURN QUANTITY:")
print(invalid_return_quantity)

# Check non-returned transactions with return amount

invalid_return_amount = (
    (transactions["ReturnFlag"] == False) &
    (transactions["ReturnAmount"] > 0)
).sum()

print("\nNON-RETURNED BUT POSITIVE RETURN AMOUNT:")
print(invalid_return_amount)



# Step 18: Return quantity validation

invalid_return_qty = (
    transactions["ReturnQuantity"] > transactions["Quantity"]
).sum()

print("\nRETURN QUANTITY GREATER THAN ORDER QUANTITY:")
print(invalid_return_qty)


# Step 19: Return amount validation

invalid_return_amount = (
    transactions["ReturnAmount"] > transactions["GrossSales"]
).sum()

print("\nRETURN AMOUNT GREATER THAN GROSS SALES:")
print(invalid_return_amount)




# Step 20: Validate OrderMonth and OrderYear

# Extract month and year from OrderDate

expected_month = transactions["OrderDate"].dt.strftime("%Y-%m")
expected_year = transactions["OrderDate"].dt.year

# Compare with existing columns

invalid_month = (
    transactions["OrderMonth"] != expected_month
).sum()

invalid_year = (
    transactions["OrderYear"] != expected_year
).sum()

print("\nINVALID ORDER MONTH:")
print(invalid_month)

print("\nINVALID ORDER YEAR:")
print(invalid_year)



# Step 21: Check Unique Categorical Values

categorical_columns = {
    "Transactions": {
        "PaymentMode": transactions,
        "SalesChannel": transactions
    },
    "Customers": {
        "CustomerSegment": customers
    },
    "Products": {
        "Category": products,
        "SubCategory": products,
        "Brand": products
    },
    "Stores": {
        "Region": stores,
        "StoreType": stores
    }
}

for dataset_name, columns in categorical_columns.items():

    print(f"\n{dataset_name} - UNIQUE VALUES")

    for column_name, df in columns.items():

        print(f"\n{column_name}:")
        print(sorted(df[column_name].dropna().unique()))


# Step 22: Outlier Detection using IQR

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "GrossSales",
    "DiscountPercent",
    "DiscountAmount",
    "NetSales",
    "COGS",
    "Profit"
]

for column in numeric_columns:

    Q1 = transactions[column].quantile(0.25)
    Q3 = transactions[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    outliers = transactions[
        (transactions[column] < lower_limit) |
        (transactions[column] > upper_limit)
    ]

    print(f"\n{column}")
    print("Lower Limit:", round(lower_limit, 2))
    print("Upper Limit:", round(upper_limit, 2))
    print("Outlier Count:", len(outliers))



# Step 23: Inspect Highest UnitPrice Transactions

high_price_transactions = transactions.nlargest(
    10, "UnitPrice"
)

print("\nTOP 10 HIGHEST UNIT PRICE TRANSACTIONS:")

print(
    high_price_transactions[
        ["OrderID", "ProductID", "Quantity",
         "UnitPrice", "GrossSales", "Profit"]
    ]
)




# Step 24: Investigate High-Priced Product

product_details = products[
    products["ProductID"] == "P00072"
]

print("\nHIGH-PRICED PRODUCT DETAILS:")
print(product_details)




# Step 25: Inspect Highest GrossSales Transactions

high_sales_transactions = transactions.nlargest(
    10, "GrossSales"
)

print("\nTOP 10 HIGHEST GROSS SALES TRANSACTIONS:")

print(
    high_sales_transactions[
        ["OrderID", "ProductID", "Quantity",
         "UnitPrice", "GrossSales", "DiscountAmount",
         "NetSales", "Profit"]
    ]
)


# Step 26: Inspect Lowest Profit Transactions

low_profit_transactions = transactions.nsmallest(
    10, "Profit"
)

print("\nTOP 10 LOWEST PROFIT TRANSACTIONS:")

print(
    low_profit_transactions[
        ["OrderID", "ProductID", "Quantity",
         "GrossSales", "DiscountAmount",
         "ReturnAmount", "NetSales", "COGS", "Profit"]
    ]
)


# Step 27: Analyze Loss-Making Transactions

loss_transactions = transactions[
    transactions["Profit"] < 0
]

total_loss_transactions = len(loss_transactions)

total_loss_amount = loss_transactions["Profit"].sum()

print("\nLOSS-MAKING TRANSACTION ANALYSIS:")

print("Total Loss Transactions:", total_loss_transactions)

print("Total Loss Amount:", round(total_loss_amount, 2))

print(
    "Loss Transaction Percentage:",
    round((total_loss_transactions / len(transactions)) * 100, 2),
    "%"
)



# Step 28: Analyze Zero-Profit Transactions

zero_profit_transactions = transactions[
    transactions["Profit"] == 0
]

print("\nZERO-PROFIT TRANSACTION ANALYSIS:")

print("Zero Profit Transactions:", len(zero_profit_transactions))


# Step 29: Analyze Profitable Transactions

profitable_transactions = transactions[
    transactions["Profit"] > 0
]

print("\nPROFITABLE TRANSACTION ANALYSIS:")

print("Profitable Transactions:", len(profitable_transactions))

print(
    "Profitable Transaction Percentage:",
    round((len(profitable_transactions) / len(transactions)) * 100, 2),
    "%"
)

# Step 29: Analyze Profitable Transactions

profitable_transactions = transactions[
    transactions["Profit"] > 0
]

print("\nPROFITABLE TRANSACTION ANALYSIS:")

print("Profitable Transactions:", len(profitable_transactions))

print(
    "Profitable Transaction Percentage:",
    round((len(profitable_transactions) / len(transactions)) * 100, 2),
    "%"
)



# Step 30: Final Dataset Profiling

print("\n========== FINAL DATASET PROFILE ==========")

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Total Missing Values:", df.isnull().sum().sum())
    print("Duplicate Rows:", df.duplicated().sum())

    print(
        "Memory Usage (MB):",
        round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2)
    )



    # Step 31: Dataset Relationship Summary

relationships = {
    "Customer": ("CustomerID", "CustomerID"),
    "Product": ("ProductID", "ProductID"),
    "Store": ("StoreID", "StoreID"),
    "Calendar": ("OrderDate", "Date")
}

print("\n========== DATASET RELATIONSHIPS ==========")

for name, (fact_key, dimension_key) in relationships.items():

    print(f"\nTransactions[{fact_key}]")
    print(f"    -> {name}[{dimension_key}]")
    print("    Relationship: Many-to-One")