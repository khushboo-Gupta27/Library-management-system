create database db;

CREATE TABLE books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));

CREATE TABLE books_issued(bid varchar(20) primary key, issuedto varchar(30));

SELECT *FROM books;
SELECT *FROM books_issued;
desc books;
desc books_issued;