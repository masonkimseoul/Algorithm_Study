-- 코드를 입력하세요
SELECT NAME, count(*) as COUNT from ANIMAL_INS 
where NAME is Not NULL 
group by NAME having COUNT >=2 
order by NAME ASC;