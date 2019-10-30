# SELECT * FROM purchases;
# SELECT * FROM items;
# SELECT * FROM customers;
# SELECT * FROM purchases;
# SELECT * FROM items INNER JOIN purchases ON items.id = purchases.item_id;
# SELECT * FROM items LEFT JOIN purchases ON items.id = purchases.item_id;
# SELECT * FROM purchases RIGHT JOIN items ON items.id = purchases.item_id;
# SELECT * FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
# SELECT * FROM customers LEFT JOIN purchases ON customers.id = purchases.customer_id;
# SELECT customers.first_name, customers.last_name FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id;
#
# SELECT * FROM items
# INNER JOIN purchases ON items.id = purchases.item_id;
#
# SELECT * FROM items
# INNER JOIN purchases ON items.id = purchases.item_id
# INNER JOIN customers ON purchases.customers_id = customers.id;
#
# SELECT  customers.first_name, customers.last_name, items.name, items.price FROM items
# INNER JOIN purchases ON items.id = purchases.item_id
# INNER JOIN customers ON purchases.customers_id = customers.id;
