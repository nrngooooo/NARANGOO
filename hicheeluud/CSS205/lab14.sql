select wlast, wname,regdug,email,depname
from worker w inner join department d
on w.depcode=d.depcode

select worker.*, profession.proname
from worker inner join profession 
on worker.procode=profession.procode

select wlast, wname, regdug, phone, proname,depname
from worker inner join profession 
on worker.procode=profession.procode
inner join department 
on worker.depcode=department.depcode
where wcode='AC1'

select worker.*, profession.proname,depname
from worker inner join profession 
on worker.procode=profession.procode
inner join department 
on worker.depcode=department.depcode

select wlast, wname,regdug,salary
from worker w inner join salary s
on w.wcode=s.wcode
order by salary asc

select wlast, wname,regdug,salary
from worker w inner join salary s
on w.wcode=s.wcode
where salary >= '1000000' and salary  <='1200000'
order by salary asc