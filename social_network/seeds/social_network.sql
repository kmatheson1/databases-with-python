-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    contents text,
    views int,
    user_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (email_address, username) VALUES ('boomzilla@aol.com', 'capacity');
INSERT INTO users (email_address, username) VALUES ('microfab@gmail.com', 'skirt');
INSERT INTO users (email_address, username) VALUES ('ilikered@mac.com', 'hefty');
INSERT INTO users (email_address, username) VALUES ('schumer@mac.com', 'bob');
INSERT INTO users (email_address, username) VALUES ('podmaster@live.com', 'ladder');
INSERT INTO users (email_address, username) VALUES ('smartfart@hotmail.com', 'delight');

INSERT INTO posts (title, contents, views, user_id) VALUES ('Man Of The East', 'test post content 1', 100, 1);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Invader Of Rainbows', 'test post content 2', 50, 1);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Spiders Of Time', 'test post content 3', 20, 2);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Cats Of Utopia', 'test post content 4', 20, 3);
INSERT INTO posts (title, contents, views, user_id) VALUEs ('Butchers And Priests', 'test post content 5', 10, 3);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Kings And Criminals', 'test post content 6', 100, 3);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Extinction Of The Gods', 'test post content 7', 50, 4);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Disruption With Vigor', 'test post content 8', 20, 5);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Leading The Hunter', 'test post content 9', 20, 5);
INSERT INTO posts (title, contents, views, user_id) VALUES ('Traces In The Graveyard', 'test post content 10', 20, 6);
