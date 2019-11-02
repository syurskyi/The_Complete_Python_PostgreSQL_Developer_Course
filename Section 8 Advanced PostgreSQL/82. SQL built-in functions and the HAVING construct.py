SELECT customers.first_name, customers.last_name, COUNT(purchases.id) AS purchase_count
FROM customers
INNER JOIN purchases ON customers.id = purchases.customer_id
GROUP BY customer.id;

SELECT AVG (items.price) FROM items;

SELECT AVG (items.price) FROM items
INNER JOIN purchases ON items.id = purchases.item_id;

SELECT * FROM items;

SELECT items.name, items.price FROM items
INNER JOIN purchases ON items.id = purchases.item_id
ORDER BY items.price;

SELECT items.name, items.price FROM items
INNER JOIN purchases ON items.id = purchases.item_id
ORDER BY items.price DESC
LIMIT 1;

SELECT MAX(items.price) FROM items
INNER JOIN purchases ON items.id = purchases.item_id;

SELECT customers.first_name, customers.last_name, COUNT(purchases.id) AS purchase_count
FROM customers
INNER JOIN purchases ON customers.id = purchases.customers_id
GROUP BY customers.id;

SELECT customers.first_name, customers.last_name, COUNT(purchases.id) AS purchase_count
FROM customers
INNER JOIN purchases ON customers.id = purchases.customers_id
HAVING COUNT(purchases.id) > 3;
