select news_id, title, contents, catname
from news n
inner join category cat 
on n.category=cat.catid 
where ognoo='2020-04-22'