USE retail_sales_analysis;

SELECT
    c.CustomerSegment,
    COUNT(t.OrderID) AS Total_Orders,
    COUNT(DISTINCT t.CustomerID) AS Total_Customers,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN customers c
    ON t.CustomerID = c.CustomerID
GROUP BY c.CustomerSegment
ORDER BY Total_Net_Sales DESC;



SELECT
    c.CustomerID,
    c.CustomerName,
    c.CustomerSegment,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN customers c
    ON t.CustomerID = c.CustomerID
GROUP BY
    c.CustomerID,
    c.CustomerName,
    c.CustomerSegment
ORDER BY Total_Net_Sales DESC
LIMIT 10;






SELECT
    Customer_Order_Count,
    COUNT(*) AS Total_Customers
FROM (
    SELECT
        CustomerID,
        COUNT(OrderID) AS Customer_Order_Count
    FROM retail_transactions_clean
    GROUP BY CustomerID
) AS Customer_Summary
GROUP BY Customer_Order_Count
ORDER BY Customer_Order_Count;





SELECT
    CustomerSegment,
    COUNT(CustomerID) AS Total_Customers,
    ROUND(AVG(Customer_Lifetime_Sales), 2) AS Average_CLV
FROM (
    SELECT
        c.CustomerID,
        c.CustomerSegment,
        SUM(t.NetSales) AS Customer_Lifetime_Sales
    FROM retail_transactions_clean t
    JOIN customers c
        ON t.CustomerID = c.CustomerID
    GROUP BY
        c.CustomerID,
        c.CustomerSegment
) AS Customer_CLV
GROUP BY CustomerSegment
ORDER BY Average_CLV DESC;





SELECT
    c.CustomerID,
    c.CustomerName,
    c.City,
    c.State,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Lifetime_Sales
FROM retail_transactions_clean t
JOIN customers c
    ON t.CustomerID = c.CustomerID
GROUP BY
    c.CustomerID,
    c.CustomerName,
    c.City,
    c.State
ORDER BY Lifetime_Sales DESC
LIMIT 20;




SELECT
    c.City,
    c.State,
    COUNT(DISTINCT c.CustomerID) AS Total_Customers,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN customers c
    ON t.CustomerID = c.CustomerID
GROUP BY
    c.City,
    c.State
ORDER BY Total_Net_Sales DESC;




SELECT
    c.CustomerID,
    c.CustomerName,
    c.CustomerSegment,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN customers c
    ON t.CustomerID = c.CustomerID
GROUP BY
    c.CustomerID,
    c.CustomerName,
    c.CustomerSegment
ORDER BY Total_Profit DESC
LIMIT 20;