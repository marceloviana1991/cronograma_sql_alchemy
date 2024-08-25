import asyncio

from conf.db_session import create_session

from typing import Optional

from sqlalchemy.future import select

from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao


async def insert_usuario(usuario: Usuario) -> Usuario:
    """
    Insere usuário no banco de dados.
    """
    async with create_session() as session:
        session.add(usuario)
        await session.commit()
    return usuario


async def insert_cronograma(cronograma: Cronograma) -> Cronograma:
    """
    Insere cronograma no banco de dados.
    """
    async with create_session() as session:
        session.add(cronograma)
        await session.commit()
    return cronograma


async def insert_usuario_cronograma(id_cronograma: int, id_usuario: int) -> Optional[Cronograma]:
    """
    Insere no banco de dados registro de relacionamento entre usuário e cronograma.
    """
    async with create_session() as session:
        query = select(Usuario).filter(Usuario.id==id_usuario)
        usuario: Optional[Usuario] = await session.execute(query)
        usuario = usuario.scalars().first()
        if usuario:
            query = select(Cronograma).filter(Cronograma.id==id_cronograma)
            cronograma: Optional[Cronograma] = await session.execute(query)
            cronograma = cronograma.scalars().first()
        else:
            return None
        if usuario not in cronograma.usuarios:
            cronograma.usuarios.append(usuario)
            await session.commit()
        else:
            return None
    return cronograma.usuarios

    

async def insert_terefa(tarefa: Tarefa) -> Tarefa:
    """
    Insere tarefa no banco de dados.
    """
    async with create_session() as session:
        session.add(tarefa)
        await session.commit()
    return tarefa


async def insert_avaliacao(avaliacao: Avaliacao) -> Avaliacao:
    """
    Insere avaliação no banco de dados.
    """
    async with create_session() as session:
        session.add(avaliacao)
        await session.commit()
    return avaliacao


if __name__ == '__main__':
    asyncio.run()

