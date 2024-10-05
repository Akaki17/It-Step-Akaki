-- Creating the employee table
CREATE TABLE employee (
    employeeid SERIAL PRIMARY KEY,
    employeeidnumber INTEGER NOT NULL UNIQUE,
    lastname VARCHAR(40) NOT NULL,
    firstname VARCHAR(40) NOT NULL,
    cityid INTEGER NOT NULL,
    department VARCHAR(30) NOT NULL,
    CONSTRAINT cityidfk FOREIGN KEY (cityid) REFERENCES cities(cityid)
);

-- Creating the cities table
CREATE TABLE cities (
    cityid SERIAL PRIMARY KEY,
    cityname VARCHAR(20) NOT NULL
);

-- Creating the accounttypes table
CREATE TABLE accounttypes (
    accounttypeid SERIAL PRIMARY KEY,
    accountabbre VARCHAR(15) NOT NULL,
    bankname VARCHAR(20) NOT NULL
);

-- Creating the accounts table
CREATE TABLE accounts (
    accounttypeid serial primary key ,
    accountidnumber VARCHAR(50) NOT NULL UNIQUE,
    employeeidnumber INTEGER,
    CONSTRAINT accounttypefk FOREIGN KEY (accounttypeid) REFERENCES accounttypes(accounttypeid),
    CONSTRAINT employeeidfk FOREIGN KEY (employeeidnumber) REFERENCES employee(employeeidnumber)
);


insert into cities(cityname) values ('Tbilisi'), ('Batumi'), ('Qutaisi'), ('Telavi'), ('Zugdidi')
insert into employee(employeeidnumber, lastname, firstname, cityid, department) values ('12345678', 'Doe','John', '1', 'IT'),
('87654321', 'Bobson', 'Bob', '2', 'Finances'),
('12121212', 'Johnson', 'James', '3', 'Sales'),
('32323232', 'Smith', 'Jason', '4', 'Marketing'),
('54321234', 'Martin', 'Tom', '5', 'HR')

ALTER TABLE accounttypes
ALTER COLUMN bankname TYPE VARCHAR(25);
insert into accounttypes(accountabbre, bankname) values('TBC', 'TBC Bank'),
('BOG', 'Bank Of Georgia'),
('Halyk', 'Halyk Bank'),
('MBC', 'Micro Business Capital'),
('Rico', 'Rico Credit')

ALTER TABLE accounts
ALTER COLUMN accountidnumber DROP NOT NULL;
insert into accounts(accountidnumber) values('12345678'),
('87654321'),
('12121212'),
('32323232'),
('54321234')