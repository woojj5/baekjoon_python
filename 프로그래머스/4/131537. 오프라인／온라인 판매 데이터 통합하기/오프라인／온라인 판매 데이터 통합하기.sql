-- 코드를 입력하세요
    select date_format(sales_date, "%Y-%m-%d") as SALES_DATE, 
    PRODUCT_ID,
    USER_ID,
    SALES_AMOUNT
    FROM ONLINE_SALE 
    where month(SALES_DATE) = 3
union
    select date_format(sales_date, "%Y-%m-%d") as SALES_DATE, 
    PRODUCT_ID,
    NULL as USER_ID,
    SALES_AMOUNT
    FROM OFFLINE_SALE  
    where month(SALES_DATE) = 3
order by sales_date asc, PRODUCT_ID asc,USER_ID asc,SALES_AMOUNT asc