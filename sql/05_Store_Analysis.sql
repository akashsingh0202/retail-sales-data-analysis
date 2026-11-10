-- 01. Store-wise Sales and Profit Analysis
USE retail_sales_analysis;
SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    s.State,
    s.Region,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    SUM(t.Quantity) AS Total_Quantity,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City,
    s.State,
    s.Region
ORDER BY Total_Net_Sales DESC;



-- 02. Store Type-wise Sales and Profit Analysis

SELECT
    s.StoreType,
    COUNT(DISTINCT s.StoreID) AS Total_Stores,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    SUM(t.Quantity) AS Total_Quantity,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY s.StoreType
ORDER BY Total_Net_Sales DESC;

-- 03. Region-wise Store Performance

SELECT
    s.Region,
    COUNT(DISTINCT s.StoreID) AS Total_Stores,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit,
    ROUND(AVG(t.NetSales), 2) AS Average_Order_Value
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY s.Region
ORDER BY Total_Net_Sales DESC;




-- 04. Top 10 Stores by Profit

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    s.State,
    s.StoreType,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City,
    s.State,
    s.StoreType
ORDER BY Total_Profit DESC
LIMIT 10;



-- 05. Bottom 10 Stores by Sales

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    s.State,
    s.StoreType,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City,
    s.State,
    s.StoreType
ORDER BY Total_Net_Sales ASC
LIMIT 10;



-- 06. Store-wise Profit Margin Analysis

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    s.StoreType,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit,
    ROUND(
        SUM(t.Profit) / NULLIF(SUM(t.NetSales), 0) * 100,
        2
    ) AS Profit_Margin_Percent
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City,
    s.StoreType
ORDER BY Profit_Margin_Percent DESC;




-- 07. Store-wise Average Order Value

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    s.StoreType,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(
        SUM(t.NetSales) / COUNT(DISTINCT t.OrderID),
        2
    ) AS Average_Order_Value
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City,
    s.StoreType
ORDER BY Average_Order_Value DESC;




-- 08. Store-wise Sales Contribution

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    ROUND(SUM(t.NetSales), 2) AS Store_Net_Sales,
    ROUND(
        SUM(t.NetSales) /
        (SELECT SUM(NetSales)
         FROM retail_transactions_clean) * 100,
        2
    ) AS Sales_Contribution_Percent
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City
ORDER BY Sales_Contribution_Percent DESC;




-- 09. Store-wise Return Analysis

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    COUNT(DISTINCT CASE
        WHEN t.ReturnFlag = 'True' THEN t.OrderID
    END) AS Returned_Orders,
    ROUND(SUM(t.ReturnAmount), 2) AS Total_Return_Amount,
    ROUND(
        COUNT(DISTINCT CASE
            WHEN t.ReturnFlag = 'True' THEN t.OrderID
        END) * 100.0 /
        COUNT(DISTINCT t.OrderID),
        2
    ) AS Return_Rate_Percent
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City
ORDER BY Return_Rate_Percent DESC;




-- 10. Store Type-wise Profit Margin

SELECT
    s.StoreType,
    COUNT(DISTINCT s.StoreID) AS Total_Stores,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit,
    ROUND(
        SUM(t.Profit) / NULLIF(SUM(t.NetSales), 0) * 100,
        2
    ) AS Profit_Margin_Percent
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY s.StoreType
ORDER BY Profit_Margin_Percent DESC;




-- 11. City-wise Store Performance

SELECT
    s.City,
    s.State,
    COUNT(DISTINCT s.StoreID) AS Total_Stores,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.City,
    s.State
ORDER BY Total_Net_Sales DESC;



-- 12. City-wise Average Sales per Store

SELECT
    s.City,
    s.State,
    COUNT(DISTINCT s.StoreID) AS Total_Stores,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(
        SUM(t.NetSales) / COUNT(DISTINCT s.StoreID),
        2
    ) AS Average_Sales_Per_Store,
    ROUND(
        SUM(t.Profit) / COUNT(DISTINCT s.StoreID),
        2
    ) AS Average_Profit_Per_Store
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.City,
    s.State
ORDER BY Average_Sales_Per_Store DESC;




-- 13. Store-wise Yearly Sales Performance

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    t.OrderYear,
    COUNT(DISTINCT t.OrderID) AS Total_Orders,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN stores s
    ON t.StoreID = s.StoreID
GROUP BY
    s.StoreID,
    s.StoreName,
    s.City,
    t.OrderYear
ORDER BY
    s.StoreID,
    t.OrderYear;
    
    
    
-- 14. Store-wise Year-over-Year Sales Growth

WITH Yearly_Sales AS (
    SELECT
        s.StoreID,
        s.StoreName,
        s.City,
        t.OrderYear,
        SUM(t.NetSales) AS Total_Net_Sales
    FROM retail_transactions_clean t
    JOIN stores s
        ON t.StoreID = s.StoreID
    GROUP BY
        s.StoreID,
        s.StoreName,
        s.City,
        t.OrderYear
),

