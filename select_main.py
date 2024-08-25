import asyncio

from typing import List
from typing import Optional

from sqlalchemy.future import select
from sqlalchemy import func

from conf.db_session import create_session

from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao


# Select Simples
async def select_todos_usuarios() -> List[Usuario]:
    """
    Captura um lista com todos os usuarios da tabela.
    """
    async with create_session() as session:
        query = select(Usuario)
        usuarios: List[Usuario] = await session.execute(query)
        usuarios = usuarios.scalars().all()
    return usuarios


async def select_todos_cronogramas() -> List[Cronograma]:
    """
    Captura um lista com todos os cronogramas da tabela.
    """
    async with create_session() as session:
        query = select(Cronograma)
        cronogramas: List[Cronograma] = await session.execute(query)
        # Utiliza-se unique() por causa das configações de orm
        cronogramas = cronogramas.unique().scalars().all()
    return cronogramas


async def select_todas_tarefas() -> List[Tarefa]:
    """
    Captura um lista com todos as tarefas da tabela.
    """
    async with create_session() as session:
        query = select(Tarefa)
        tarefas: List[Tarefa] = await session.execute(query)
        # Utiliza-se unique() por causa das configações de orm
        tarefas = tarefas.unique().scalars().all()
    return tarefas


async def select_todas_avaliacoes() -> List[Avaliacao]:
    """
    Captura um lista com todos as avaliações da tabela.
    """
    async with create_session() as session:
        query = select(Avaliacao)
        avaliacoes: List[Avaliacao] = await session.execute(query)
        # Utiliza-se unique() por causa das configações de orm
        avaliacoes = avaliacoes.unique().scalars().all()
    return avaliacoes


#Select com filtro
async def select_filtro_usuario(id_usuario: int) -> Optional[Usuario]:
    """
    Captura um usuário da tabela pelo id.
    """
    async with create_session() as session:
        query = select(Usuario).filter(Usuario.id==id_usuario)
        usuario: Optional[Usuario] = await session.execute(query)
        usuario = usuario.scalars().first()
    return usuario


async def select_filtro_cronograma(id_cronograma: int) -> Optional[Cronograma]:
    """
    Captura um cronograma da tabela pelo id.
    """
    async with create_session() as session:
        query = select(Cronograma).filter(Cronograma.id==id_cronograma)
        cronograma: Optional[Cronograma] = await session.execute(query)
        cronograma = cronograma.scalars().first()
    return cronograma


async def select_filtro_tarefa(id_tarefa: int) -> Optional[Tarefa]:
    """
    Captura uma tarefa da tabela pelo id.
    """
    async with create_session() as session:
        query = select(Tarefa).filter(Tarefa.id==id_tarefa)
        tarefa: Optional[Tarefa] = await session.execute(query)
        tarefa = tarefa.scalars().first()
    return tarefa


async def select_filtro_tarefas_por_localizacao_no_tamanho(id_cronograma: int, 
                                                     localizacao_no_tamanho: int) -> List[Tarefa]:
    """
    Captura uma lista de tarefas pelos parâmetros localizacao_no_tamanho e id_cronograma.
    """
    async with create_session() as session:
        query = select(Tarefa).filter(Tarefa.id_cronograma==id_cronograma)\
            .filter(Tarefa.localizacao_no_tamanho==localizacao_no_tamanho)
        tarefas: List[Tarefa] = await session.execute(query)
        tarefas = tarefas.unique().scalars().all()
    return tarefas


async def select_filtro_avaliacao(id_avaliacao: int) -> Optional[Avaliacao]:
    """
    Captura uma avaliação da tabela pelo id.
    """
    async with create_session() as session:
        query = select(Avaliacao).filter(Avaliacao.id==id_avaliacao)
        avaliacao: Optional[Avaliacao] = await session.execute(query)
        avaliacao = avaliacao.scalars().first()
    return avaliacao


async def select_count_avaliacoes_por_tarefa(id_tarefa: int) -> int:
    """
    Captura a quantidade de avaliações de acordo com o parâmetro id_tarefa.
    """
    async with create_session() as session:
        query = select(func.count(Avaliacao.id)).filter(Avaliacao.id_tarefa==id_tarefa)
        n_de_avaliacoes = await session.execute(query)
        n_de_avaliacoes: int = n_de_avaliacoes.scalar()
    return n_de_avaliacoes


if __name__ == '__main__':
    variavel = asyncio.run()
    print(variavel)