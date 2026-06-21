-- 1 Employee count by department
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

-- 2 Average salary by department
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

-- 3 Highest paid employees
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 10;

-- 4 Best performers
SELECT *
FROM employees
ORDER BY performance_score DESC
LIMIT 10;

-- 5 Total sales by employee
SELECT employee_id,
       SUM(sale_amount) AS total_sales
FROM sales
GROUP BY employee_id
ORDER BY total_sales DESC;

-- 6 Top 10 sales performers
SELECT employee_id,
       SUM(sale_amount) AS total_sales
FROM sales
GROUP BY employee_id
ORDER BY total_sales DESC
LIMIT 10;

-- 7 Average sale amount
SELECT AVG(sale_amount)
FROM sales;

-- 8 Total sales company wide
SELECT SUM(sale_amount)
FROM sales;

-- 9 Sales transaction count
SELECT COUNT(*)
FROM sales;

-- 10 Employee count
SELECT COUNT(*)
FROM employees;