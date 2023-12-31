
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments CASCADE;
DROP SEQUENCE IF EXISTS comments_id_seq;


CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id serial PRIMARY key,
    name text,
    contents text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id serial PRIMARY key,
    name text,
    contents text,
    post_id int,
    constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);

INSERT INTO posts (name, contents) VALUES ('James', 'Hello World');
INSERT INTO posts (name, contents) VALUES ('John', 'Hello World!');
INSERT INTO posts (name, contents) VALUES ('Lewis', 'Goodbye');
INSERT INTO posts (name, contents) VALUES ('Josh', 'Welcome');

INSERT INTO comments (name, contents, post_id) VALUES ('Kieran', 'Hello', 1);
INSERT INTO comments (name, contents, post_id) VALUES ('Jane', 'Nice', 1);
INSERT INTO comments (name, contents, post_id) VALUES ('Hannah', 'Okay', 2);
INSERT INTO comments (name, contents, post_id) VALUES ('Alana', 'Not Okay', 2);
