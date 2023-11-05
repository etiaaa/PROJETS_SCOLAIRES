-- SQLite 

CREATE TABLE Terrorist_Attack (
    ID_ATTACK INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "DATE" DATE,
    COUNTRY VARCHAR(100),
    CITY VARCHAR(100),
    PERPETRATOR_GROUP VARCHAR(100),
    FATALITIES INT NOT NULL,
    INJURED INT NOT NULL,
    TARGET_TYPE VARCHAR(100)
);

CREATE TABLE Person_Traumatised (
    ID_PERSON INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    GENDER VARCHAR(100),
    LASTNAME VARCHAR(100),
    FIRSTNAME VARCHAR(100),
    ADDRESS VARCHAR(100),
    EMAIL VARCHAR(100),
    AGE INT NOT NULL,
    ORIGIN VARCHAR(100),
    CAUSE VARCHAR(100),
    FOREIGN KEY(CAUSE) REFERENCES Terrorist_Attack(CITY)
);