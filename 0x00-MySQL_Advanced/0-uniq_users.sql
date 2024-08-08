-- Write a SQL script that creates a table users

CREATE TABLE users IF NOT EXISTS (
	    id INT AUTO_INCREMENT,
	    email VARCHAR(255) NOT NULL UNIQUE,
	    name VARCHAR(255),
	    PRIMARY KEY (id)
	    );
