-- 코드를 작성해주세요
select A.ID,
CASE
when A.per <= 0.25 then 'CRITICAL'
when A.per <= 0.5  then 'HIGH'
when A.per <= 0.75  then 'MEDIUM'
else 'LOW'
end as COLONY_NAME
from (select id, percent_rank() over (order by SIZE_OF_COLONY desc) as per from ECOLI_DATA) as A
order by A.ID