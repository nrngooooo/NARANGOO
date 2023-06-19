select news_id, catid, subcategory, subcatname, userid, ognoo 
from news n inner join subcategory s 
on n.subcategory=s.subcatid