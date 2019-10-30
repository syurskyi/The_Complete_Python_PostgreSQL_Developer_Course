SELECT * FROM customers LEFT JOIN purchases ON customers.id = purchases.customers_id;

SELECT customers.first_name, customers.last_name, purchases.id FROM customers LEFT JOIN purchases ON customers.id = purchases.customers_id;

SELECT customers.first_name, customers.last_name, COUNT(purchases.id) FROM customers LEFT JOIN purchases ON customers.id = purchases.customers_id
GROUP BY customers.id;

SELECT *FROM customers GROUP BY customers.id;

SELECT customers.first_name, customers.last_name, SUM(items.price) FROM items 
INNER JOIN purchases ON items.id = purchases.item_id
INNER JOIN customers ON purchases.customers_id = customers.id
GROUP BY customers.id ;
