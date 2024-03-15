-- A script that lists all records of the table second_table of the database
-- and doesn't list rows without a name
-- and records are listed by descending score order.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
