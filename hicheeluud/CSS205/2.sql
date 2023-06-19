select s.catid,catname,subcatid,subcatname 
from category cat inner join subcategory s
on cat.catid=s.catid