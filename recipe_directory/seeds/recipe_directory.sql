-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    avg_cooking_time_mins INT,
    rating INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (title, avg_cooking_time_mins, rating) VALUES ('Carbonara', 30, 4);
INSERT INTO recipes (title, avg_cooking_time_mins, rating) VALUES ('Pizza', 60, 5);
INSERT INTO recipes (title, avg_cooking_time_mins, rating) VALUES ('Noodles', 20, 4);
INSERT INTO recipes (title, avg_cooking_time_mins, rating) VALUES ('Baked Beans', 5, 1);
INSERT INTO recipes (title, avg_cooking_time_mins, rating) VALUES ('Salad', 15, 3);
INSERT INTO recipes (title, avg_cooking_time_mins, rating) VALUES ('Sandwich', 5, 3);
