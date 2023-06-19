create database nomiinsan

create table student(
stcode CHARACTER VARYING NOT NULL,
stlast CHARACTER VARYING NOT NULL,
stname CHARACTER VARYING NOT NULL,
regdug CHARACTER VARYING NOT NULL,
mcode CHARACTER VARYING NOT NULL,
phone BIGINT NOT NULL,
ognoo DATE NOT NULL,
PRIMARY KEY(stcode))

create table book(
bookcode CHARACTER VARYING NOT NULL,
bookname CHARACTER VARYING NOT NULL,
author CHARACTER VARYING NOT NULL,
tcode CHARACTER VARYING NOT NULL,
dtcode CHARACTER VARYING NOT NULL,
bindex CHARACTER VARYING NOT NULL,
page BIGINT NOT NULL,
PRIMARY KEY(bookcode))

create table turul(
tcode CHARACTER VARYING NOT NULL,
tname CHARACTER VARYING NOT NULL,
PRIMARY KEY(tcode))

create table dedturul(
dtcode CHARACTER VARYING NOT NULL,
dtname CHARACTER VARYING NOT NULL,
PRIMARY KEY(dtcode))

create table mergejil(
mcode CHARACTER VARYING NOT NULL,
mname CHARACTER VARYING NOT NULL,
PRIMARY KEY(mcode))

create table librarian(
libcode CHARACTER VARYING NOT NULL,
liblast CHARACTER VARYING NOT NULL,
libname CHARACTER VARYING NOT NULL,
phone BIGINT NOT NULL,
address TEXT NOT NULL,
PRIMARY KEY(libcode))

create table bookgive(
bookcode CHARACTER VARYING NOT NULL,
bookname CHARACTER VARYING NOT NULL,
enterognoo DATE NOT NULL,
retognoo DATE NOT NULL,
libcode CHARACTER VARYING NOT NULL,
stcode CHARACTER VARYING NOT NULL,
gid INTEGER NOT NULL,
PRIMARY KEY(gid))

select bookcode,bookname,author,bindex,page,tname,dtname 
from book b inner join turul tu
on b.tcode=tu.tcode
inner join dedturul d
on b.dtcode=d.dtcode

select student.*, mname
from student inner join mergejil
on student.mcode=mergejil.mcode
where stname like 'Гэрэл%'

select mname, count(stname) as "Оюутны тоо" 
from student s inner join mergejil me
on s.mcode=me.mcode
group by mname

select * from student s
where stcode='SA14D005'

select stname, libname
from bookgive bg inner join librarian l
on bg.libcode=l.libcode
inner join student s
on bg.stcode=s.stcode
where bookcode='Swco001'

select * from student
order by ognoo asc

select stname, bookname, enterognoo, retognoo,libname
from student s inner join bookgive bg 
on s.stcode=bg.stcode
inner join librarian l
on bg.libcode=l.libcode
where enterognoo between '2015-11-01' and '2015-12-03' and retognoo between '2015-11-01' and '2015-12-03'

