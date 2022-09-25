-- Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.
-- The query result format is in the following example.

-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- mi solución:
with biggest as (
  select MAX(salary) as biggestval
  from employee
)

select MAX(salary) as secondHighestSalary
from employee
where salary not in (
  select *
  from biggest
);

-- solución más "elegante" (que al final es exactamente igual):
select MAX(salary) as secondHighestSalary
from employee
where salary not in (
    select MAX(salary)
    from employee
);