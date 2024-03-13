SELECT b.CATEGORY, sum(s.SALES) as TOTAL_SALES from BOOK b
    join BOOK_SALES s
    on b.BOOK_ID = s.BOOK_ID
    where year(s.SALES_DATE) = 2022
    and month(s.SALES_DATE) = 1
    group by CATEGORY
    order by b.CATEGORY;