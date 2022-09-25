-- Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Input: 
-- Products table:
-- +------------+--------+--------+--------+
-- | product_id | store1 | store2 | store3 |
-- +------------+--------+--------+--------+
-- | 0          | 95     | 100    | 105    |
-- | 1          | 70     | null   | 80     |
-- +------------+--------+--------+--------+
-- Output: 
-- +------------+--------+-------+
-- | product_id | store  | price |
-- +------------+--------+-------+
-- | 0          | store1 | 95    |
-- | 0          | store2 | 100   |
-- | 0          | store3 | 105   |
-- | 1          | store1 | 70    |
-- | 1          | store3 | 80    |
-- +------------+--------+-------+

with st1 as (
  select product_id, 'store1' as store, store1 as price
  from products
  where store1 is not null
),
st2 as (
  select product_id, 'store2' as store, store2 as price
  from products
  where store2 is not null
),
st3 as (
  select product_id, 'store3' as store, store3 as price
  from products
  where store3 is not null
)

select *
from st1
UNION
select *
from st2
UNION
select *
from st3;