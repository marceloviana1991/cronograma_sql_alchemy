from typing import List

from sqlalchemy import func

from conf.db_session import create_session

from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao

# Select Simples
def select_todos_usuarios() -> List[Usuario]:
    """
    Captura um lista com todos os usuarios da tabela.
    """
    with create_session() as session:
        usuarios: List[Usuario] = session.query(Usuario)
    return usuarios

def select_todos_cronogramas() -> List[Cronograma]:
    """
    Captura um lista com todos os cronogramas da tabela.
    """
    with create_session() as session:
        cronogramas: List[Cronograma] = session.query(Cronograma)
    return cronogramas

def select_todas_tarefas() -> List[Tarefa]:
    """
    Captura um lista com todos as tarefas da tabela.
    """
    with create_session() as session:
        tarefas: List[Tarefa] = session.query(Tarefa)
    return tarefas

def select_todas_avaliacoes() -> List[Avaliacao]:
    """
    Captura um lista com todos as avaliações da tabela.
    """
    with create_session() as session:
        avaliacoes: List[Avaliacao] = session.query(Avaliacao)
    return avaliacoes

#Select com filtro
def select_filtro_usuario(id_usuario: int) -> Usuario:
    """
    Captura um usuário da tabela pelo id.
    """
    with create_session() as session:
        usuario: Usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    return usuario

def select_filtro_cronograma(id_cronograma: int) -> Cronograma:
    """
    Captura um cronograma da tabela pelo id.
    """
    with create_session() as session:
        cronograma: Cronograma = session.query(Cronograma)\
            .filter(Cronograma.id==id_cronograma).first()
    return cronograma

def select_filtro_tarefas(id_tarefa: int) -> Tarefa:
    """
    Captura uma tarefa da tabela pelo id.
    """
    with create_session() as session:
        tarefa: Tarefa = session.query(Tarefa).filter(Tarefa.id==id_tarefa).first()
    return tarefa

def select_filtro_tarefas_localizacao_no_tamanho(id_cronograma: int, 
                                                 localizacao_no_tamanho: int) -> List[Tarefa]:
    """
    Captura uma lista de tarefas pelos parâmetros localizacao_no_tamanho e id_cronograma.
    """
    with create_session() as session:
        tarefas: Tarefa = session.query(Tarefa).filter(Tarefa.id_cronograma==id_cronograma)\
            .filter(Tarefa.localizacao_no_tamanho==localizacao_no_tamanho)
    return tarefas

def select_filtro_avaliacoes(id_avaliacao: int) -> Avaliacao:
    """
    Captura uma avaliação da tabela pelo id.
    """
    with create_session() as session:
        avaliacao: Avaliacao = session.query(Avaliacao).filter(Avaliacao.id==id_avaliacao).first()
    return avaliacao

def select_filtro_avaliacoes(id_tarefa: int) -> List[Avaliacao]:
    """
    Captura uma lista de avaliações pelo parâmetro id_tarefa.
    """
    with create_session() as session:
        avaliacoes: List[Avaliacao] = session.query(Avaliacao)\
            .filter(Avaliacao.id_tarefa==id_tarefa)
    return avaliacoes

if __name__ == '__main__':
    pass