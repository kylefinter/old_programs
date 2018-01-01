REM Kyle Finter
REM Trace: Finter179

insert into employee values('Kyle Finter','Harrison','Springfield');
insert into employee values('Jamil Saquer','Rock','Springfield');
insert into employee values('Noah Baird','Holland','Raymore');
insert into employee values('Miranda Wade','Elm','Springfield');
insert into employee values('Emily Carriere','Adams Dairy','Blue Springs');
insert into employee values('Person Name', 'Some Street', 'Some City');
insert into employee values('Ken Vollmar', 'Rock', 'Springfield');
insert into employee values('Paul Snider', 'Rose', 'Kansas City');

insert into manages values('Kyle Finter', 'Jamil Saquer');
insert into manages values('Jamil Saquer', 'Ken Vollmar');
insert into manages values('Noah Baird', 'Jamil Saquer');
insert into manages values('Miranda Wade', 'Kyle Finter');
insert into manages values('Emily Carriere', 'Miranda Wade');
insert into manages values('Person Name', 'Ken Vollmar');

insert into company values('Cerner','Kansas City');
insert into company values('Missouri State University','Springfield');
insert into company values('Chips','Blue Springs');
insert into company values('Wells Fargo','Independence');
insert into company values('First Bank Corporation', 'Some City');

insert into works values('Kyle Finter','Cerner','12000');
insert into works values('Jamil Saquer','Missouri State University','68000');
insert into works values('Noah Baird','Cerner','24000');
insert into works values('Miranda Wade','Wells Fargo','8000');
insert into works values('Emily Carriere','Chips','10000');
insert into works values('Person Name', 'First Bank Corporation', '50000');
insert into works values('Paul Snider', 'Cerner', '75000');