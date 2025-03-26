-- 코드를 작성해주세요
select s3.ID
from ECOLI_DATA as s1
join ECOLI_DATA as s2 on s1.id = s2.parent_id
join ECOLI_DATA as s3 on s2.id = s3.parent_id
where s1.parent_id is NULL
order by s3.id
