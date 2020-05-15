# SELECT * FROM items WHERE price > AVG(price)  # ERROR
#
#
# SELECT * FROM items WHERE price >
# (SELECT AVG(items.price) FROM items);
#
#
# SELECT items.name, items.price - (SELECT AVG(items.price) FROM items) FROM items;
#
# SELECT *, items.price -
# (SELECT AVG(items.price) FROM items WHERE price > 100)
# FROM items WHERE price > 100;
#
# CREATE VIEW expencive_items_diff AS
# SELECT *, items.price -
# (SELECT AVG(items.price) FROM items WHERE price > 100)
# FROM items WHERE price > 100;
#
# SELECT * FROM  expencive_items_diff
#
# DROP VIEW  expencive_items_diff
#
# CREATE VIEW expencive_items_diff AS
# SELECT *, items.price -
# (SELECT AVG(items.price) FROM items WHERE price > 100) AS "average_diff"
# FROM items WHERE price > 100;
#
# SELECT * FROM  expencive_items_diff
#
