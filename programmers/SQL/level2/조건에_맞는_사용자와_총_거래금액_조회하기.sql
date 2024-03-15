-- 코드를 입력하세요
select u.USER_ID, u.NICKNAME, sum(b.PRICE) as TOTAL_SALES from USED_GOODS_BOARD b
    join USED_GOODS_USER u
    on b.WRITER_ID = u.USER_ID
    where b.STATUS = 'DONE'
    group by b.WRITER_ID
    having TOTAL_SALES >= 700000
    order by TOTAL_SALES