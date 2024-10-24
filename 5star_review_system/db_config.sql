CREATE DATABASE IF NOT EXISTS dataverse;

USE dataverse;

CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    rating INT,
    review TEXT,
    timestamp DATETIME
);
