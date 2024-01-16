CREATE TABLE BILLET (

NUMERO_DU_PASSAGER int auto_increment,
NUMERO_DU_BILLET varchar(50),
DATE_D_EMISSION date,
PRIX varchar(50),


primary key (NUMERO_DU_BILLET),
foreign key (NUMERO_DU_PASSAGER) references PASSAGER(NUMERO_DU_PASSAGER)


);