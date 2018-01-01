rem Kyle Finter
rem Finter179

create assertion name_exists check
(not exists (select * from address, salaried_worker, hourly_worker
             where address.name <> salaried_worker.name and address.name <> hourly_worker.name))