select bname, dprice
from branch b 
inner join worker w 
on b.bid=w.bid
inner join debt d
on w.wid=d.wid
where wname='Баатархүү'