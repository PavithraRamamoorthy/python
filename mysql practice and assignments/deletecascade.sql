CREATE DATABASE deletecascade;
use deletecascade


CREATE TABLE category(
category_id int not null primary key,
category_name varchar(20) not null
);

INSERT INTO category (category_id,category_name) 
VALUES
(1,"redmi"),
(2,"realme"),
(3,"dell"),
(4,"hp"),
(5,"shirts");


CREATE TABLE products(
    product_id int not null primary key auto_increment,
    product_name varchar(20) not null,
    category_id int not null,
    price int not null,
    sale_price int not null,
    FOREIGN KEY (category_id)
        REFERENCES category(category_id)
        ON DELETE CASCADE
);


INSERT INTO products (product_id,product_name,category_id,price,sale_price)
VALUES
(1,"mobile",1,10000,8000),
(2,"mobile",2,15000,10000),
(3,"labtop",3,50000,40000),
(4,"labtop",4,40000,30000),
(5,"clothes",5,5000,3000);













