from typing import Optional

from conf.db_session import create_session

from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa
from models.avaliacao import Avaliacao

def deletar_usuario(id: int) ->Optional[Usuario]:
    with create_session() as session:
        usuario: Optional[Usuario] = session.query(Usuario).filter(Usuario.id==id).one_or_none()
        if usuario:
            session.delete(usuario)
            session.commit()
        else:
            print(f'Usuário não encontrada')
    return usuario

def deletar_cronograma(id: int) ->Optional[Cronograma]:
    with create_session() as session:
        cronograma: Optional[Cronograma] = session.query(Cronograma).filter(Cronograma.id==id).one_or_none()
        if cronograma:
            session.delete(cronograma)
            session.commit()
        else:
            print(f'Cronograma não encontrado')
    return cronograma

def deletar_tarefa(id: int) -> Optional[Tarefa]:
    with create_session() as session:
        tarefa: Optional[Tarefa] = session.query(Tarefa).filter(Tarefa.id==id).one_or_none()
        if tarefa:
            session.delete(tarefa)
            session.commit()
        else:
            print(f'Tarefa não encontrada')
    return tarefa

def deletar_avaliacao(id: int) -> Optional[Avaliacao]:
    with create_session() as session:
        avaliacao: Optional[Avaliacao] = session.query(Avaliacao)\
            .filter(Avaliacao.id==id).one_or_none()
        if avaliacao:
            session.delete(avaliacao)
            session.commit()
        else:
            print(f'Avaliação não encontrada')
    return avaliacao  

if __name__ == '__main__':
    pass