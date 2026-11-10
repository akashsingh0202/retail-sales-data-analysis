
import pandas as pd
import numpy as np
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset directory
DATA_DIR = BASE_DIR / "dataset"

# Load all five raw datasets
transactions = pd.read_csv(DATA_DIR / "retail_transactions_100k.csv")
customers = pd.read_csv(DATA_DIR / "customers_12k.csv")
products = pd.read_csv(DATA_DIR / "products_650.csv")
stores = pd.read_csv(DATA_DIR / "stores_35.csv")
calendar = pd.read_csv(DATA_DIR / "calendar_2023_2025.csv")

# Create working copies
clean_transactions = transactions.copy()
clean_customers = customers.copy()
clean_products = products.copy()
clean_stores = stores.copy()
clean_calendar = calendar.copy()

# Store all datasets in a dictionary
datasets = {
    "Transactions": clean_transactions,
    "Customers": clean_customers,
    "Products": clean_products,
    "Stores": clean_stores,
    "Calendar": clean_calendar
}

# Display dataset shapes
print("\n========== DATA CLEANING SETUP ==========")

for name, df in datasets.items():
    print(f"{name}: {df.shape}")

print("\nAll five datasets loaded successfully!")




print("\n========== INITIAL DATA QUALITY PROFILE ==========")

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("Missing Values:", df.isnull().sum().sum())

    print("Duplicate Rows:", df.duplicated().sum())

    print("Memory Usage (MB):",
          round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2))

    print("Data Types:")
    print(df.dtypes)



# step-3

print("\n========== COLUMN DATA TYPE CLASSIFICATION ==========")

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    text_columns = df.select_dtypes(include=["object", "str"]).columns.tolist()

    boolean_columns = df.select_dtypes(include=["bool"]).columns.tolist()

    datetime_columns = df.select_dtypes(include=["datetime"]).columns.tolist()

    print("Numeric Columns:", numeric_columns)
    print("Text Columns:", text_columns)
    print("Boolean Columns:", boolean_columns)
    print("Datetime Columns:", datetime_columns)




print("\n========== MISSING VALUES COLUMN-WISE ANALYSIS ==========")

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    missing_count = df.isnull().sum()

    missing_percentage = (missing_count / len(df)) * 100

    missing_report = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing Percentage": missing_percentage
    })

    missing_report = missing_report[missing_report["Missing Count"] > 0]

    if missing_report.empty:
        print("No missing values found.")
    else:
        print(missing_report)



print("\n========== DUPLICATE RECORD ANALYSIS ==========")

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    duplicate_count = df.duplicated().sum()

    duplicate_percentage = (duplicate_count / len(df)) * 100

    print("Duplicate Rows:", duplicate_count)

    print("Duplicate Percentage:",
          round(duplicate_percentage, 2), "%")

    if duplicate_count > 0:

        print("\nDuplicate Records Sample:")
        print(df[df.duplicated()].head())

    else:
        print("No duplicate records found.")




print("\n========== PRIMARY KEY VALIDATION ==========")

primary_keys = {
    "Transactions": ["OrderID"],
    "Customers": ["CustomerID"],
    "Products": ["ProductID"],
    "Stores": ["StoreID"],
    "Calendar": ["Date"]
}

for name, columns in primary_keys.items():

    df = datasets[name]

    print(f"\n{name.upper()}")

    for column in columns:

        duplicate_count = df[column].duplicated().sum()

        missing_count = df[column].isnull().sum()

        print(f"{column} Duplicate Values:", duplicate_count)
        print(f"{column} Missing Values:", missing_count)

        if duplicate_count == 0 and missing_count == 0:
            print(f"{column}: Primary Key validation passed.")
        else:
            print(f"{column}: Primary Key issue found.")





print("\n========== DUPLICATE COLUMN NAME VALIDATION ==========")

for name, df in datasets.items():

    duplicate_columns = df.columns[df.columns.duplicated()].tolist()

    print(f"\n{name.upper()}")

    print("Duplicate Column Names:", duplicate_columns)

    if len(duplicate_columns) == 0:
        print("Column name validation passed.")
    else:
        print("Duplicate column names found.")




print("\n========== DATE DATA TYPE CONVERSION ==========")

date_columns = {
    "Transactions": ["OrderDate"],
    "Customers": ["SignupDate"],
    "Calendar": ["Date"]
}

for name, columns in date_columns.items():

    df = datasets[name]

    print(f"\n{name.upper()}")

    for column in columns:

        df[column] = pd.to_datetime(df[column], errors="coerce")

        print(f"{column}:", df[column].dtype)

        print("Invalid Dates:", df[column].isnull().sum())




