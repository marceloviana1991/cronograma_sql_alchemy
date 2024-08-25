# Cronograma de Tarefas

Projeto em SQLAlchemy de implementação de cronograma de tarefas multi-usuário com retorno de avaliação.

## Funcionalidades

- Criação de modelos com configuração de ORM
- Criação de sessão configuração de conexão com banco de dados
- Implementação de métodos DML no banco de dados
- Implementação de métodos assíncronos

## Documentação da Base de Dados

#### Configuração da tabela usuários

| Atributo  | Tipo    |  Descrição             |
| :-------: | :------: | :-------------------: |
| id | BigInteger | primary key, autoincrement |
| data_cadastro | DateTime | default=datetime  |
| email | String(45) | unique, not null        |
| senha | String(45) |        not null         |

#### Configuração da tabela cronogramas

| Atributo  | Tipo    |  Descrição             |
| :-------: | :------: | :-------------------: |
| id | BigInteger | primary key, autoincrement |
| data_cadastro | DateTime | default=datetime  |
| nome | String(45) |          not null        |
| tamanho | Integer |         not null         |
| id_usuario | Integer | ForeignKey            | 

#### Configuração da tabela tarefas

| Atributo  | Tipo    |  Descrição             |
| :-------: | :------: | :-------------------: |
| id | BigInteger | primary key, autoincrement |
| data_cadastro | DateTime | default=datetime  |
| nome | String(45) |          not null        |
| detalhamento | String(100) | not null        |
| localizacao_no_tamanho | Integer |   not null|
| id_usuario | Integer | ForeignKey            |
| id_cronograma | Integer | ForeignKey         |

#### Configuração da tabela avaliacoes

| Atributo  | Tipo    |  Descrição             |
| :-------: | :------: | :-------------------: |
| id | BigInteger | primary key, autoincrement |
| data_cadastro | DateTime | default=datetime  |
| retorno | String(250) |       not null       |
| id_usuario | Integer | ForeignKey            |
| id_cronograma | Integer | ForeignKey         |
| id_tarefa | Integer | ForeignKey         |
