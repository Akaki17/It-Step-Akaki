-- Create Customers table
CREATE TABLE Customers (
    customer_ID SERIAL PRIMARY KEY NOT NULL,
    full_name VARCHAR(30),
    email VARCHAR(30),
    phone VARCHAR(35)
);

-- Create Sales table
CREATE TABLE Sales (
    sale_ID SERIAL PRIMARY KEY,
    customer_ID INT,
    product_name VARCHAR(25),
    quantity FLOAT,
    unit_price FLOAT,
    sale_date TIMESTAMP,
    FOREIGN KEY (customer_ID) REFERENCES Customers (customer_ID)
);

-- Insert data into Customers table
INSERT INTO Customers (full_name, email, phone)
VALUES
('Akaki Surmava', 'a.surmava@gmail.com', '+967 345 765'),
('Nino Larneki', 'n.larneki@gmail.com', '+967 435 234'),
('Levani Gamrekeli', 'l.gamrekeli@gmail.com', '+967 876 132'),
('Manana Menabde', 'm.menabde@gmail.com', '+967 876 456'),
('Ana Chaganava', 'a.chaganava@gmail.com', '+967 098 890'),
('Stela Melini', 's.melini@gmail.com', '+967 786 897'),
('Goga Maver', 'g.maver@gmail.com', '+967 564 091'),
('Melini Sorsia', 'm.sorsia@gmail.com', '+967 396 730');

-- Insert data into Sales table
INSERT INTO Sales (customer_ID, product_name, quantity, unit_price, sale_date)
VALUES
(1, 't-shirt', 2, 114, '2024-10-01'),
(2, 'short', 1, 50, '2024-09-25'),
(3, 'stocking', 5, 11, '2024-10-09'),
(4, 'shirt', 3, 159, '2024-10-04'),
(5, 'shoes', 1, 219, '2024-10-07'),
(6, 'trousers', 2, 189, '2024-10-05'),
(7, 'underwear', 5, 19, '2024-10-15'),
(8, 'dress', 3, 79, '2024-10-11');

-- Total Revenue
SELECT SUM(Sales.unit_price) AS TotalRevenue
FROM Sales;

-- Average Sales
SELECT AVG(Sales.unit_price) AS AverageSales
FROM Sales;

-- Customers with sales
SELECT Customers.full_name, Sales.product_name, Sales.quantity, Sales.unit_price, Sales.sale_date
FROM Sales
JOIN Customers ON Sales.customer_ID = Customers.customer_ID;

-- Customers without sales
SELECT Customers.full_name
FROM Customers
LEFT JOIN Sales ON Customers.customer_ID = Sales.customer_ID
WHERE Sales.customer_ID IS NULL;

-- Product that sold
SELECT product_name, SUM(quantity) AS TotalQuantitySold
FROM Sales
GROUP BY product_name;

-- Whole info
SELECT Customers.full_name, SUM(Sales.unit_price) AS TotalRevenue
FROM Sales
JOIN Customers ON Sales.customer_ID = Customers.customer_ID
GROUP BY Customers.full_name;
