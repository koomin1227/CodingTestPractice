# -- 코드를 입력하세요
SELECT month(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where CAR_ID in 
    (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where START_DATE between '2022-08-01' and '2022-10-31'
        group by CAR_ID
        having count(*) >= 5
    ) and START_DATE between '2022-08-01' and '2022-10-31'
    group by month(START_DATE), CAR_ID
    order by month(START_DATE), CAR_ID desc;