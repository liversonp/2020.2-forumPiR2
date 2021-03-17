CREATE database IF NOT EXISTS pir2
DEFAULT CHARACTER SET utf8
DEFAULT collate utf8_general_ci;

use pir2;


create table USUARIO(
  nome varchar(50) not null,
  sexo char not null default '?',
  como_descobriu_forum varchar(300) ,
  idade int,
  localizacao varchar(100),
  humor varchar(300),
  emprego_lazer varchar(100),
  nivel_instrucao varchar(35),
  data_inscricao date,

  constraint pk_USUARIO primary key (nome)
);
