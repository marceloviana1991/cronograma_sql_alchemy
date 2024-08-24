import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped

from models.model_base import ModelBase
from models.usuario import Usuario
from models.cronograma import Cronograma
from models.tarefa import Tarefa

from datetime import datetime

class Avaliacao(ModelBase):
    __tablename__: str = 'avaliacoes'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_cadastro: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    retorno: str = sa.Column(sa.String(250), nullable=False)

    # Cada avaliação é exclusiva de um usuário
    id_usuario: int = sa.Column(sa.Integer, sa.ForeignKey('usuarios.id'))
    usuario: Mapped[Usuario] = orm.relationship('Usuario', lazy='joined')

    # Cada avaliação é exclusiva de um cronograma
    id_cronograma: int = sa.Column(sa.Integer, sa.ForeignKey('cronogramas.id'))
    cronograma: Mapped[Cronograma] = orm.relationship('Cronograma', lazy='joined')

    # Cada avaliação é exclusiva de uma tarefa
    id_tarefa: int = sa.Column(sa.Integer, sa.ForeignKey('tarefas.id'))
    tarefa: Mapped[Tarefa] = orm.relationship('Tarefa', lazy='joined')

    def __repr__(self) -> str:
        return f'<Avaliação: {self.retorno}>'