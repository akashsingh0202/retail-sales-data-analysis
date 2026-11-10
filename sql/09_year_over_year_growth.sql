USE retail_sales_analysis;



-- 09. Year-over-Year Sales Growth

WITH Yearly_Sales AS (
    SELECT
        OrderYear,
        ROUND(SUM(NetSales), 2) AS Total_Sales
    FROM retail_transactions_clean
    GROUP BY OrderYear
),

Sales_Growth AS (
    SELECT
        OrderYear,
        Total_Sales,
        LAG(Total_Sales) OVER (
            ORDER BY OrderYear
        ) AS Previous_Year_Sales
    FROM Yearly_Sales
)

SELECT
    OrderYear,
    Total_Sales,
    Previous_Year_Sales,
    ROUND(
        (Total_Sales - Previous_Year_Sales)
        / Previous_Year_Sales * 100,
        2
    ) AS Growth_Percentage
FROM Sales_Growth
ORDER BY OrderYear;
