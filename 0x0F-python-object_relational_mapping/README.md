A readme on Object-relational mapping project with python given by ALX.

An Object-relational Mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

ORMs are useful becausethey provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.

## Background Context
In this project, we will link two amazing worlds: Databases and Python!

In the first part, we will use the module MySQLdb to connect to a MySQL database and execute our SQL queries.

In the second part, we will use the module SQLAlchemy bject Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, our biggest concern will be “What can we do with our objects” and not “How this object is stored? where? when?”. We won’t write any SQL queries only Python code. Last thing, our code won’t be “storage type” dependent. We will be able to change our storage easily without re-writing our entire project.

## Learning Objectives
At the end of this project, we are expected to be able to explain to anyone, the following:
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERTS rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
