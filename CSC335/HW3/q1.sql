REM Kyle Finter
REM Trace: Finter179

CREATE TABLE employee (
employee_name      VARCHAR2(32) PRIMARY KEY,
street     VARCHAR2(32),
city       VARCHAR2(32));

CREATE TABLE manages(
employee_name VARCHAR2(32),
manager_name VARCHAR2(32),
PRIMARY KEY (employee_name),
CONSTRAINT fk_PerManager FOREIGN KEY (employee_name)
REFERENCES employee(employee_name));

create table company(
company_name VARCHAR2(32) PRIMARY KEY,
city       VARCHAR2(32));

create table works(
employee_name      VARCHAR2(32),
company_name       VARCHAR2(32),
salary             Number(8,2),
PRIMARY KEY (employee_name),
CONSTRAINT fk_employee FOREIGN KEY (employee_name)
REFERENCES employee(employee_name),
CONSTRAINT fk_company FOREIGN KEY (company_name)
REFERENCES company(company_name));