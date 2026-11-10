# Retail Sales Analysis – Data Cleaning Report

## 1. Project Overview

The purpose of this phase was to validate the quality, consistency,
and reliability of all five datasets used in the Retail Sales Analysis project.

Cleaning and validation were performed using Python and Pandas.
Working copies of the datasets were used, keeping the original CSV files unchanged.

## 2. Tools and Libraries

- Python
- Pandas
- NumPy
- pathlib

## 3. Dataset Overview

| Dataset | Rows | Columns |
|---|---:|---:|
| Transactions | 100,000 | 20 |
| Customers | 12,000 | 6 |
| Products | 650 | 7 |
| Stores | 35 | 6 |
| Calendar | 1,096 | 7 |

## 4. Data Cleaning Activities

The following activities were completed:

1. Data cleaning script setup.
2. Initial data quality profiling.
3. Column data type classification.
4. Missing values analysis.
5. Duplicate record analysis.
6. Primary key duplicate validation.
7. Duplicate column name validation.
8. Date data type conversion.
9. Numeric data type validation.
10. Boolean data type validation.
11. Text data type validation.
12. Leading and trailing whitespace validation.
13. Empty string validation.
14. Categorical value consistency analysis.
15. Numeric range validation.
16. Business formula validation.
17. Foreign key validation.
18. Return data consistency validation.
19. Order month and year consistency validation.
20. Final data cleaning verification.

## 5. Data Quality Validation Results

### Missing Values

No missing values were found in any of the five datasets.

### Duplicate Records

No duplicate rows were found in any dataset.

### Primary Key Validation

All primary keys passed duplicate and missing-value checks:

- Transactions: OrderID
- Customers: CustomerID
- Products: ProductID
- Stores: StoreID
- Calendar: Date

### Foreign Key Validation

All foreign key checks passed:

- Transactions to Customers: 0 invalid references.
- Transactions to Products: 0 invalid references.
- Transactions to Stores: 0 invalid references.
- Transactions to Calendar: 0 invalid references.

### Data Type Validation

The following data types were validated:

- Datetime
- Numeric
- Boolean
- Text

Date columns were successfully converted to datetime types.

### Whitespace and Empty String Validation

No leading or trailing whitespace issues were detected.

No empty strings were detected.

### Numeric Range Validation

All tested numeric columns passed their range checks.

### Business Formula Validation

All four business formula checks returned zero mismatches:

- GrossSales
- DiscountAmount
- NetSales
- Profit

### Return Data Consistency

All four return validation checks passed:

- Returned orders with zero return quantity: 0
- Non-returned orders with positive return quantity: 0
- Non-returned orders with positive return amount: 0
- Return quantity greater than order quantity: 0

### Order Date Component Validation

- OrderMonth mismatches: 0
- OrderYear mismatches: 0

## 6. Final Dataset Profile

| Dataset | Missing Values | Duplicate Rows | Memory (MB) |
|---|---:|---:|---:|
| Transactions | 0 | 0 | 46.46 |
| Customers | 0 | 0 | 3.42 |
| Products | 0 | 0 | 0.19 |
| Stores | 0 | 0 | 0.01 |
| Calendar | 0 | 0 | 0.20 |

## 7. Conclusion

The data cleaning and validation phase was successfully completed.

All five datasets passed the implemented data quality checks.
No missing values, duplicate records, invalid foreign key references,
or business formula mismatches were found.

The datasets are ready for the next phase of the project:
Exploratory Data Analysis (EDA).

Original CSV files were preserved, and validation was performed
on separate working copies.