-- 코드를 작성해주세요
with RECURSIVE ECOLI_GENERATIONS AS(
    select id, parent_id, 1 as GENERATION
    from ECOLI_DATA 
    where parent_id is NULL
    union all
    select E.id,E.parent_id, G.GENERATION+1 as GENERATION
    from ECOLI_DATA E
    join ECOLI_GENERATIONS G ON G.ID = E.PARENT_ID
)
select count(g.id) as count, g.GENERATION
from ECOLI_GENERATIONS as g
WHERE NOT EXISTS (
    SELECT 1 
    FROM ECOLI_DATA child 
    WHERE child.PARENT_ID = g.ID
)
group by GENERATION
order by GENERATION asc