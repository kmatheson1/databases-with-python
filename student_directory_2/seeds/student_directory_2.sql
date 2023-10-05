DROP TABLE IF EXISTS cohorts CASCADE;
DROP SEQUENCE IF EXISTS cohorts_id_seq;
DROP TABLE IF EXISTS students CASCADE;
DROP SEQUENCE IF EXISTS students_id_seq;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);


INSERT INTO cohorts (name, starting_date) VALUES ('RA', '04/09/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('R1', '03/06/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('R2', '02/04/2023');
INSERT INTO cohorts (name, starting_date) VALUES ('R3', '06/09/2023');

INSERT INTO students (name, cohort_id) VALUES ('Jake', 2);
INSERT INTO students (name, cohort_id) VALUES ('Kate', 2);
INSERT INTO students (name, cohort_id) VALUES ('Kieran', 1);
INSERT INTO students (name, cohort_id) VALUES ('Jason', 3);
INSERT INTO students (name, cohort_id) VALUES ('Ellen', 3);
INSERT INTO students (name, cohort_id) VALUES ('Bob', 4);