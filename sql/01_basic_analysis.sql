USE retail_sales_analysis;

-- 1. Total Number of Orders

SELECT
    COUNT(DISTINCT OrderID) AS Total_Orders
FROM retail_transactions_clean;


-- 2. Total Net Sales

SELECT
    ROUND(SUM(NetSales), 2) AS Total_Net_Sales
FROM retail_transactions_clean;



-- 3. Total Profit

SELECT
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_transactions_clean;



-- 4. Average Order Value (AOV)

SELECT
    ROUND(AVG(NetSales), 2) AS Average_Order_Value
FROM retail_transactions_clean;



-- 5. Total Quantity Sold

SELECT
    SUM(Quantity) AS Total_Quantity_Sold
FROM retail_transactions_clean;



-- 6. Total Discount Given

SELECT
    ROUND(SUM(DiscountAmount), 2) AS Total_Discount
FROM retail_transactions_clean;


-- 7. Total Return Amount

SELECT
    ROUND(SUM(ReturnAmount), 2) AS Total_Return_Amount
FROM retail_transactions_clean;


-- 8. Total Returned Orders

SELECT
    COUNT(*) AS Total_Returned_Orders
FROM retail_transactions_clean
WHERE ReturnFlag = 'True';



-- 9. Return Rate Percentage

SELECT
    ROUND(
        COUNT(CASE WHEN ReturnFlag = 'True' THEN 1 END) * 100.0
        / COUNT(*), 2
    ) AS Return_Rate_Percentage
FROM retail_transactions_clean;



-- 10. Overall Profit Margin

SELECT
    ROUND(
        SUM(Profit) * 100.0 / SUM(NetSales), 2
    ) AS Profit_Margin_Percentage
FROM retail_transactions_clean;



-- 11. Total Unique Customers

SELECT
    COUNT(DISTINCT CustomerID) AS Total_Unique_Customers
FROM retail_transactions_clean;


-- 12. Total Unique Products Sold

SELECT
    COUNT(DISTINCT ProductID) AS Unique_Products_Sold
FROM retail_transactions_clean;


-- 13. Total Unique Stores

SELECT
    COUNT(DISTINCT StoreID) AS Total_Active_Stores
FROM retail_transactions_clean;

-- 14. Total Unique Sales Channels

SELECT
    COUNT(DISTINCT SalesChannel) AS Total_Sales_Channels
FROM retail_transactions_clean;

-- 15. Total Unique Payment Modes

SELECT
    COUNT(DISTINCT PaymentMode) AS Total_Payment_Modes
FROM retail_transactions_clean;
