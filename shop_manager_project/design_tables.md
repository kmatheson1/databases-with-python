## Two Table (Many-to-Many) Desingn Recipe Template

*Copy this recipe template to design and create two related database tables having a Many-to-Many relationship.*

## 1. Extract nouns from the user stories or specification

```markdown
# USER STORIES:

As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.
```
```
Nouns:
items, name, unit_price, quantity
orders, customer_name, date

Verbs:
create new items
create new order
find order with items

```

## 2. Infer the Table Name and Columns

| Record     |       Properties                  |
| ---------  | --------------------------------- |
|  items     |    name, unit_price, quantity     |
| orders     |    customer_name, date_ordered    |

    1. Name of the first table (always plural): `items`
        
        Column names: `name`, `unit_price`, `quantity`
        
    2. Name of the second table (always plural): `orders`
        
        Column names: `customer_name`, `date_ordered`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: items
id: SERIAL
name: text
unit_price: float
quantity: int

Table: orders
id: SERIAL
customer_name: text
date_ordered: date
```

## 4. Design the Many-to-Many relationship

```markdown
# EXAMPLE

1. Can one item have many orders? YES
2. Can one order have many items? YES

```

## 5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `items_orders`.

```markdown
# EXAMPLE

Join table for tables: items and orders
Join table name: items_orders
Columns: item_id, order_id

```

## 6. Write the SQL.

```sql
-- EXAMPLE
-- file: posts_tags.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  unit_price float,
  quantity int
);

-- Create the second table.
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  cutomer_name text,
  date_ordered date
);

-- Create the join table.
CREATE TABLE items_orders (
  item_id int,
  order_id int,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

```

## 7. Create the tables.

```bash
psql -h 127.0.0.1 shop_directory < items_orders.sql
```