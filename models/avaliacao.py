import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped

from models.model_base import ModelBase
from models.tarefa import Tarefa

from datetime import datetime

class Avaliacao(ModelBase):
    __tablename__: str = 'avaliacoes'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_cadastro: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    nota: float = sa.Column(sa.DECIMAL(1,2), nullable=False)
    retorno: str = sa.Column(sa.String(250), nullable=False)

    id_tarefa: int = sa.Column(sa.Integer, sa.ForeignKey('tarefas.id'))
    tarefa: Mapped[Tarefa] = orm.relationship('Tarefa', lazy='joined')

    def __repr__(self) -> str:
        return f'<Avaliação: {self.nota}>'