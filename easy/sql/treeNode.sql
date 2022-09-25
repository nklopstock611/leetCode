-- Each node in the tree can be one of three types:
-- "Leaf": if the node is a leaf node.
-- "Root": if the node is the root of the tree.
-- "Inner": If the node is neither a leaf node nor a root node.
-- Write an SQL query to report the type of each node in the tree.
-- Return the result table ordered by id in ascending order.
-- The query result format is in the following example.

--         1
--       /   \
--      2     3
--     / \ 
--    4   5

-- Input: 
-- Tree table:
-- +----+------+
-- | id | p_id |
-- +----+------+
-- | 1  | null |
-- | 2  | 1    |
-- | 3  | 1    |
-- | 4  | 2    |
-- | 5  | 2    |
-- +----+------+
-- Output: 
-- +----+-------+
-- | id | type  |
-- +----+-------+
-- | 1  | Root  |
-- | 2  | Inner |
-- | 3  | Leaf  |
-- | 4  | Leaf  |
-- | 5  | Leaf  |
-- +----+-------+

with root as (
  select tree.id, 'Root' as type
  from tree
  where p_id is null
),

inners as (
  select tree.id, 'Inner' as type
  from tree
  where tree.id in ( -- el id del nodo está en la columna de padres (es decir, tiene hijos)
    SELECT p_id
    from tree
  )
  AND
  tree.id not in ( -- no es raíz.
    select id
    from root
  )
),

leafs as (
  select tree.id, 'Leaf' as type
  from tree
  where id not in ( -- no tiene hijos.
    select id
    from inners
    where id not in ( -- no eso no es raíz.
      select id
      from root
  	)
  )
  AND
  tree.id not in (
    select id
    from root
  )
)

select *
from root
UNION
select *
from inners
UNION
select *
from leafs;