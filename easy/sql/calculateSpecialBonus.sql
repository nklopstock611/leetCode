-- Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
-- Return the result table ordered by employee_id.
-- The query result format is in the following example.

-- Input: 
-- Employees table:
-- +-------------+---------+--------+
-- | employee_id | name    | salary |
-- +-------------+---------+--------+
-- | 2           | Meir    | 3000   |
-- | 3           | Michael | 3800   |
-- | 7           | Addilyn | 7400   |
-- | 8           | Juan    | 6100   |
-- | 9           | Kannon  | 7700   |
-- +-------------+---------+--------+
-- Output: 
-- +-------------+-------+
-- | employee_id | bonus |
-- +-------------+-------+
-- | 2           | 0     |
-- | 3           | 0     |
-- | 7           | 7400  |
-- | 8           | 0     |
-- | 9           | 7700  |
-- +-------------+-------+

-- mi solución:
with zero as
(
    select employee_id, name, 0 as bonus
    from employees
    where employee_id % 2 = 0 OR SUBSTRING(name, 1, 1) = "M"
),
nbonus as
(
    select employee_id, name, salary as bonus
    from employees
    where employee_id % 2 = 1 and SUBSTRING(name, 1, 1) != "M"
)

select employee_id, bonus
from zero
UNION
select employee_id, bonus
from nbonus
order by employee_id;

-- solución con IF!
select employee_id, IIF(employee_id % 2 <> 0 AND SUBSTRING(name, 1, 1) <> "M", salary, 0) as bonus
-- if employee_id es impar Y el primer caracter del nombre es "M", entonces salary cambia a 0.
from employees
order by employee_id;