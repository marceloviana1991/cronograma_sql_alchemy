"""
1 - Buscar o registro a ser excluido;
2 - Exclui o registro;
3- Salvar a alteração no banco de dados;

OBS: Não é permitido excluir registros que são referência de chave estrangeira em outras tabelas,
exceto quando o resgistro for refência na tabela 'usuario_cronograma'
"""
import asyncio
from sqlalchemy.future import select

from typing import Optional

from conf.db_session import create_session

from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao


async def deletar_usuario(id: int) -> Optional[Usuario]:
    # Verificar referência de chave estrangeira em outras tabelas
    """
    Exclui usuário do banco de dados
    """
    async with create_session() as session:
        query = select(Usuario).filter(Usuario.id==id)
        usuario: Optional[Usuario] = await session.execute(query)
        usuario = usuario.scalars().first()
        if usuario:
            await session.delete(usuario)
            await session.commit()
        else:
            return None
    return usuario


async def deletar_cronograma(id: int) -> Optional[Cronograma]:
    # Verificar referência de chave estrangeira em outras tabelas
    """
    Exclui cronograma do banco de dados
    """
    async with create_session() as session:
        query = select(Cronograma).filter(Cronograma.id==id)
        cronograma: Optional[Cronograma] = await session.execute(query)
        cronograma = cronograma.scalars().first()
        if cronograma:
            await session.delete(cronograma)
            await session.commit()
        else:
            return None
    return cronograma


async def deletar_tarefa(id: int) -> Optional[Tarefa]:
    # Verificar referência de chave estrangeira em outras tabelas
    """
    Exclui tarefa do banco de dados
    """
    async with create_session() as session:
        query = select(Tarefa).filter(Tarefa.id==id)
        tarefa: Optional[Tarefa] = await session.execute(query)
        tarefa = tarefa.scalars().first()
        if tarefa:
            await session.delete(tarefa)
            await session.commit()
        else:
            return None
    return tarefa


async def deletar_avaliacao(id: int) -> Optional[Avaliacao]:
    """
    Exclui avaliação do banco de dados
    """
    async with create_session() as session:
        query = select(Avaliacao).filter(Avaliacao.id==id)
        avaliacao: Optional[Avaliacao] = await session.execute(query)
        avaliacao = avaliacao.scalars().first()
        if avaliacao:
            await session.delete(avaliacao)
            await session.commit()
        else:
            return None
    return avaliacao  


if __name__ == '__main__':
    variavel = asyncio.run()
    print(variavel)