print("\n========== NUMERIC DATA TYPE VALIDATION ==========")

numeric_columns = {
    "Transactions": [
        "Quantity", "UnitPrice", "GrossSales",
        "DiscountPercent", "DiscountAmount",
        "ReturnQuantity", "ReturnAmount",
        "NetSales", "COGS", "Profit", "OrderYear"
    ],

    "Products": ["UnitPrice", "UnitCost"],

    "Calendar": ["Year", "MonthNumber"]
}

for name, columns in numeric_columns.items():

    df = datasets[name]

    print(f"\n{name.upper()}")

    for column in columns:

        print(f"{column}: {df[column].dtype}")

        if pd.api.types.is_numeric_dtype(df[column]):
            print("Numeric validation passed.")
        else:
            print("Numeric validation failed.")



print("\n========== BOOLEAN DATA TYPE VALIDATION ==========")

boolean_columns = {
    "Transactions": ["ReturnFlag"],
    "Calendar": ["IsWeekend"]
}

for name, columns in boolean_columns.items():

    df = datasets[name]

    print(f"\n{name.upper()}")

    for column in columns:

        print(f"{column}: {df[column].dtype}")

        if pd.api.types.is_bool_dtype(df[column]):
            print("Boolean validation passed.")
        else:
            print("Boolean validation failed.")



print("\n========== TEXT DATA TYPE VALIDATION ==========")

text_columns = {
    "Transactions": [
        "OrderID", "CustomerID", "ProductID",
        "StoreID", "PaymentMode", "SalesChannel", "OrderMonth"
    ],

    "Customers": [
        "CustomerID", "CustomerName", "City",
        "State", "CustomerSegment"
    ],

    "Products": [
        "ProductID", "ProductName", "Category",
        "SubCategory", "Brand"
    ],

    "Stores": [
        "StoreID", "StoreName", "City",
        "State", "Region", "StoreType"
    ],

    "Calendar": [
        "Quarter", "MonthName", "DayName"
    ]
}

for name, columns in text_columns.items():

    df = datasets[name]

    print(f"\n{name.upper()}")

    for column in columns:

        print(f"{column}: {df[column].dtype}")

        if pd.api.types.is_string_dtype(df[column]):
            print("Text validation passed.")
        else:
            print("Text validation failed.")




print("\n========== WHITESPACE VALIDATION ==========")

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    text_cols = df.select_dtypes(include=["str"]).columns

    total_whitespace = 0

    for column in text_cols:

        whitespace_count = (
            df[column].str.strip() != df[column]
        ).sum()

        if whitespace_count > 0:
            print(f"{column}: {whitespace_count} extra spaces")
            total_whitespace += whitespace_count

    print("Total whitespace issues:", total_whitespace)





print("\n========== EMPTY STRING VALIDATION ==========")

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    text_cols = df.select_dtypes(include=["str"]).columns

    total_empty = 0

    for column in text_cols:

        empty_count = (df[column] == "").sum()

        if empty_count > 0:
            print(f"{column}: {empty_count} empty strings")
            total_empty += empty_count

    print("Total empty strings:", total_empty)





print("\n========== CATEGORICAL VALUE CONSISTENCY ==========")

categorical_columns = {
    "Transactions": ["PaymentMode", "SalesChannel"],
    "Customers": ["CustomerSegment"],
    "Products": ["Category", "SubCategory", "Brand"],
    "Stores": ["Region", "StoreType"]
}

for name, columns in categorical_columns.items():

    df = datasets[name]

    print(f"\n{name.upper()}")

    for column in columns:

        print(f"\n{column}")

        print("Unique Values:", df[column].nunique())

        print(df[column].value_counts().to_string())




print("\n========== NUMERIC RANGE VALIDATION ==========")

range_checks = {
    "Transactions": {
        "Quantity": (1, None),
        "UnitPrice": (0, None),
        "DiscountPercent": (0, 100),
        "DiscountAmount": (0, None),
        "ReturnQuantity": (0, None),
        "ReturnAmount": (0, None),
        "GrossSales": (0, None),
        "NetSales": (0, None),
        "COGS": (0, None)
    },

    "Products": {
        "UnitPrice": (0, None),
        "UnitCost": (0, None)
    }
}

