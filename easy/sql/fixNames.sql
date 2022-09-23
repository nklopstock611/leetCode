-- Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.
-- Return the result table ordered by user_id.
-- The query result format is in the following example.

-- Input: 
-- Users table:
-- +---------+-------+
-- | user_id | name  |
-- +---------+-------+
-- | 1       | aLice |
-- | 2       | bOB   |
-- +---------+-------+
-- Output: 
-- +---------+-------+
-- | user_id | name  |
-- +---------+-------+
-- | 1       | Alice |
-- | 2       | Bob   |
-- +---------+-------+

with min as (
  select user_id, LOWER(name) as nname
  from users
)

SELECT user_id,
CASE
	WHEN nname is not NULL THEN CONCAT(UPPER(SUBSTRING(nname, 1, 1)), RIGHT(nname, LENGTH(nname) - 1))
    -- RIGHT retorna el string que se pasa como primer parámetro desde última posición hasta la que se pasa como segundo parámetro
    -- también existe LEFT, que es lo mismo pero al revés.
    -- también se podría usar SUBSTRING(nname, 2, LENGTH(nname) - 1) para obtener el string desde la segunda posición hasta la última.
    else nname
END as name
from min
order by user_id asc;