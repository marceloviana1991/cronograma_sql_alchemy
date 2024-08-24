"""
1 - Buscar o registro a ser atualizado;
2 - Fazer as alterações no registro;
3- Salvar o registro no banco de dados;

OBS: Não faz alteração de parâmetros refentes a chave estrangeira
"""
from conf.db_session import create_session

from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao

from typing import Optional

def atualizar_usuario(id: int, novo_email: str, nova_senha: str) -> Optional[Usuario]:
    with create_session() as session:
        usuario: Optional[Usuario] = session.query(Usuario).filter(Usuario.id==id).one_or_none()
        if usuario:
            usuario.email = novo_email
            usuario.senha = nova_senha
            session.commit()
        else:
            print(f'Usuário não encontrado')
    return usuario
    
def atualizar_cronograma(id: int, novo_nome: str, novo_tamanho: int) -> Optional[Cronograma]:
    with create_session() as session:
        cronograma: Optional[Cronograma] = session.query(Cronograma).filter(Cronograma.id==id).one_or_none()
        if cronograma:
            cronograma.nome = novo_nome
            cronograma.tamanho = novo_tamanho
            session.commit()
        else:
            print(f'Cronograma não encontrado')
    return cronograma
    
def atualizar_cronograma(id: int, novo_nome: str, novo_detalhamento: 
                         str, nova_localizacao_no_tamanho: int) -> Optional[Tarefa]:
    with create_session() as session:
        tarefa: Optional[Tarefa] = session.query(Tarefa).filter(Tarefa.id==id).one_or_none()
        if tarefa:
            tarefa.nome = novo_nome
            tarefa.detalhamento = novo_detalhamento
            tarefa.localizacao_no_tamanho = nova_localizacao_no_tamanho
            session.commit()
        else:
            print(f'Tarefa não encontrada')
    return tarefa

def atualizar_avaliacao(id: int, novo_retorno: str) -> Optional[Avaliacao]:
    with create_session() as session:
        avaliacao: Optional[Avaliacao] = session.query(Avaliacao).filter(Avaliacao.id==id).one_or_none()
        if avaliacao:
            avaliacao.retorno = novo_retorno
            session.commit()
        else:
            print(f'Avaliação não encontrada')
    return avaliacao    


    
if __name__ == '__main__':
    pass
