-- Date: Fri 10 May 2019 16:43:14 CEST 
-- Author: Nicolas Flandrois
-- This script will create the initial database for OpenFoodFacts Porject#5

CREATE DATABASE openfoodfacts CHARACTER SET 'utf8';

--Table 1
CREATE TABLE Categories ( 
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category VARCHAR(40) NOT NULL,
    subcategory VARCHAR(40),
    origin_ean SMALLINT NOT NULL,
    substitute_ean SMALLINT NOT NULL,
    PRIMARY KEY (id)
) 
ENGINE=INNODB;

LOAD DATA LOCAL INFILE 'tbl1_cat.csv'
    INTO TABLE Categories
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (category, subcategory, origin_ean, substitute_ean);

--Table 2
CREATE TABLE Products ( 
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ean SMALLINT NOT NULL,
    product_name VARCHAR(40),
    PRIMARY KEY (id)
) 
ENGINE=INNODB;

LOAD DATA LOCAL INFILE 'tbl2_prod.csv'
    INTO TABLE Products
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (ean, product_name);

--Table 3
CREATE TABLE History ( 
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    origin_ean SMALLINT NOT NULL,
    substitute_ean SMALLINT NOT NULL,
    status CHAR(1),
    date_change DATETIME NOT NULL,
    comments TEXT,
    PRIMARY KEY (id)
) 
ENGINE=INNODB;

LOAD DATA LOCAL INFILE 'tbl3_historic.csv'
    INTO TABLE History
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (origin_ean, substitute_ean, status, date_change, comments);