-- Create the database if it does not exists
CREATE DATABASE IF NOT EXISTS dataverse;
USE dataverse;

-- Create the users table if it does not exist
CREATE TABLE users (
    u_id BIGINT NOT NULL PRIMARY KEY,
    u_name VARCHAR(255) DEFAULT NULL,
    pwd VARCHAR(255) DEFAULT NULL,
    country VARCHAR(50) DEFAULT 'India'
);


CREATE TABLE finance (
    u_id BIGINT DEFAULT NULL,
    salary FLOAT DEFAULT 0,
    gold FLOAT DEFAULT 0,
    stocks FLOAT DEFAULT 0,
    commodity FLOAT DEFAULT 0,
    sales FLOAT DEFAULT 0,
    expenditure FLOAT DEFAULT 0,
    total FLOAT GENERATED ALWAYS AS (salary + gold + stocks + commodity + sales - expenditure) STORED,
    entryDate DATE DEFAULT NULL
);
