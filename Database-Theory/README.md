# SQL, SQLAlchemy, SQLlite

> [!NOTE]
>
> A lot of this content is very simple and serves more as a reminder. 

It is super common knowledge that we use SQL with accesing and storing data in databases. There are some extremely common foundational commands:

## SQL CRUD 

### SELECT

> Here is a standard exmaple of `SELECT`  in SQL:
>
> ```sql
>SELECT username, email
> FROM users
> WHERE age >= 21;
> ```
> 
> - `SELECT` requests columns
>- `FROM` requests the table
> - `WHERE` filters the records

### INSERT

> Here is a standard exmaple of `INSERT`  in SQL:
>
> ```sql
> INSERT INTO users (username, email,	age)
> VALUES ('Jordan', 'jordan@example.com', 23);
> ```
>
> - `INSERT INTO` specifies which table we are inserting in, as well as the columns
> - `VALUES` contains the respective column's data

### UPDATE

> Here is a standard exmaple of `UPDATE`  in SQL:
>
> ```sql
> UPDATE users
> SET email = 'jordan2026@example.com'
> WHERE username = 'Jordan';
> ```
>
> - `UPDATE` specifies the table
> - `SET` specifies the change
> - `WHERE` specify which user

### Delete

> Here is a standard exmaple of `DELETE`  in SQL:
>
> ```sql
> DELETE FROM users 
> WHERE username = 'jordan';
> ```
>
> - `DELETE FROM` specifies to delete from this table
> - `WHERE` specify which user

## Keys

### Primary Keys (PK)

A primary key uniquely identifies a records in a table. 

- Cannot be `NULL`
- Cannot have duplicates

- Most often, are IDs.

> [!NOTE]
>
>  Even thoguh usernames may be unique, usernames can change. 

### Foreign Keys (FK)

A coloumn in one table that references to the primary key in different table. 

They:

- Establish relationships
- Connect related records
- Maintain referential integretity (Prevents references to records that dont exist)

## JOINs

A JOIN combines records from two or more tables based on a related column, usually a **Primary Key (PK)** and **Foreign Key (FK)**.

### INNER JOIN

Returns only records where there is a matching value in both tables.

```sql
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.id = courses.student_id;
```

- `SELECT` specifies which columns to retrieve.
- `FROM` specifies the main (left) table.
- `INNER JOIN` specifies the table to combine with the main table. Only matching records are returned.
- `ON` specifies the condition used to match records between the tables.

### LEFT JOIN

Returns **ALL records from the left table**, including records without a match in the right table. Where no match exists, the right table's columns contain `NULL`.

```sql
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses
ON students.id = courses.student_id;
```

### RIGHT JOIN

Returns **ALL records from the right table**, including records without a match in the left table. Where no match exists, the left table's columns contain `NULL`.

```sql
SELECT students.name, courses.course_name
FROM students
RIGHT JOIN courses
ON students.id = courses.student_id;
```

### Understanding LEFT vs RIGHT

The position of the tables determines which one is preserved:

- **LEFT JOIN:** Keeps every record from the table after `FROM`
- **RIGHT JOIN:** Keeps every record from the table after `JOIN`

## Creating Tables

### CREATE

> Here is a standard example of creating a table
>
> ```sql
> CREATE TABLE users {
> 	id INTEGER PRIMARY KEY,
> 	username TEXT NOT NULL,
> 	email TEXT UNIQUE,
> 	age INTEGER
> };
> ```
>
> 
>
> Here we could create the posts table like:
>
> ```sql
> CREATE TABLE posts {
> 	id INTEGER PRIMARY KEY,
> 	title TEXT NOT NULL,
> 	content TEXT NOT NULL,
> 	user_id INTEGER 
> 	FOREIGN KEY (user_id) REFERENCES uesrs(id)
> };
> ```
>
> 
