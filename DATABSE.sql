CREATE DATABASE CRYPTO_TRACKER;
USE CRYPTO_TRACKER;

CREATE TABLE CRYPTO(
ID INT auto_increment PRIMARY KEY,
COIN VARCHAR(50),
PRICE FLOAT,
TIMESTAMP DATETIME DEFAULT current_timestamp
);

Alter Table crypto
modify column timestamp datetime default current_timestamp;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM CRYPTO WHERE ID < 547;
commit;
select * from CRYPTO;
SELECT * FROM CRYPTO ORDER BY TIMESTAMP DESc;

SET autocommit = 1;