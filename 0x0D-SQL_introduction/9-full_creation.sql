-- A script that creates a table 'second_table' in the database.

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO TABLE second_table VALUE (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);