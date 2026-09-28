-- Employee name + department name
SELECT e.name, d.name AS department
FROM employees as e
join departments as d
on e.department_id = d.id
