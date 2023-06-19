select wname, billid, dprice
from worker w inner join debt d
on w.wid=d.wid