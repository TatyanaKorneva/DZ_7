DROP DATABASE IF EXISTS handbook;
CREATE DATABASE handbook;
USE handbook;

DROP TABLE IF exists individuals;
CREATE TABLE individuals(
id bigint unsigned NOT NULL AUTO_INCREMENT,
lastname varchar(100),
firstname varchar(100),
middlename varchar(100),
company varchar(50),
work_phone varchar(50),
cellular_phone varchar(50),
email varchar(120),
 PRIMARY KEY (id)
);

INSERT ignore INTO  individuals (lastname, firstname,middlename, company, work_phone, cellular_phone, email) VALUES
	('Воевода','Надежда','Васильевна','ГАУ РК "ЦИТ"','88212443355','89042224562','Nadezhda.Voevoda@rkcit.ru'),
	('Нурдынова','Ирина','Викторовна','ГАУ РК "ЦИТ"','88212445236', '89125649898','Irina.Nurdynova@rkcit.ru');

select * from individuals;


