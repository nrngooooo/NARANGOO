select news_id, n.userid, "password", email, fullname, ognoo 
from news n inner join users u
on n.userid=u.userid