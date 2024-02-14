DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;


CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  email text,
  username text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
-- The foreign key name is always {other_table_singular}_id
  account_id int,
  constraint fk_account foreign key(account_id)
    references accounts(id)
    on delete cascade
);

-- Seed the table with data 
-- accounts first

INSERT INTO accounts
(email, username)
values('pato@patomail.com', 'pato2000');

INSERT INTO accounts
(email, username)
values('cao@dogmail.com', 'doggydog');

INSERT INTO accounts
(email, username)
values('cat@catmail.com', 'tac');

-- posts second

INSERT INTO posts
(title, content, views, account_id)
values('Ducktales', 'Story of my life, quack quack quack..', 500, 1);

INSERT INTO posts
(title, content, views, account_id)
values('Dog Life', 'Say it, bow-wow-wow, Uh, uh, Bow Wow (yeah)', 12, 2);

INSERT INTO posts
(title, content, views, account_id)
values('Dog Life VOL.2', 'Still waters run deep / Still Snoop Dogg and D.R.E.', 122, 2);

INSERT INTO posts
(title, content, views, account_id)
values('Meow', 'Meow, meow, meow', 200, 3);


