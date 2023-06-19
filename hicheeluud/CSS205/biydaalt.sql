---150-190 iin hoorond duriin toog gargaj irh 150 bolon 190 orhgui
select floor(random()*(190-150)+150)

---0-1 iin hoorond duriin toog gargaj irh 0 bolon 1 orohgui
select random()

SELECT floor(random()*(10-1+1))+1

SELECT floor(random()*(40-25+1))+25

---unuudriin on sar udur tsag minut sekund tsagiin bus gargana
SELECT now();

--- umnuh bichlegiig uur bichlegeer solih
UPDATE 
   branch
SET 
   bname = REPLACE(bname,'Сэнтий-2 ресторан','Тэнгэр-2 ресторан')
   
SELECT
	REPLACE ('2BC 22', '2', 'Z')
	
----orngoor avh(toimloh)
SELECT ROUND(67.456) AS "Round";

---taslalaas hoish 1 orngoor toimloh
SELECT ROUND(67.456,1) AS "Round";

----toonii zereg oloh 
SELECT POWER(7,3) AS "7-ийн 3 зэрэг"

select dprice,power(dprice,0.3) from debt

