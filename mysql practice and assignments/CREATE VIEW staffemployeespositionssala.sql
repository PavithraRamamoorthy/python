CREATE VIEW staffemployeespositionssalary
AS 

SELECT staff.id, employees.first_name, employees.last_name, positions.position, salary.salary
FROM staff
JOIN employees 
ON employees.id = staff.first_name

JOIN positions 
ON positions.id = staff.position

JOIN salary 
ON salary.id = staff.salary
WHERE salary.salary>25000
ORDER BY staff.salary DESC;

select * from staffemployeespositionssalary;