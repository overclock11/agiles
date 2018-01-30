CREATE TABLE IF NOT EXISTS `prueba_user` (
	`id`	integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`name`	varchar ( 100 ) NOT NULL,
	`user`	varchar ( 30 ) NOT NULL,
	`passw`	varchar ( 15 ) NOT NULL,
	`photo`	text NOT NULL,
	`country`	varchar ( 50 ) NOT NULL,
	`city`	varchar ( 50 ) NOT NULL,
	`address`	varchar ( 50 ) NOT NULL,
	`email`	varchar ( 50 ) NOT NULL
);
CREATE TABLE IF NOT EXISTS `prueba_category` (
	`id`	integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`name`	varchar ( 50 ) NOT NULL
);
CREATE TABLE IF NOT EXISTS `prueba_promotion` (
	`id`	integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`name`	varchar ( 50 ) NOT NULL,
	`value`	integer NOT NULL,
	`description`	text NOT NULL,
	`image`	text NOT NULL,
	`category_id`	integer,
	FOREIGN KEY(`category_id`) REFERENCES `prueba_category`(`id`) 
);
CREATE TABLE IF NOT EXISTS `prueba_favourite` (
	`id`	integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`category_id`	integer,
	`user_id`	integer,
	FOREIGN KEY(`category_id`) REFERENCES `prueba_category`(`id`) ,
	FOREIGN KEY(`user_id`) REFERENCES `prueba_user`(`id`) 
);
CREATE TABLE IF NOT EXISTS `prueba_commentary` (
	`id`	integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`comment`	text NOT NULL,
	`promotion_id`	integer,
	`user_id`	integer,
	FOREIGN KEY(`user_id`) REFERENCES `prueba_user`(`id`) ,
	FOREIGN KEY(`promotion_id`) REFERENCES `prueba_promotion`(`id`) 
);