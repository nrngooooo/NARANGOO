select billid, foodname,deal 
from food f inner join zahialga z
on f.foodid=z.foodid
order by z.billid