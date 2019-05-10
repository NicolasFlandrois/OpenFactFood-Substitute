CREATE TABLE Categories ( 
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category VARCHAR(40) NOT NULL,
    subcategory VARCHAR(40),
    origin_ean SMALLINT NOT NULL,
    substitute_ean SMALLINT NOT NULL,
    PRIMARY KEY (id)
) --Table 1
ENGINE=INNODB;

CREATE TABLE Products ( 
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ean SMALLINT NOT NULL,
    product_name VARCHAR(40),
    PRIMARY KEY (id)
) --Table 2
ENGINE=INNODB;

CREATE TABLE History ( 
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    origin_ean SMALLINT NOT NULL,
    substitute_ean SMALLINT NOT NULL,
    status CHAR(1),
    date_change DATETIME NOT NULL,
    comments TEXT,
    PRIMARY KEY (id)
) --Table 3
ENGINE=INNODB;