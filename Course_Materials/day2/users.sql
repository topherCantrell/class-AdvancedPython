-- SQL Command Line

DROP TABLE USERS;

CREATE TABLE USERS (
  name VARCHAR(20), 
  pass VARCHAR(20)        
);

INSERT INTO USERS values ('Admin', 'secret');
INSERT INTO USERS values ('Chris', 'topher');
INSERT INTO USERS values ('Pat',   '12345');

select * from grades;

select * from users where name='Admin' AND pass='jj'

select * from users where name='Admin' AND pass='secret'

select * from users where name='Admin' AND pass='' OR ''='' --'

