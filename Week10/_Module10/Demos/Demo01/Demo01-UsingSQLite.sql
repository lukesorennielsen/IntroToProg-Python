
-- Drop the table as needed
-- DROP TABLE Students

-- Create a table for student data
CREATE TABLE Students (-- The first column is added as an identifier
    StudentID INTEGER PRIMARY KEY,  -- INTEGER PRIMARY KEY makes it auto-incrementing.(Not INT PRIMARY KEY)
    StudentFirstName TEXT,  -- Text or VarChar are a close match for string
    StudentLastName TEXT,
    StudentGPA REAL  -- Real is a close match for float
);


-- We use this command to write data to a table
INSERT INTO Students (StudentFirstName, StudentLastName, StudentGPA)
VALUES ('Vic', 'Vu', 3.85); -- The StudentID will automatically increment


-- We use this command to read data from a table
SELECT StudentID, StudentFirstName, StudentLastName, StudentGPA
FROM Students;


-- To change data in a table we use this command
UPDATE Students
SET StudentFirstName = 'Vic', StudentLastName = 'Vu', StudentGPA = 4.0
WHERE StudentID = 1;

SELECT StudentID, StudentFirstName, StudentLastName, StudentGPA
FROM Students;


-- Let's add another row and remove it with the DELETE command
INSERT INTO Students (StudentFirstName, StudentLastName, StudentGPA)
VALUES ('Test', 'Delete', 1.0);

SELECT StudentID, StudentFirstName, StudentLastName, StudentGPA
FROM Students;


-- Then use this command remove data from a table
DELETE FROM Students WHERE StudentID = 2;

SELECT StudentID, StudentFirstName, StudentLastName, StudentGPA
FROM Students;
