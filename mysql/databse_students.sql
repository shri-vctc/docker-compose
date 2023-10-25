use db;

CREATE TABLE students(
    StudentID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    LastName varchar(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students(FirstName, LastName)
VALUES("Rahul", "Sharma"), ("Sonam", "Verma");  