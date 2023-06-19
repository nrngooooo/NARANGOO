select fullname, news_id, title, contents, catname 
from users u 
inner join news as n
on n.userid=u.userid
inner join category cat 
on cat.catid=n.category

select title , subcatname, fullname 
from news j
inner join users s
on j.userid= s.userid inner join subcategory d
on j.subcategory= d.subcatid
