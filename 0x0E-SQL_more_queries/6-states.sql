-- Creates the database hbtn_0d_usa and the table states(in hbtn_0d_usa) on MySQL server
-- states description:
-- 	id INT unique, auto generated, can't be null and is a primary key
-- 	name VARCHAR(256) can't be null
-- The database name will be passed as an argument of the mysql command
-- If the table states already exists, the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
