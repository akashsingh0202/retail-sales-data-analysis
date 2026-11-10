USE retail_sales_analysis;

SELECT
    ROUND(SUM(GrossSales), 2) AS Total_Gross_Sales,
    ROUND(SUM(DiscountAmount), 2) AS Total_Discount,
    ROUND(SUM(NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_transactions_clean;


SELECT
    COUNT(OrderID) AS Total_Orders,
    COUNT(DISTINCT CustomerID) AS Unique_Customers
FROM retail_transactions_clean;


SELECT
    ROUND(AVG(NetSales), 2) AS Average_Order_Value
FROM retail_transactions_clean;



SELECT
    OrderYear,
    COUNT(OrderID) AS Total_Orders,
    ROUND(SUM(NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_transactions_clean
GROUP BY OrderYear
ORDER BY OrderYear;





SELECT
    OrderYear,
    OrderMonth,
    COUNT(OrderID) AS Total_Orders,
    ROUND(SUM(NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_transactions_clean
GROUP BY
    OrderYear,
    OrderMonth
ORDER BY
    OrderYear,
    OrderMonth;
    
    
    
    
    
    
SELECT
    OrderYear,
    QUARTER(STR_TO_DATE(CONCAT(OrderMonth, '-01'), '%Y-%m-%d')) AS Quarter_Number,
    COUNT(OrderID) AS Total_Orders,
    ROUND(SUM(NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_transactions_clean
GROUP BY
    OrderYear,
    QUARTER(STR_TO_DATE(CONCAT(OrderMonth, '-01'), '%Y-%m-%d'))
ORDER BY
    OrderYear,
    Quarter_Number;
    
    
    


SELECT
    DAYNAME(OrderDate) AS Day_Name,
    COUNT(OrderID) AS Total_Orders,
    ROUND(SUM(NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_transactions_clean
GROUP BY DAYNAME(OrderDate), DAYOFWEEK(OrderDate)
ORDER BY DAYOFWEEK(OrderDate);

SHOW TABLES;

SELECT
    s.State,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY s.State
ORDER BY Total_Net_Sales DESC;



SELECT
    s.Region,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY s.Region
ORDER BY Total_Net_Sales DESC;





SELECT
    PaymentMode,
    COUNT(OrderID) AS Total_Orders,
    ROUND(SUM(NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_transactions_clean
GROUP BY PaymentMode
ORDER BY Total_Orders DESC;