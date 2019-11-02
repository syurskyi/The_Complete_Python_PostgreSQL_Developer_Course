SELECT customers.first_name, customers.last_name, SUM(items.price) FROM customers
INNER JOIN purchases ON customers.id = purchases.customer_id
INNER JOIN items ON purchases.item_id = items.id
GROUP BY customers.id;

CREATE VIEW total_revenue_per_customer AS
SELECT customers.first_name, customers.last_name, SUM(items.price) FROM customers
INNER JOIN purchases ON customers.id = purchases.customer_id
INNER JOIN items ON purchases.item_id = items.id
GROUP BY customers.id;

SELECT * FROM total_revenue_per_customer;

DROP VIEW total_revenue_per_customer;

CREATE VIEW total_revenue_per_customer AS
SELECT customers.id, customers.first_name, customers.last_name, SUM(items.price) FROM customers
INNER JOIN purchases ON customers.id = purchases.customer_id
INNER JOIN items ON purchases.item_id = items.id
GROUP BY customers.id;

SELECT * FROM total_revenue_per_customer;

SELECT * FROM items;

INSERT INTO purchses
VALUE(11, 6, 5);

SELECT * FROM total_revenue_per_customer;

SELECT * FROM total_revenue_per_customer WHERE sum > 150;

CREATE VIEW awesome_customer AS
SELECT * FROM total_revenue_per_customer WHERE sum > 150;

SELECT * FROM awesome_customer;

SELECT * FROM awesome_customer ORDER BY sum DESC;

CREATE VIEW expencive_items AS
SELECT *FROM items WHERE price > 100;

SELECT * FROM  expencive_items;


INSERT INTO expencive_items(id, name, price)
VALUES(9, 'DSLR', 400.00)

SELECT * FROM  expencive_items;

DROP VIEW expencive_items;

CREATE VIEW expencive_items AS
SELECT *FROM items WHERE price >= 100
WITH LOCAL CHECK OPTION;


INSERT INTO expencive_items(id, name, price)
VALUES(11, 'Pencil', 2.00)

DROP VIEW expencive_items;
CREATE VIEW expencive_items AS
SELECT *FROM items WHERE price > 100;

CREATE VIEW non_luxury_items AS
SELECT *FROM expencive_items WHERE price < 10000
WITH LOCAL CHECK OPTION

INSERT INTO non_luxury_items(id, name, price)
VALUES(11, 'Pencil', 2.00)

DROP VIEW non_luxury_items

CREATE VIEW non_luxury_items AS
SELECT *FROM expencive_items WHERE price < 10000
WITH CASCADED CHECK OPTION

INSERT INTO non_luxury_items(id, name, price)
VALUES(11, 'Pencil', 2.00)