Sales_Growth AS (
    SELECT
        StoreID,
        StoreName,
        City,
        OrderYear,
        Total_Net_Sales,
        LAG(Total_Net_Sales) OVER (
            PARTITION BY StoreID
            ORDER BY OrderYear
        ) AS Previous_Year_Sales
    FROM Yearly_Sales
)

SELECT
    StoreID,
    StoreName,
    City,
    OrderYear,
    ROUND(Total_Net_Sales, 2) AS Current_Year_Sales,
    ROUND(Previous_Year_Sales, 2) AS Previous_Year_Sales,
    ROUND(
        (Total_Net_Sales - Previous_Year_Sales)
        / NULLIF(Previous_Year_Sales, 0) * 100,
        2
    ) AS YoY_Growth_Percent
FROM Sales_Growth
ORDER BY StoreID, OrderYear;




-- 15. Store Ranking by Net Sales

WITH Store_Sales AS (
    SELECT
        s.StoreID,
        s.StoreName,
        s.City,
        s.StoreType,
        SUM(t.NetSales) AS Total_Net_Sales
    FROM retail_transactions_clean t
    JOIN stores s
        ON t.StoreID = s.StoreID
    GROUP BY
        s.StoreID,
        s.StoreName,
        s.City,
        s.StoreType
)

SELECT
    StoreID,
    StoreName,
    City,
    StoreType,
    ROUND(Total_Net_Sales, 2) AS Total_Net_Sales,
    DENSE_RANK() OVER (
        ORDER BY Total_Net_Sales DESC
    ) AS Sales_Rank
FROM Store_Sales
ORDER BY Sales_Rank;



-- 16. Store Ranking by Profit

WITH Store_Profit AS (
    SELECT
        s.StoreID,
        s.StoreName,
        s.City,
        s.StoreType,
        SUM(t.Profit) AS Total_Profit
    FROM retail_transactions_clean t
    JOIN stores s
        ON t.StoreID = s.StoreID
    GROUP BY
        s.StoreID,
        s.StoreName,
        s.City,
        s.StoreType
)

SELECT
    StoreID,
    StoreName,
    City,
    StoreType,
    ROUND(Total_Profit, 2) AS Total_Profit,
    DENSE_RANK() OVER (
        ORDER BY Total_Profit DESC
    ) AS Profit_Rank
FROM Store_Profit
ORDER BY Profit_Rank;





-- 17. Top 5 Stores in Each Region

WITH Store_Sales AS (
    SELECT
        s.StoreID,
        s.StoreName,
        s.City,
        s.Region,
        SUM(t.NetSales) AS Total_Net_Sales
    FROM retail_transactions_clean t
    JOIN stores s
        ON t.StoreID = s.StoreID
    GROUP BY
        s.StoreID,
        s.StoreName,
        s.City,
        s.Region
),

Regional_Ranking AS (
    SELECT
        StoreID,
        StoreName,
        City,
        Region,
        Total_Net_Sales,
        ROW_NUMBER() OVER (
            PARTITION BY Region
            ORDER BY Total_Net_Sales DESC
        ) AS Region_Rank
    FROM Store_Sales
)

SELECT
    StoreID,
    StoreName,
    City,
    Region,
    ROUND(Total_Net_Sales, 2) AS Total_Net_Sales,
    Region_Rank
FROM Regional_Ranking
WHERE Region_Rank <= 5
ORDER BY Region, Region_Rank;



-- 18. Final Store Performance Summary

SELECT
    s.StoreID,
    s.StoreName,
    s.City,
    s.Region,
    s.StoreType,

    COUNT(t.OrderID) AS Total_Orders,

    SUM(t.Quantity) AS Total_Quantity,

    ROUND(SUM(t.NetSales), 2) AS Net_Sales,

    ROUND(SUM(t.Profit), 2) AS Total_Profit,

    ROUND(
        SUM(t.Profit) / NULLIF(SUM(t.NetSales), 0) * 100,
        2
    ) AS Profit_Margin_Percent,

    ROUND(
        SUM(t.NetSales) / COUNT(t.OrderID),
        2
    ) AS Average_Order_Value,

    SUM(
        CASE WHEN t.ReturnFlag = 'True'
        THEN 1 ELSE 0 END
    ) AS Return_Orders,

    ROUND(
        SUM(CASE WHEN t.ReturnFlag = 'True'
        THEN 1 ELSE 0 END) / COUNT(t.OrderID) * 100,
        2
    ) AS Return_Rate_Percent

FROM retail_transactions_clean t

JOIN stores s
    ON t.StoreID = s.StoreID

GROUP BY
    s.StoreID,
    s.StoreName,
    s.City,
    s.Region,
    s.StoreType

ORDER BY Net_Sales DESC;