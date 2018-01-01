REM Kyle Finter
REM Finter179

REM 1
select id from instructor intersect select id from student;

REM 2
select id from instructor where id in(select id from student);

REM 3
select id from instructor where id =some(select id from student);

REM 4
select id from instructor where exists(select student.id from student where student.id = instructor.id);

REM 5
select student.name,student.id from student join takes on student.id=takes.id
where takes.course_id =all(
	select course.course_id from course where student.dept_name=course.dept_name);

REM 6
select student.name,student.id from student where 1=(
	select count(takes.id) from takes where takes.year=2010 
	and takes.semester='Spring' and student.id=takes.id);

REM 7
select student.name,student.id from student where 1>=(
	select count(takes.id) from takes where takes.year=2010 
	and takes.semester='Spring' and student.id=takes.id);
	
Rem 8
select id,number_courses
from(select id,count(id) number_courses
		from takes where semester='Spring' and year=2010 group by id)
where number_courses >=2;

REM 9
select name,id,(select count(course_id) from teaches 
				where teaches.id=instructor.id group by id) number_courses
from instructor;

REM 10
select name,course_id from instructor full outer join teaches 
on instructor.id=teaches.id where semester<>'Spring' or year<>2010;

REM 11 extra credit close makes all appear
select id,max(student_courses) number_courses from(
		select id,count(id) student_courses from takes group by id)
		where student_courses >= all(select count(id) from takes group by id)
		group by id;