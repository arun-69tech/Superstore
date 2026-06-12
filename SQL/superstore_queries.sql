/*=========================================================
SUPERSTORE SALES ANALYSIS - SQL QUERIES
=========================================================*/

USE superstore_db;

/*=========================================================
1. Total Sales
=========================================================*/
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore;


/*=========================================================
2. Total Profit
=========================================================*/
SELECT
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore;


/*=========================================================
3. Total Orders
=========================================================*/
SELECT
    COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM superstore;


/*=========================================================
4. Total Customers
=========================================================*/
SELECT
    COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM superstore;


/*=========================================================
5. Profit Margin Percentage
=========================================================*/
SELECT
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Percentage
FROM superstore;


/*=========================================================
6. Average Order Value
=========================================================*/
SELECT
    ROUND(
        SUM(Sales) / COUNT(DISTINCT `Order ID`),
        2
    ) AS Average_Order_Value
FROM superstore;


/*=========================================================
7. Sales by Region
=========================================================*/
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;


/*=========================================================
8. Profit by Region
=========================================================*/
SELECT
    Region,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Profit DESC;


/*=========================================================
9. Sales by Category
=========================================================*/
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;


/*=========================================================
10. Profit by Category
=========================================================*/
SELECT
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;


/*=========================================================
11. Sales by Segment
=========================================================*/
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;


/*=========================================================
12. Profit by Segment
=========================================================*/
SELECT
    Segment,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Segment
ORDER BY Total_Profit DESC;


/*=========================================================
13. Top 10 Customers by Sales
=========================================================*/
SELECT
    `Customer Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;


/*=========================================================
14. Top 10 Products by Sales
=========================================================*/
SELECT
    `Product Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;


/*=========================================================
15. Top 10 Products by Profit
=========================================================*/
SELECT
    `Product Name`,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Profit DESC
LIMIT 10;


/*=========================================================
16. Bottom 10 Products by Profit
=========================================================*/
SELECT
    `Product Name`,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Profit ASC
LIMIT 10;


/*=========================================================
17. Sales by State
=========================================================*/
SELECT
    State,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY State
ORDER BY Total_Sales DESC;


/*=========================================================
18. Bottom 10 States by Profit
=========================================================*/
SELECT
    State,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY State
ORDER BY Total_Profit ASC
LIMIT 10;


/*=========================================================
19. Monthly Sales Trend
=========================================================*/
SELECT
    YEAR(`Order Date`) AS Order_Year,
    MONTH(`Order Date`) AS Order_Month,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY
    YEAR(`Order Date`),
    MONTH(`Order Date`)
ORDER BY
    Order_Year,
    Order_Month;


/*=========================================================
20. Monthly Profit Trend
=========================================================*/
SELECT
    YEAR(`Order Date`) AS Order_Year,
    MONTH(`Order Date`) AS Order_Month,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY
    YEAR(`Order Date`),
    MONTH(`Order Date`)
ORDER BY
    Order_Year,
    Order_Month;


/*=========================================================
21. Quarterly Sales Performance
=========================================================*/
SELECT
    QUARTER(`Order Date`) AS Quarter,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Quarter
ORDER BY Quarter;


/*=========================================================
22. Average Sales per Customer
=========================================================*/
SELECT
    ROUND(
        SUM(Sales) / COUNT(DISTINCT `Customer ID`),
        2
    ) AS Avg_Sales_Per_Customer
FROM superstore;


/*=========================================================
23. Average Profit per Customer
=========================================================*/
SELECT
    ROUND(
        SUM(Profit) / COUNT(DISTINCT `Customer ID`),
        2
    ) AS Avg_Profit_Per_Customer
FROM superstore;


/*=========================================================
24. Average Sales per Product
=========================================================*/
SELECT
    ROUND(
        SUM(Sales) / COUNT(DISTINCT `Product Name`),
        2
    ) AS Avg_Sales_Per_Product
FROM superstore;


/*=========================================================
25. Best Performing Region
=========================================================*/
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC
LIMIT 1;


/*=========================================================
26. Best Customer Segment
=========================================================*/
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC
LIMIT 1;


/*=========================================================
27. Best Product Category
=========================================================*/
SELECT
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC
LIMIT 1;


/*=========================================================
28. Strongest Quarter
=========================================================*/
SELECT
    QUARTER(`Order Date`) AS Quarter,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Quarter
ORDER BY Total_Sales DESC
LIMIT 1;


/*=========================================================
END OF SQL QUERIES
=========================================================*/