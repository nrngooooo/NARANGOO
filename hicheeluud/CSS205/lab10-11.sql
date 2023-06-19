select wlast, wname,regdug,email,depname
from worker w inner join department d
on w.depcode=d.depcode

select worker.*, profession.proname
from worker inner join profession 
on worker.procode=profession.procode

select suutname,suutdun, nemname, nemdun, wlast,wname,salary,tax,ndsh,payment,garolgo
from worker w inner join salary s
on w.wcode=s.wcode
inner join suutgal su
on s.suutcode=su.suutcode
inner join nemegdel n
on n.nemcode=s.nemcode

select wlast,wname, depname
from worker w inner join department d
on w.depcode=d.depcode

select depname as "хэлтэсийн нэр", count(wname) as "Workernum" from worker inner join department 
on worker.depcode=department.depcode
group by (depname)

select depname, sum(salary) 
from worker w inner join salary s
on w.wcode=s.wcode
inner join department d
on w.depcode=d.depcode
group by (depname)

select max(nemdun) from nemegdel
select min(nemdun) from nemegdel

select worker.*, profession.proname,depname
from worker inner join profession 
on worker.procode=profession.procode
inner join department 
on worker.depcode=department.depcode

select depname, sum(suutdun)
from salary inner join suutgal
on salary.suutcode=suutgal.suutcode
inner join worker
on salary.wcode=worker.wcode
inner join department
on worker.depcode=department.depcode
group by(depname)

select sum(salary) from salary s inner join worker w
on s.wcode=w.wcode
inner join department d
on w.depcode=d.depcode
where d.depname='Захиргааны хэлтэс'

select avg(salary) from salary s inner join worker w
on s.wcode=w.wcode
inner join department d
on w.depcode=d.depcode
where d.depname='Захиргааны хэлтэс'