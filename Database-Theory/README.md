# SQL, SQLAlchemy, SQLlite

It is super common knowledge that we use SQL with accesing and storing data in databases. There are some extremely common foundational commands:

## SELECT

> NOTE]
>
> Here is a standard exmaple of `SELECT`  in SQL:
>
> ```sql
> SELECT username, email
> FROM users
> WHERE age >= 21;
> ```
>
> - `SELECT` requests columns
> - `FROM` requests the table
> - `WHERE` filters the records

## INSERT

> Here is a standard exmaple of `INSERT`  in SQL:
>
> ```sql
> INSERT INTO users (username, email,	age)
> VALUES ('Jordan', 'jordan@example.com', 23);
> ```
>
> - `INSERT INTO` specifies which table we are inserting in, as well as the columns
> - `VALUES` contains the respective column's data

## UPDATE

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
