-- create table depositor_info_3(depositor_id serial primary key not null,
-- DepOwnerName VARCHAR(20),
-- DateOfBirth date,
-- City VARCHAR(20),
-- StreetName VARCHAR(20),
-- DepositAmount integer,
-- Interest VARCHAR(20),
-- Comission integer,
-- Total integer
-- )


-- insert into depositor_info_3(depownername, dateofbirth, city, streetname, depositamount, interest, comission, total)
-- values('Soso', '1998-01-14', 'Tbilisi', 'Rustaveli', 1400, 5, 13, 2400),
-- ('Tatiana', '2002-05-07', 'Moscow', 'Rustaveli', 2200, 3, 14, 2000),
-- ('Irakli', '2000-04-23', 'Tbilisi', 'Wereteli', 17000, 2, 14, 3300),
-- ('Gela', '1963-09-15', 'Tsagveri', 'Chikhishvilis', 1200, 2, 18, 3300),
-- ('Nino', '2005-02-11', 'Batumi', 'Gorgasali', 1900, 1, 11, 1300),
-- ('Dodo', '1984-09-09', 'London', 'Paster', 3000, 7, 17, 2900),
-- ('Nikola', '1993-02-27', 'New York', 'Pier', 4000, 8, 17, 3900)


-- select * from depositor_info_3
-- select * from depositor_info_3 where depositamount > 1500;
-- select * from depositor_info_3 where city like 'Tbilisi' and streetname like 'Rustaveli'
-- select * from depositor_info_3 where city like 'Batumi' and streetname like 'Gorgasali' and depositamount >= 100 and depositamount <=2000;
-- select * from depositor_info_3 where depownername like 'D%'