# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._


## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```
```
Nouns:

student, name, cohort
```


## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record   |     Properties      |
| -------  | ------------------- |
|  student | name, cohort        |

Name of the table (always plural): `students`

Column names: `name`, `cohort`


## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```markdown
# EXAMPLE:

id: SERIAL
name: text
cohort: text

```

## 4. Write the SQL

```sql

-- EXAMPLE
-- file: students_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  name text,
  cohort text
);

```

## 5. Create the Table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```