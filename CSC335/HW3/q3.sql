REM Kyle Finter
REM Trace: Finter179

REM a
select employee_name from works where company_name='First Bank Corporation';

REM b
select employee.employee_name from employee 
join works on employee.employee_name = works.employee_name
join company on works.company_name = company.company_name
where employee.city=company.city;

REM c
select p.employee_name
from employee p, employee r, manages m
where p.employee_name = m.employee_name and m.manager_name = r.employee_name
and p.street = r.street and p.city = r.city;

REM ii
select works.company_name, count(employee_name) as number_employees 
from employee natural join works group by company_name;

REM iii
select works.company_name, count(employee_name) as number_employees
from employee natural join works group by company_name having count(employee_name)>2;

REM d
select employee_name from works w 
where salary>(select avg(salary) 
	from works u where u.company_name=w.company_name);

REM e
select company_name from works
group by company_name
having sum(salary) <= all(select sum(salary) 
	from works group by company_name);