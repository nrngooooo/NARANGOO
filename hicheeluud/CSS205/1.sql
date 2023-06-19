select news_id, title, catid, catname, subcategory, userid, ognoo 
from news n inner join category cat 
on n.category= cat.catid