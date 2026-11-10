USE retail_sales_analysis;

SELECT
    p.Category,
    COUNT(t.OrderID) AS Total_Orders,
    COUNT(DISTINCT t.ProductID) AS Total_Products,
    SUM(t.Quantity) AS Total_Quantity,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Net_Sales DESC;




SELECT
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand,
    COUNT(t.OrderID) AS Total_Orders,
    SUM(t.Quantity) AS Total_Quantity_Sold,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand
ORDER BY Total_Net_Sales DESC
LIMIT 10;





SELECT
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand,
    SUM(t.Quantity) AS Total_Quantity_Sold,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand
ORDER BY Total_Profit DESC
LIMIT 10;



SELECT
    p.Brand,
    COUNT(DISTINCT p.ProductID) AS Total_Products,
    COUNT(t.OrderID) AS Total_Orders,
    SUM(t.Quantity) AS Total_Quantity_Sold,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Brand
ORDER BY Total_Net_Sales DESC;





SELECT
    p.Category,
    SUM(t.Quantity) AS Total_Quantity_Sold,
    COUNT(t.OrderID) AS Total_Orders,
    ROUND(AVG(t.Quantity), 2) AS Average_Quantity_Per_Order,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Quantity_Sold DESC;





SELECT
    p.Category,
    SUM(t.ReturnQuantity) AS Total_Return_Quantity,
    COUNT(CASE WHEN t.ReturnFlag = 1 THEN 1 END) AS Total_Return_Orders,
    ROUND(SUM(t.ReturnAmount), 2) AS Total_Return_Amount
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Return_Quantity DESC;




SELECT
    ReturnFlag,
    COUNT(*) AS Total_Records
FROM retail_transactions_clean
GROUP BY ReturnFlag;



SELECT
    p.Category,
    SUM(t.ReturnQuantity) AS Total_Return_Quantity,
    COUNT(CASE WHEN t.ReturnFlag = TRUE THEN 1 END) AS Total_Return_Orders,
    ROUND(SUM(t.ReturnAmount), 2) AS Total_Return_Amount
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Return_Quantity DESC;



DESCRIBE retail_transactions_clean;


SELECT
    p.Category,
    SUM(t.ReturnQuantity) AS Total_Return_Quantity,
    COUNT(CASE WHEN t.ReturnFlag = 'True' THEN 1 END) AS Total_Return_Orders,
    ROUND(SUM(t.ReturnAmount), 2) AS Total_Return_Amount
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Return_Quantity DESC;




SELECT
    p.Category,
    COUNT(t.OrderID) AS Total_Orders,
    COUNT(CASE WHEN t.ReturnFlag = 'True' THEN 1 END) AS Returned_Orders,
    ROUND(
        COUNT(CASE WHEN t.ReturnFlag = 'True' THEN 1 END)
        * 100.0 / COUNT(t.OrderID), 2
    ) AS Return_Rate_Percentage
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Return_Rate_Percentage DESC;




SELECT
    p.Brand,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit,
    ROUND(
        SUM(t.Profit) * 100.0 / SUM(t.NetSales), 2
    ) AS Profit_Margin_Percentage
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Brand
ORDER BY Profit_Margin_Percentage DESC;




SELECT
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand,
    SUM(t.ReturnQuantity) AS Total_Return_Quantity,
    COUNT(CASE WHEN t.ReturnFlag = 'True' THEN 1 END) AS Return_Orders,
    ROUND(SUM(t.ReturnAmount), 2) AS Total_Return_Amount
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand
HAVING SUM(t.ReturnQuantity) > 0
ORDER BY Total_Return_Quantity DESC
LIMIT 10;



SELECT
    p.Category,
    ROUND(AVG(p.UnitPrice), 2) AS Average_Product_Price,
    ROUND(MIN(p.UnitPrice), 2) AS Minimum_Product_Price,
    ROUND(MAX(p.UnitPrice), 2) AS Maximum_Product_Price,
    COUNT(DISTINCT p.ProductID) AS Total_Products
FROM products p
GROUP BY p.Category
ORDER BY Average_Product_Price DESC;




SELECT
    Category,
    ROUND(AVG(UnitPrice), 2) AS Average_Selling_Price,
    ROUND(AVG(UnitCost), 2) AS Average_Cost_Price,
    ROUND(AVG(UnitPrice - UnitCost), 2) AS Average_Unit_Profit,
    ROUND(
        AVG((UnitPrice - UnitCost) * 100.0 / UnitPrice), 2
    ) AS Average_Markup_Percentage
FROM products
GROUP BY Category
ORDER BY Average_Markup_Percentage DESC;





SELECT
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand,
    ROUND(SUM(t.Profit) / SUM(t.Quantity), 2) AS Average_Profit_Per_Unit,
    SUM(t.Quantity) AS Total_Quantity_Sold,
    ROUND(SUM(t.Profit), 2) AS Total_Profit
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY
    p.ProductID,
    p.ProductName,
    p.Category,
    p.Brand
HAVING SUM(t.Quantity) > 0
ORDER BY Average_Profit_Per_Unit DESC
LIMIT 10;




SELECT
    Brand,
    COUNT(ProductID) AS Total_Products,
    ROUND(AVG(UnitPrice), 2) AS Average_Selling_Price,
    ROUND(AVG(UnitCost), 2) AS Average_Cost_Price,
    ROUND(AVG(UnitPrice - UnitCost), 2) AS Average_Unit_Profit
FROM products
GROUP BY Brand
ORDER BY Average_Selling_Price DESC;




SELECT
    p.Category,
    COUNT(DISTINCT p.ProductID) AS Total_Products,
    SUM(t.Quantity) AS Total_Quantity_Sold,
    ROUND(SUM(t.NetSales), 2) AS Total_Net_Sales,
    ROUND(SUM(t.Profit), 2) AS Total_Profit,
    ROUND(
        SUM(t.Profit) * 100.0 / SUM(t.NetSales), 2
    ) AS Profit_Margin_Percentage
FROM retail_transactions_clean t
JOIN products p
    ON t.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Profit DESC;