CREATE DATABASE loaddata;
use loaddata

CREATE TABLE products(
    id int not null primary key,
    product_name varchar(20) not null,
    category_id int not null,
    price int not null,
    sale_price int not null,
    date_into_market  DATE not null
);

LOAD DATA INFILE "C:\\Users\\Suresh\\Desktop\\mySQL\\product - sheet1.csv"
INTO TABLE products
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id,product_name,category_id,price,sale_price,date_into_market);





