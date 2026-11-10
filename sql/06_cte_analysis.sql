USE retail_sales_analysis;


-- 01. Basic CTE: Year-wise Sales and Profit

WITH Yearly_Sales AS (
    SELECT
        OrderYear,
        SUM(NetSales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM retail_transactions_clean
    GROUP BY OrderYear
)

SELECT
    OrderYear,
    ROUND(Total_Sales, 2) AS Total_Sales,
    ROUND(Total_Profit, 2) AS Total_Profit
FROM Yearly_Sales
ORDER BY OrderYear;



-- 02. CTE with WHERE: High Value Customers

WITH Customer_Sales AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS Total_Orders,
        SUM(NetSales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM retail_transactions_clean
    GROUP BY CustomerID
)

SELECT
    CustomerID,
    Total_Orders,
    ROUND(Total_Sales, 2) AS Total_Sales,
    ROUND(Total_Profit, 2) AS Total_Profit
FROM Customer_Sales
WHERE Total_Sales > 500000
ORDER BY Total_Sales DESC;




-- 03. CTE with HAVING: Frequent Customers

WITH Customer_Orders AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS Total_Orders,
        SUM(NetSales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM retail_transactions_clean
    GROUP BY CustomerID
    HAVING COUNT(OrderID) > 10
)

SELECT
    CustomerID,
    Total_Orders,
    ROUND(Total_Sales, 2) AS Total_Sales,
    ROUND(Total_Profit, 2) AS Total_Profit
FROM Customer_Orders
ORDER BY Total_Orders DESC;





-- 04. CTE with Multiple Conditions: High Value & Frequent Customers

WITH Customer_Sales AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS Total_Orders,
        SUM(NetSales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM retail_transactions_clean
    GROUP BY CustomerID
)

SELECT
    CustomerID,
    Total_Orders,
    ROUND(Total_Sales, 2) AS Total_Sales,
    ROUND(Total_Profit, 2) AS Total_Profit
FROM Customer_Sales
WHERE Total_Orders > 10
AND Total_Sales > 300000
ORDER BY Total_Sales DESC;




-- 05. CTE with JOIN: Customer-wise Sales Details

WITH Customer_Sales AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS Total_Orders,
        SUM(NetSales) AS Total_Sales,
        SUM(Profit) AS Total_Profit
    FROM retail_transactions_clean
    GROUP BY CustomerID
)

SELECT
    c.CustomerID,
    c.CustomerName,
    c.City,
    c.CustomerSegment,
    cs.Total_Orders,
    ROUND(cs.Total_Sales, 2) AS Total_Sales,
    ROUND(cs.Total_Profit, 2) AS Total_Profit
FROM customers c
INNER JOIN Customer_Sales cs
    ON c.CustomerID = cs.CustomerID
ORDER BY cs.Total_Sales DESC
LIMIT 10;



-- 06. Customer Segment Analysis

SELECT
    c.CustomerSegment,
    COUNT(DISTINCT c.CustomerID) AS Total_Customers,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit,
    ROUND(AVG(t.NetSales), 2) AS Average_Order_Value
FROM customers c
INNER JOIN retail_transactions_clean t
    ON c.CustomerID = t.CustomerID
GROUP BY c.CustomerSegment
ORDER BY Total_Sales DESC;

