-- 코드를 작성해주세요
select f.ITEM_ID, f.ITEM_NAME, f.RARITY from ITEM_INFO f
    join ITEM_TREE t
    on f.ITEM_ID = t.ITEM_ID
    where f.ITEM_ID not in (select distinct PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not NULL)
    order by f.ITEM_ID desc;