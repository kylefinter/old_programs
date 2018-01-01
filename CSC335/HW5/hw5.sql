REM Kyle Finter
REM Finter179
REM Question 2

create or replace trigger total_salary after insert on emp
referencing new as nrow
for each row
when (nrow.salary > 0)
begin
	update deptsalary
	set totalsalary=totalsalary+:nrow.salary
	where deptsalary.dept=:nrow.dept;
end total_salary;
/