for name, columns in range_checks.items():

    df = datasets[name]

    print(f"\n{name.upper()}")

    for column, (minimum, maximum) in columns.items():

        invalid_count = 0

        if minimum is not None:
            invalid_count += (df[column] < minimum).sum()

        if maximum is not None:
            invalid_count += (df[column] > maximum).sum()

        print(f"{column} Invalid Values: {invalid_count}")




print("\n========== DISCOUNT FORMULA INVESTIGATION ==========")

df = datasets["Transactions"]

# Calculate expected discount
expected_discount = (
    df["GrossSales"] * df["DiscountPercent"] / 100
)

# Create comparison DataFrame
comparison = df[
    [
        "OrderID",
        "GrossSales",
        "DiscountPercent",
        "DiscountAmount",
        "ReturnAmount",
        "NetSales",
        "COGS",
        "Profit"
    ]
].copy()

# Add expected discount
comparison["ExpectedDiscount"] = expected_discount

# Calculate difference
comparison["DiscountDifference"] = (
    comparison["DiscountAmount"]
    - comparison["ExpectedDiscount"]
)

# Filter mismatched records
mismatches = comparison[
    comparison["DiscountDifference"].abs() > 0.01
]

print("Total Discount Mismatches:", len(mismatches))

print("\nFirst 10 Mismatched Records:")

print(mismatches.head(10).to_string(index=False))




print("\n========== BUSINESS FORMULA VALIDATION ==========")

df = datasets["Transactions"]

# Expected business calculations
expected_gross_sales = (
    df["Quantity"] * df["UnitPrice"]
)

expected_discount = (
    df["GrossSales"] * df["DiscountPercent"]
)

expected_net_sales = (
    df["GrossSales"]
    - df["DiscountAmount"]
    - df["ReturnAmount"]
)

expected_profit = (
    expected_net_sales - df["COGS"]
)

# Formula comparisons
checks = {
    "GrossSales": expected_gross_sales,
    "DiscountAmount": expected_discount,
    "NetSales": expected_net_sales,
    "Profit": expected_profit
}

for column, expected in checks.items():

    mismatch_count = (
        ~np.isclose(
            df[column],
            expected,
            rtol=1e-5,
            atol=0.01
        )
    ).sum()

    print(f"{column} Mismatches:", mismatch_count)



print("\n========== FOREIGN KEY VALIDATION ==========")

transactions = datasets["Transactions"]

foreign_keys = {
    "CustomerID": datasets["Customers"]["CustomerID"],
    "ProductID": datasets["Products"]["ProductID"],
    "StoreID": datasets["Stores"]["StoreID"],
    "OrderDate": datasets["Calendar"]["Date"]
}

for column, reference_values in foreign_keys.items():

    invalid_count = (
        ~transactions[column].isin(reference_values)
    ).sum()

    print(f"{column} Invalid References:", invalid_count)

    if invalid_count == 0:
        print("Foreign key validation passed.")
    else:
        print("Foreign key validation failed.")



print("\n========== RETURN DATA CONSISTENCY ==========")

df = datasets["Transactions"]

checks = {
    "Returned but Zero Return Quantity": (
        (df["ReturnFlag"] == True) &
        (df["ReturnQuantity"] == 0)
    ),

    "Non-Returned but Positive Return Quantity": (
        (df["ReturnFlag"] == False) &
        (df["ReturnQuantity"] > 0)
    ),

    "Non-Returned but Positive Return Amount": (
        (df["ReturnFlag"] == False) &
        (df["ReturnAmount"] > 0)
    ),

    "Return Quantity Greater Than Order Quantity": (
        df["ReturnQuantity"] > df["Quantity"]
    )
}

for check_name, condition in checks.items():

    invalid_count = condition.sum()

    print(f"{check_name}: {invalid_count}")



print("\n========== ORDER DATE COMPONENT VALIDATION ==========")

df = datasets["Transactions"]

expected_month = df["OrderDate"].dt.strftime("%Y-%m")
expected_year = df["OrderDate"].dt.year

month_mismatches = (
    df["OrderMonth"] != expected_month
).sum()

year_mismatches = (
    df["OrderYear"] != expected_year
).sum()

print("OrderMonth Mismatches:", month_mismatches)
print("OrderYear Mismatches:", year_mismatches)


print("\n========== FINAL DATA CLEANING VERIFICATION ==========")

for name, df in datasets.items():

    print(f"\n{name}")

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("Missing Values:", df.isnull().sum().sum())

    print("Duplicate Rows:", df.duplicated().sum())

    print("Memory Usage (MB):", round(
        df.memory_usage(deep=True).sum() / (1024 ** 2), 2
    ))

print("\nAll five datasets verified successfully!")







