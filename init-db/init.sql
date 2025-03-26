CREATE TABLE users (
    uid SERIAL PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    emailid VARCHAR(100),
    mobile VARCHAR(20)
);

INSERT INTO users (uid,username,password,emailid,mobile) VALUES
(1,'Divya','divyapwd','divya@gmail.com','8888888888'),
(2,'kavya','kavyapwd','kavya@gmail.com','9999999999');

CREATE TABLE my_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO my_table (name) VALUES
('John Doe'),
('Jane Smith');


