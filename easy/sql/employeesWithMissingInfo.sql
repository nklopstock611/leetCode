-- Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:
-- The employee's name is missing, or
-- The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.
-- The query result format is in the following example.

-- Input: 
-- Employees table:
-- +-------------+----------+
-- | employee_id | name     |
-- +-------------+----------+
-- | 2           | Crew     |
-- | 4           | Haven    |
-- | 5           | Kristian |
-- +-------------+----------+
-- Salaries table:
-- +-------------+--------+
-- | employee_id | salary |
-- +-------------+--------+
-- | 5           | 76071  |
-- | 1           | 22517  |
-- | 4           | 63539  |
-- +-------------+--------+
-- Output: 
-- +-------------+
-- | employee_id |
-- +-------------+
-- | 1           |
-- | 2           |
-- +-------------+

with noSalary as (
    select employee_id
    from employees
    where employee_id not in (
        select employee_id
        from salaries
    )    
),
noName as (
    select employee_id
    from salaries
    where employee_id not in (
        select employee_id
        from employees
    )
)

select *
from noSalary
union
select *
from noName
order by employee_id asc;