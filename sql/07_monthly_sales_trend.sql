USE retail_sales_analysis;



-- 07. Monthly Sales Trend Analysis

SELECT
    OrderYear,
    OrderMonth,
    COUNT(OrderID) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(NetSales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(AVG(NetSales), 2) AS Average_Order_Value
FROM retail_transactions_clean
GROUP BY
    OrderYear,
    OrderMonth
ORDER BY
    OrderYear,
    OrderMonth;
