-- Teaching schema for the sales analytics course.
-- Run only in a database you own. Adjust types, indexes, currency, and rules for your use case.
CREATE DATABASE IF NOT EXISTS analytics;
USE analytics;

CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(32) PRIMARY KEY,
    customer_name VARCHAR(120) NULL,
    region VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(32) PRIMARY KEY,
    order_date DATETIME NOT NULL,
    customer_id VARCHAR(32) NOT NULL,
    status VARCHAR(20) NOT NULL,
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    INDEX idx_orders_date_region (order_date, status)
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id VARCHAR(32) NOT NULL,
    product VARCHAR(100) NOT NULL,
    category VARCHAR(60) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    unit_cost DECIMAL(12,2) NOT NULL,
    CONSTRAINT fk_items_order FOREIGN KEY (order_id) REFERENCES orders(order_id),
    INDEX idx_items_product_category (category, product)
);

-- Example: bind the values using the driver; do not interpolate them into SQL.
-- SELECT order_id, order_date, status FROM orders
-- WHERE order_date >= %s AND order_date < %s ORDER BY order_date, order_id;
