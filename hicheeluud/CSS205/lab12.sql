CREATE DATABASE supermarket

CREATE TABLE customers(
dnum bigint NOT NULL,
clast CHARACTER VARYING NOT NULL,
cname CHARACTER VARYING NOT NULL,
creg CHARACTER VARYING NOT NULL,
regdate date NOT NULL,
PRIMARY KEY (dnum));

CREATE TABLE deposit(
    dnum integer NOT NULL,
    deposit bigint NOT NULL,
    ozognoo date NOT NULL,
    tailbar character varying NOT NULL,
    wcode character varying NOT NULL,
    oz character varying NOT NULL,
    PRIMARY KEY (oz)
);

CREATE TABLE worker(
wcode CHARACTER VARYING NOT NULL,
wlast CHARACTER VARYING NOT NULL,
wname CHARACTER VARYING NOT NULL,
regdug CHARACTER VARYING NOT NULL,
dcode INT NOT NULL,
PRIMARY KEY (wcode));

create table department(
dcode INT NOT NULL,
dname CHARACTER VARYING NOT NULL, 
address TEXT NOT NULL,
PRIMARY KEY(dcode));

select * from worker 
order by wname

select cname from customers
where cname like '%туяа%'

select cu.dnum, deposit, tailbar, cname,oz from deposit d
inner join customers cu 
on cu.dnum=d.dnum
where ozognoo between '2009-09-01' and '2012-09-01'

select * from customers
where creg like '%9005%'

select dname, count(wname) from worker
inner join department
on department.dcode=worker.dcode
group by dname

select * from customers
order by regdate desc

select * from worker 
where wcode='T103'

select sum(deposit) from deposit
inner join worker 
on deposit.wcode=worker.wcode
where worker.wcode='T101' and oz like '%рло%'

select wlast, wname, regdug, ozognoo, deposit,oz, dnum
from deposit d inner join worker w
on d.wcode=w.wcode
where oz like '%рло%'

INSERT INTO worker( wcode, wlast,wname,regdug,dcode)
VALUES ('T103', 'Мөнхбат','Урангоо','НЛ95122540', 2)

update worker
set wname = 'Уянга', dcode = 1
where wcode='T103'

delete from worker
where wcode='T103'

insert into department
values ( 4, 'Баянгол салбар','БГД 18-р хорооны хажууд')
