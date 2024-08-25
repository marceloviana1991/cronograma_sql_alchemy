"""
1 - Buscar o registro a ser atualizado;
2 - Fazer as alterações no registro;
3- Salvar o registro no banco de dados;

OBS: Não faz alteração de parâmetros refentes a chave estrangeira
"""
import asyncio
from sqlalchemy.future import select

from conf.db_session import create_session

from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao

from typing import Optional


async def atualizar_usuario(id: int, novo_email: str, nova_senha: str) -> Optional[Usuario]:
    """
    Atualiza os parametros email e senha de um registro da tabela usuário
    """
    async with create_session() as session:
        query = select(Usuario).filter(Usuario.id==id)
        usuario: Optional[Usuario] = await session.execute(query)
        usuario = usuario.scalars().first()
        if usuario:
            usuario.email = novo_email
            usuario.senha = nova_senha
            await session.commit()
        else:
            return None
    return usuario


async def atualizar_cronograma(id: int, novo_nome: str, novo_tamanho: int) -> Optional[Cronograma]:
    """
    Atualiza os parametros nome e tamanho de um registro da tabela cronograma
    """
    async with create_session() as session:
        query = select(Cronograma).filter(Cronograma.id==id)
        cronograma: Optional[Cronograma] = await session.execute(query)
        cronograma = cronograma.scalars().first()
        if cronograma:
            cronograma.nome = novo_nome
            cronograma.tamanho = novo_tamanho
            await session.commit()
        else:
            return None
    return cronograma
    

async def atualizar_tarefa(id: int, novo_nome: str, novo_detalhamento: 
                         str, nova_localizacao_no_tamanho: int) -> Optional[Tarefa]:
    """
    Atualiza os parametros nome, detalhamento e localização no tamanho de um registro da tabela tarefa
    """
    async with create_session() as session:
        query = select(Tarefa).filter(Tarefa.id==id)
        tarefa: Optional[Tarefa] = await session.execute(query)
        tarefa = tarefa.scalars().first()
        if tarefa:
            tarefa.nome = novo_nome
            tarefa.detalhamento = novo_detalhamento
            tarefa.localizacao_no_tamanho = nova_localizacao_no_tamanho
            await session.commit()
        else:
            return None
    return tarefa


async def atualizar_avaliacao(id: int, novo_retorno: str) -> Optional[Avaliacao]:
    """
    Atualiza o parametro retorno de um registro da tabela avaliação
    """
    async with create_session() as session:
        query = select(Avaliacao).filter(Avaliacao.id==id)
        avaliacao: Optional[Avaliacao] = await session.execute(query)
        avaliacao = avaliacao.scalars().first()
        if avaliacao:
            avaliacao.retorno = novo_retorno
            await session.commit()
        else:
            return None
    return avaliacao    
    
    
if __name__ == '__main__':
    variavel = asyncio.run()
    print(variavel)
