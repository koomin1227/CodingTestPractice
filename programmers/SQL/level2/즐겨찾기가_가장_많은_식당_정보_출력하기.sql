-- 코드를 입력하세요
select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES from REST_INFO r
    where FAVORITES = (select max(FAVORITES) from REST_INFO where FOOD_TYPE = r.FOOD_TYPE)
    order by FOOD_TYPE desc