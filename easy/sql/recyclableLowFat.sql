-- Write an SQL query to find the ids of products that are both low fat and recyclable.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Input: 
-- Products table:
-- +-------------+----------+------------+
-- | product_id  | low_fats | recyclable |
-- +-------------+----------+------------+
-- | 0           | Y        | N          |
-- | 1           | Y        | Y          |
-- | 2           | N        | Y          |
-- | 3           | Y        | Y          |
-- | 4           | N        | N          |
-- +-------------+----------+------------+
-- Output: 
-- +-------------+
-- | product_id  |
-- +-------------+
-- | 1           |
-- | 3           |
-- +-------------+

select product_id
from products
where low_fats = "Y" and recyclable = "Y";