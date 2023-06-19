select foodname, price, z.billid, wname
from food f 
inner join zahialga z
on f.foodid=z.foodid
inner join debt d
on d.billid=z.billid
inner join worker w
on w.wid=d.wid
where z.billid='20121024/001'
