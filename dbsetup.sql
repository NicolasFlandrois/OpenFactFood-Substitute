-- Date: Fri 10 May 2019 16:43:14 CEST 
-- Author: Nicolas Flandrois
-- This script will create the initial database for OpenFoodFacts Porject#5

-- Personal note: How to make it happen? Execute from python? 
-- How to import from csv and not take in account the headers?
-- (erase after solving issue)

CREATE DATABASE off1 CHARACTER SET 'UTF8';

--Table 1
CREATE TABLE Categories ( 
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    category VARCHAR(40) NOT NULL,
    origin_ean VARCHAR(13) NOT NULL,
    substitute_ean VARCHAR(13) NOT NULL,
    PRIMARY KEY (id)
) 
ENGINE=INNODB;

LOAD DATA LOCAL INFILE 'tbl1_cat.csv'
    INTO TABLE Categories
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (category, origin_ean, substitute_ean);

--Table 2
CREATE TABLE Products ( 
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ean VARCHAR(13) NOT NULL,
    product_name TEXT,
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
    origin_ean VARCHAR(13) NOT NULL,
    substitute_ean VARCHAR(13) NOT NULL,
    substitute_status CHAR(1),
    date_change DATETIME NOT NULL,
    comments TEXT,
    PRIMARY KEY (id)
) 
ENGINE=INNODB;

LOAD DATA LOCAL INFILE 'tbl3_historic.csv'
    INTO TABLE History
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (origin_ean, substitute_ean, substitute_status, date_change, comments);