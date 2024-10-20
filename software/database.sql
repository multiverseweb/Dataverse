-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS finance_data;
USE finance_data;

-- Create the users table if it does not exist
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Create the income table if it does not exist
CREATE TABLE IF NOT EXISTS income (
    income_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    income_source VARCHAR(50),
    amount DECIMAL(10, 2),
    date_received DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert users data
INSERT INTO users (username, email)
VALUES
    ('JohnDoe', 'john.doe@example.com'),
    ('JaneSmith', 'jane.smith@example.com'),
    ('AliceBrown', 'alice.brown@example.com');

-- Insert income data for users (no IF EXISTS directly allowed, so we assume user_id mapping is correct)
-- For JohnDoe (user_id = 1)
INSERT INTO income (user_id, income_source, amount, date_received)
VALUES
    (1, 'Salary', 1200.00, '2024-10-01'),
    (1, 'Salary', 1300.00, '2024-09-01'),
    (1, 'Investments', 300.00, '2024-09-10'),
    (1, 'Freelancing', 450.00, '2024-09-15');

-- For JaneSmith (user_id = 2)
INSERT INTO income (user_id, income_source, amount, date_received)
VALUES
    (2, 'Salary', 1100.00, '2024-10-01'),
    (2, 'Salary', 1150.00, '2024-09-01'),
    (2, 'Investments', 200.00, '2024-09-12'),
    (2, 'Freelancing', 350.00, '2024-09-18');

-- For AliceBrown (user_id = 3)
INSERT INTO income (user_id, income_source, amount, date_received)
VALUES
    (3, 'Salary', 1400.00, '2024-10-01'),
    (3, 'Salary', 1350.00, '2024-09-01'),
    (3, 'Investments', 400.00, '2024-09-05'),
    (3, 'Freelancing', 500.00, '2024-09-20');
