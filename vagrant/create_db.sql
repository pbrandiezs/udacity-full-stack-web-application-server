
-- Program: create_db.sql
--
-- This program will initialize the database with an articles table.
--
-- Author: Perry Brandiezs
--
-- Created: May 10, 2019


CREATE TABLE articles (
    id integer NOT NULL,
    body text
);

ALTER TABLE articles OWNER TO "www-data";

COPY articles (id, body) FROM stdin;
1	Hello World, it's a great day
2	Gooday world!
\.
