from conf.db_session import create_session
from typing import List
from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao


def insert_usuario(usuario: Usuario) -> Usuario:
    """
    Insere usuário no banco de dados.
    """
    with create_session() as session:
        session.add(usuario)
        session.commit()
    return usuario


def insert_cronograma(cronograma: Cronograma) -> Cronograma:
    """
    Insere cronograma no banco de dados, informando o id do usuário.
    """
    with create_session() as session:
        session.add(cronograma)
        session.commit()
    return cronograma


def insert_usuario_cronograma(id_cronograma: int, id_usuario: int) -> None:
    """
    Insere no banco de dados relacionamento entre usuário e cronograma.
    """
    with create_session() as session:
        usuario: Usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
        cronograma: Cronograma = session.query(Cronograma).filter(Cronograma.id==id_cronograma).first()
        if usuario not in cronograma.usuarios:
            cronograma.usuarios.append(usuario)
            session.commit()
    return cronograma

    

def insert_terefa(tarefa: Tarefa) -> Tarefa:
    """
    Insere tarefa no banco de dados, informando id do usuário e
    id do cronograma
    """
    with create_session() as session:
        session.add(tarefa)
        session.commit()
    return tarefa


def insert_avaliacao(avaliacao: Avaliacao) -> Avaliacao:
    """
    Insere avaliação no banco de dados, informando id do usuário,
    id do cronograma e id da tarefa.
    """
    with create_session() as session:
        session.add(avaliacao)
        session.commit()
    return avaliacao


if __name__ == '__main__':
    pass

