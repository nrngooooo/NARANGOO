select title, contents, fullname, catname, subcatname,ognoo
from news n 
inner join category cat 
on n.category=cat.catid
inner join subcategory s
on n.subcategory=s.subcatid
inner join users u
on n.userid=u.userid