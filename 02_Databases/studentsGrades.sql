DROP TABLE GRADES;
DROP TABLE STUDENTS;

PRAGMA foreign_keys = ON;

CREATE TABLE STUDENTS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20) NOT NULL,
  phone VARCHAR(8) 
);

-- Normally you would let the DB create the keys. I set them here
-- to give better examples in the lecture.
-- INSERT INTO STUDENTS (name,phone) values ('Chris','1234');
-- INSERT INTO STUDENTS (name,phone) values ('Ann','9999');
-- INSERT INTO STUDENTS (name,phone) values ('Pat','0110');

INSERT INTO STUDENTS (id,name,phone) values (20,'Chris','1234');
INSERT INTO STUDENTS (id,name,phone) values (17,'Ann','9999');
INSERT INTO STUDENTS (id,name,phone) values (35,'Pat','0110');

select * from students;

CREATE TABLE GRADES (
  student INT NOT NULL,
  grade INT NOT NULL,
  FOREIGN KEY(student) REFERENCES STUDENTS(id)  
);

INSERT INTO GRADES (student,grade) values (20,90);  
INSERT INTO GRADES (student,grade) values (17,85);
INSERT INTO GRADES (student,grade) values (35,97);  

select * from grades;

select * from students,grades where students.id = grades.student

