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


2. UNIQUE -   This constraint ensures that all values in a column are unique. It prevents duplicate entries in the column.
3. PRIMARY KEY - This constraint uniquely identifies each record in a table. It is a combination
4. Auto Increment - This constraint automatically generates a unique value for a column when a new record is inserted. It is often used with the PRIMARY KEY constraint to create a unique identifier for each record.
5. FOREIGN KEY - This constraint is used to establish a relationship between two tables. It ensures
6. Check  - This constraint is used to limit the values that can be inserted into a column. It allows you to specify a condition that must be met for the data to be accepted.
7. DEFAULT - This constraint is used to provide a default value for a column when no value is specified during an insert operation. It ensures that a column will have a value even if the user does not provide one.``
















