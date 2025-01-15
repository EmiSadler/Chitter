DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;

CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    content VARCHAR(255),
    date_only DATE DEFAULT CURRENT_DATE,  -- Only stores date (YYYY-MM-DD)
    time_only TIME(0) DEFAULT CURRENT_TIME, -- Only stores time (HH:MM)
    users_id int
);



