-- removes all records with a score <= 5 in the table second_table
DELETE FROM second_table
WHERE `score` >=10;

SELECT `score`,`name` FROM second_table;
