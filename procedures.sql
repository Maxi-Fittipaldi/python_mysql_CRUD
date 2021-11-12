DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `pr_create`(IN `id` INT, IN `name` VARCHAR(25), IN `q_in_stock` INT, IN `unit_price` DECIMAL(4,2))
INSERT INTO products (product_id,name,quantity_in_stock,unit_price) VALUES(id, name, q_in_stock, unit_price)$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `pr_delete`(
	IN id INT
)
DELETE FROM products WHERE product_id = id$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `pr_read`()
SELECT * FROM products$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `pr_update`(
	IN id INT,
    IN name VARCHAR(50),
    IN q_in_stock INT,
    IN u_price decimal(4,2)
)
UPDATE products 
	SET name = name, 
	quantity_in_stock = q_in_stock, 
	unit_price = u_price 
WHERE product_id = id$$
DELIMITER ;