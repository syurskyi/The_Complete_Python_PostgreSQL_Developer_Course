# SELECT * FROM purchases INNER JOIN items on purchases.item_id = items.id;
#
# SELECT SUM(items.price) FROM purchases INNER JOIN items on purchases.item_id = items.id;
#
# SELECT * FROM items
# INNER JOIN purchases ON purchases.item_id = items.id
# INNER JOIN customers OM purchases.customers_id = customers.id;
#
# SELECT customers.first_name, customers.last_name, items.price FROM items
# INNER JOIN purchases ON purchases.item_id = items.id
# INNER JOIN customers OM purchases.customers_id = customers.id;
#
# SELECT customers.first_name, customers.last_name, SUM(items.price) FROM items
# INNER JOIN purchases ON purchases.item_id = items.id
# INNER JOIN customers OM purchases.customers_id = customers.id
# GROUP BY customers.id;
#
# SELECT customers.first_name, customers.last_name, SUM(items.price) AS "total_spent" FROM items
# INNER JOIN purchases ON purchases.item_id = items.id
# INNER JOIN customers OM purchases.customers_id = customers.id
# GROUP BY customers.id
# ORDER BY total_spend;
#
# SELECT customers.first_name, customers.last_name, SUM(items.price) AS "total_spent" FROM items
# INNER JOIN purchases ON purchases.item_id = items.id
# INNER JOIN customers OM purchases.customers_id = customers.id
# GROUP BY customers.id
# ORDER BY total_spend DESC;
#
# SELECT customers.first_name, customers.last_name, SUM(items.price) AS "total_spent" FROM items
# INNER JOIN purchases ON purchases.item_id = items.id
# INNER JOIN customers OM purchases.customers_id = customers.id
# GROUP BY customers.id
# ORDER BY total_spend DESC
# LIMIT 1;
