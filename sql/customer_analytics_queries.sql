
CREATE TABLE online_retail(
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate TIMESTAMP,
    UnitPrice FLOAT,
    CustomerID FLOAT,
    Country TEXT,
    total_price FLOAT,
    month VARCHAR(10)
);

ALTER TABLE online_retail
ALTER COLUMN total_price
TYPE NUMERIC (10,2);

--1 Revenue by country

SELECT Country,
SUM(total_price) AS revenue
FROM online_retail
GROUP BY Country
ORDER BY revenue DESC
LIMIT 10;


--2 Top customers by revenue

SELECT CustomerID,
SUM(total_price) AS revenue
FROM online_retail
GROUP BY CustomerID
ORDER BY revenue DESC
LIMIT 10;


--3 Monthly revenue

SELECT month,
SUM(total_price) AS revenue
FROM online_retail
GROUP BY month
ORDER BY month;


--4 Top products by revenue

SELECT Description,
SUM(total_price) AS revenue
FROM online_retail
GROUP BY Description
ORDER BY revenue DESC
LIMIT 10;

--Top products by quantity sold
SELECT Description,
SUM(Quantity) AS total_quantity
FROM online_retail
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 10;

--Product quantity vs Revenue Comparision
SELECT Description,
SUM(Quantity) AS total_quantity,
SUM(total_price) AS revenue
FROM online_retail
GROUP BY Description
ORDER BY revenue DESC
LIMIT 10;

--Repeated Customers
SELECT CustomerID,
COUNT(DISTINCT InvoiceNo) AS purchases
FROM online_retail
GROUP BY CustomerID
ORDER BY purchases DESC
LIMIT 10;

--highest and Lowest sales month
SELECT

(SELECT month
FROM online_retail
GROUP BY month
ORDER BY SUM(total_price) DESC
LIMIT 1)
AS highest_sales_month,

(SELECT month
FROM online_retail
GROUP BY month
ORDER BY SUM(total_price)
LIMIT 1)
AS lowest_sales_month;

--Average order value
SELECT 
AVG(total_price) AS average_order_value
FROM online_retail;

--Average Order Value By Country
SELECT Country,
AVG(total_price) as average_order_value
FROM online_retail
GROUP BY country
ORDER BY average_order_value DESC
LIMIT 10;

--High revenue low quantity products
SELECT Description,
SUM(Quantity) AS total_quantity,
SUM(total_price) AS revenue
FROM online_retail
GROUP BY Description

HAVING SUM(Quantity) < (SELECT AVG(total_quantity)
FROM (SELECT SUM(Quantity) AS total_quantity
FROM online_retail
GROUP BY Description)
temp)
ORDER BY revenue DESC
LIMIT 10;

--Top customer contribution %
WITH top10_revenue AS
(
SELECT SUM(total_price) AS revenue
FROM online_retail
WHERE CustomerID IN
(
SELECT CustomerID
FROM online_retail
GROUP BY CustomerID
ORDER BY SUM(total_price) DESC
LIMIT 10
))

SELECT ROUND (revenue * 100/
(SELECT SUM(total_price)
FROM online_retail),2)
AS contribution_percentage
FROM top10_revenue;





