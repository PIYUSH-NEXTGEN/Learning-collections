# SQL Basics

## What is SQL?

SQL (Structured Query Language) is a programming language used for managing and manipulating data in relational databases.

It allows users to:
- Insert data
- Update data
- Retrieve data
- Delete data

SQL is widely used in applications, websites, and software systems for data management.

In simple terms, SQL is used to communicate with and control databases.

---

# Types of SQL Commands

## 1. DDL (Data Definition Language)

Used to define and manage database structures.

- `CREATE` → Creates new database objects.
- `ALTER` → Modifies existing database objects.
- `DROP` → Deletes existing database objects.
- `TRUNCATE` → Removes all rows from a table.

---

## 2. DML (Data Manipulation Language)

Used to manipulate data stored in tables.

- `INSERT` → Adds new rows into a table.
- `UPDATE` → Modifies existing data in a table.
- `DELETE` → Removes data from a table.
- `SELECT` → Retrieves data from a table.

---

## 3. DCL (Data Control Language)

Used to control access and permissions.

- `GRANT` → Gives access rights to users.
- `REVOKE` → Removes access rights from users.

---

## 4. TCL (Transaction Control Language)

Used to manage transactions in a database.

- `COMMIT` → Saves changes permanently.
- `ROLLBACK` → Undoes changes that are not committed.

### Rules - 
- Keywords should be in caps.
- Object name should be in all small letters.

## DDL COMMANDS FOR DATABASE
- CREATE DATABASE campusx<br>
or
- CREATE DATABASE IF NOT EXISTS campusx <br>
This will create a new db.


- DROP DATABASE IF EXISTS campusx <br>
It will delete the db.

## DDL COMMANDS FOR TABLE <br>
```
CREATE TABLE users(
    id INTEGER,
    name VARCHAR(255),
    age INTEGER,
    city VARCHAR(255)
);
```
This will create a table named users with 4 columns - id, name, age and city.

### TRUNCATE TABLE users <br>
This will remove all rows from the users table but keep the structure intact.

### DROP TABLE IF EXISTS users
This will delete the users table.

## Data integrity -
Data integrity refers to the accuracy and consistency of data stored in a database. 
It ensures that the data is reliable and can be trusted for analysis and decision-making 
and the data in a database is protected from errors, or unauthorized changes.

There are various methods used to ensure data integrity -

- Constraints - Constraints are rules or condition that mush be met for the data to be inserted,updated or deleted in a database table
- Transaction - A transaction is a sequence of one or more SQL operations that are treated as a single unit of work.
- Normalization - Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.


### Constraints in MYSQL -
1. NOT NULL - This constraint ensures that a column cannot have a NULL value. It requires that a value must be provided for the column when inserting or updating data.

```aiignore
CREATE TABLE users(
    id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    age INTEGER,
    city VARCHAR(255)
)
```
Here the id and name columns are defined with the NOT NULL constraint, which means that they cannot have NULL values. When inserting or updating data in the users table, you must provide a value for the id and name columns. If you try to insert a record without providing a value for these columns, it will result in an error.

---
2. UNIQUE -   This constraint ensures that all values in a column are unique. It prevents duplicate entries in the column.
```aiignore
CREATE TABLE users(
    id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    
    CONTRAINTS users_email_unique UNIQUE (email,name)
)
```
Here user name and email are defined with the UNIQUE constraint, which means that the combination of email and name must be unique across all records in the users table. This prevents duplicate entries for the same email and name combination.

---
3. PRIMARY KEY - This constraint uniquely identifies each record in a table. It is a combination of the NOT NULL and UNIQUE constraints. A table can have only one PRIMARY KEY, and it can consist of one or more columns. PRIMARY KEY is by default do NOT NULL and UNIQUE.
```aiignore
CREATE TABLE users(
    id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    
    CONTRAINTS users_email_unique UNIQUE (email,name)
    CONTRAINTS USER_PK PRIMARY KEY (id,name)
)
```
Here the id and name columns are defined as the PRIMARY KEY, which means that the combination of id and name must be unique across all records in the users table. This ensures that each record can be uniquely identified by its id and name combination. Additionally, since PRIMARY KEY is a combination of NOT NULL and UNIQUE, it also ensures that the id and name columns cannot have NULL values and must be unique.

---
4. Auto Increment - This constraint automatically generates a unique value for a column when a new record is inserted. It is often used with the PRIMARY KEY constraint to create a unique identifier for each record.
```aiignore
CREATE TABLE users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
```
Here the id column is defined with the AUTO_INCREMENT constraint, which means that it will automatically generate a unique value for each new record inserted into the users table. When a new record is inserted without specifying a value for the id column, the database will automatically assign the next available integer value to it. This is commonly used to create a unique identifier for each record in the table.

---
5. FOREIGN KEY - This constraint is used to establish a relationship between two tables. It ensures that the value in a column (or a set of columns) in one table matches the value in a column (or a set of columns) in another table. It helps maintain referential integrity between the tables.
```aiignore
CREATE TABLE orders(
    order_id INTEGER NOT NULL AUTO_INCREMENT,
    user_id INTEGER,
    product VARCHAR(255),
    
    CONSTRAINT orders_user_fk FOREIGN KEY (user_id) REFERENCES users(id)
)

```
Here the user_id column in the orders table is defined as a FOREIGN KEY that references the id column in the users table. This means that any value inserted into the user_id column of the orders table must match an existing value in the id column of the users table. This helps maintain referential integrity between the two tables, ensuring that each order is associated with a valid user.

---
6. Check  - This constraint is used to limit the values that can be inserted into a column. It allows you to specify a condition that must be met for the data to be accepted. For example, you can use a CHECK constraint to ensure that the age of a user is greater than 18.
```aiignore
CREATE TABLE users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INTEGER,
    
    CONSTRAINT user_age_check CHECK (age > 10 AND age < 30)
)
```
Here the age column in the users table is defined with a CHECK constraint that ensures the age value must be greater than 10 and less than 30. This means that any attempt to insert or update a record with an age value outside of this range will result in an error, ensuring that only valid age values are accepted in the users table.

---
7. DEFAULT - This constraint is used to provide a default value for a column when no value is specified during an insert operation. It ensures that a column will have a value even if the user does not provide one.``
```aiignore
CREATE TABLE users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INTEGER DEFAULT 18
)
```
Here the age column in the users table is defined with a DEFAULT constraint that sets the default value to 18. This means that if a new record is inserted into the users table without specifying a value for the age column, it will automatically be assigned the default value of 18. This ensures that the age column will always have a value, even if the user does not provide one during the insert operation.

---












