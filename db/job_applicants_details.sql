CREATE DATABASE job_applicants_details;

show databases;

USE job_applicants_details;

CREATE TABLE IF NOT EXISTS details2 (
  Name varchar(50),
  Notice_period INT,
  Current_annual_Salary DECIMAL(10,2),
  Expected_annual_Salary DECIMAL(10,2),
  Relocation_acceptance ENUM('Yes', 'No')
);


INSERT INTO details2 (Name,Notice_period, Current_annual_Salary, Expected_annual_Salary, Relocation_acceptance)
VALUES
  ('akash',30, 50000.00, 60000.00, 'Yes'),
  ('sheel',60, 70000.00, 75000.00, 'No'),
  ('viswa',15, 45000.00, 55000.00, 'Yes'),
  ('jay',45, 60000.00, 65000.00, 'Yes');
  
select * from details;
truncate details