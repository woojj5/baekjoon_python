-- 코드를 작성해주세요
Select B.ITEM_ID, A.ITEM_NAME, A.RARITY from  ITEM_INFO A
left join ITEM_TREE B on A.ITEM_ID = B.ITEM_ID
where B.PARENT_ITEM_ID in (select ITEM_ID from ITEM_INFO where rarity = 'RARE') order by B.ITEM_ID desc