use db;

CREATE TABLE access_log (
    ID INT NOT NULL AUTO_INCREMENT,
    DateAndTime DateTime NOT NULL,
    UserIP INT UNSIGNED NOT NULL,
    ContainerIP INT UNSIGNED NOT NULL,
    primary key(ID)
);

CREATE TABLE global_count (
    ID enum('count') NOT NULL,
    count INT UNSIGNED DEFAULT '0',
    primary key(ID)
);


INSERT INTO global_count (ID) values ('count')