-- 21
SELECT student_id, surname, stipend*1.2
FROM student
ORDER BY 2;

-- 22 a
SELECT student_id, MAX(mark)
FROM exam_marks
GROUP BY student_id;

-- 22 b
SELECT student_id, min(mark)
FROM exam_marks
GROUP BY student_id;

-- 23 a
SELECT semester, subj_name, subj_id 
FROM subject
ORDER BY semester DESC;

-- 23 b
SELECT semester, subj_name, subj_id 
FROM subject
ORDER BY hour;

-- 24
SELECT exam_date, SUM(mark)
FROM exam_marks
GROUP BY exam_date 
ORDER BY 2 DESC;

-- 25 a
SELECT exam_date, AVG(mark)
FROM exam_marks
GROUP BY exam_date 
ORDER BY 2 DESC;

-- 25 b
SELECT exam_date, MIN(mark)
FROM exam_marks
GROUP BY exam_date 
ORDER BY 2 DESC;

-- 25 c
SELECT exam_date, MAX(mark)
FROM exam_marks
GROUP BY exam_date 
ORDER BY 2 DESC;

-- 26
SELECT mark 
FROM exam_marks 
WHERE student_id = (SELECT student_id
					FROM student
					WHERE surname = "Зайцева");

-- 27
SELECT name 
FROM student
WHERE student_id IN(SELECT student_id 
					FROM exam_marks
					WHERE subj_id = 10 AND MARK > (SELECT AVG(mark)
												   FROM exam_marks
												   WHERE subj_id = 10));

-- 28
SELECT name 
FROM student
WHERE student_id IN(SELECT student_id 
					FROM exam_marks
					WHERE subj_id = 10 AND MARK < (SELECT AVG(mark)
												   FROM exam_marks
												   WHERE subj_id = 10));

-- 29
SELECT COUNT(subj_id)
FROM subject
WHERE subj_id in (SELECT subj_id 
				  FROM exam_marks
				  WHERE student_id in (SELECT student_id 
									   FROM (SELECT student_id, count(subj_id)
											 FROM exam_marks
											 GROUP BY student_id 
											 HAVING count(subj_id) > 1)));

-- 30
SELECT DISTINCT STUDENT_ID, NAME
from student S1
where STIPEND=(SELECT max(stipend)
			   from student S2
			   WHERE S1.CITY = S2.CITY) 

-- 31
SELECT DISTINCT STUDENT_ID, NAME
from student, university
where student.city not in (SELECT city
						   from university)

-- 32
SELECT DISTINCT name, STUDENT_ID
from student S
where city not in (select city
				   FROM university U
				   where S.city = U.city);	

-- 33
SELECT *
from STUDENT
where EXISTS (SELECT *
			  FROM university
              WHERE RATING>300 AND student.UNIV_ID = university.UNIV_ID);

-- 34
SELECT student.*
FROM STUDENT 
inner join university on
student.UNIV_ID=university.UNIV_ID and university.RATING>300;

-- 35
SELECT *
FROM student S1
WHERE EXISTS(SELECT *
			 FROM university U1
			 WHERE S1.city=U1.city AND U1.univ_id != S1.univ_id);
			 
-- 36
SELECT *
from subject S
where EXISTS (SELECT SUBJ_ID, count(STUDENT_ID)
			  from exam_marks EM
			  WHERE S.SUBJ_ID = EM.SUBJ_ID 
			  group by subj_id 
			  HAVING count(student_id)>1);
			  