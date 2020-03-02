-- SQL Command Line

DROP TABLE GRADES;

CREATE TABLE GRADES (
  name VARCHAR(20), 
  grade INT        
);

INSERT INTO GRADES values ('Chris',90);
INSERT INTO GRADES values ('Ann',85);
INSERT INTO GRADES values ('Pat',97);

select * from grades;

select * from grades where name='Chris';

UPDATE GRADES 
  SET grade=95 
  WHERE name='Chris'; 
  
UPDATE GRADES 
  SET grade=100;
  
-- SQL Basics

DROP TABLE GRADES;
CREATE TABLE GRADES (
  name VARCHAR(20), 
  grade INT        
);
INSERT INTO GRADES values ('Chris',90);
INSERT INTO GRADES values ('Ann',85);
INSERT INTO GRADES values ('Pat',97);

-- STUDENTS Table

DROP TABLE students;

CREATE TABLE STUDENTS (
  name VARCHAR(20),
  phone VARCHAR(8)
);

INSERT INTO STUDENTS values ('Chris','1234');
INSERT INTO STUDENTS values ('Ann','9999');
INSERT INTO STUDENTS values ('Pat','0110');

SELECT * FROM STUDENTS;

-- Joins

SELECT * FROM GRADES, STUDENTS;

SELECT * FROM GRADES, STUDENTS
 WHERE GRADES.name = STUDENTS.name;
 
SELECT GRADES.grade, GRADES.name, STUDENTS.phone 
  FROM GRADES, STUDENTS
  WHERE GRADES.name = STUDENTS.name;

SELECT GRADES.grade, GRADES.name, STUDENTS.phone 
  FROM GRADES, STUDENTS
  WHERE GRADES.name = STUDENTS.name 
  ORDER BY GRADES.name DESC;

-- Generated Primary Keys
  
DROP TABLE STUDENTS;

CREATE TABLE STUDENTS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20) NOT NULL,
  phone VARCHAR(8) 
);

INSERT INTO STUDENTS (name,phone) values ('Chris','1234');
INSERT INTO STUDENTS (name,phone) values ('Ann','9999');
INSERT INTO STUDENTS (name,phone) values ('Pat','0110');

SELECT * FROM STUDENTS;

-- Foreign Keys

PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;

DROP TABLE GRADES;

CREATE TABLE GRADES (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  
  name INT NOT NULL,
  grade INT NOT NULL,
  FOREIGN KEY(name) REFERENCES STUDENTS(id)  
);

INSERT INTO GRADES (name,grade) values (1,90);  
INSERT INTO GRADES (name,grade) values (2,85);

select * from grades;
select * from STUDENTS;

INSERT INTO GRADES (name,grade) values (null,75);
INSERT INTO GRADES (name,grade) values (123,75);

-- Other constraints

DROP TABLE GRADES;

CREATE TABLE GRADES (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  
  name INT NOT NULL,
  grade INT NOT NULL CHECK (grade>=0),
  FOREIGN KEY(name) REFERENCES STUDENTS(id)  
);

INSERT INTO GRADES (name,grade) values (1,-15);

-- For next lecture

DROP TABLE GRADES;
DROP TABLE STUDENTS;

CREATE TABLE STUDENTS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20) NOT NULL,
  phone VARCHAR(8) 
);

INSERT INTO STUDENTS (name,phone) values ('Chris','1234');
INSERT INTO STUDENTS (name,phone) values ('Ann','9999');
INSERT INTO STUDENTS (name,phone) values ('Pat','0110');

CREATE TABLE GRADES (
  id INTEGER PRIMARY KEY AUTOINCREMENT,  
  name INT NOT NULL,
  grade INT NOT NULL,
  FOREIGN KEY(name) REFERENCES STUDENTS(id)  
);

INSERT INTO GRADES (name,grade) values (1,90);  
INSERT INTO GRADES (name,grade) values (2,85);
INSERT INTO GRADES (name,grade) values (3,97);  
