import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped

from models.model_base import ModelBase
from models.cronograma import Cronograma
from models.usuario import Usuario

from datetime import datetime

class Tarefa(ModelBase):
    __tablename__: str = 'tarefas'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_cadastro: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    nome: str = sa.Column(sa.String(45), nullable=False)
    detalhamento: str = sa.Column(sa.String(100), nullable=False)
    localizacao_no_tamanho: int = sa.Column(sa.Integer, nullable=False)

    # Cada tarefa é exclusiva de um cronograma
    id_cronograma: int = sa.Column(sa.Integer, sa.ForeignKey('cronogramas.id'))
    cronograma: Mapped[Cronograma] = orm.relationship('Cronograma', lazy='joined')

    # Cada tarefa é exclusiva de um usuário
    id_usuario: int = sa.Column(sa.Integer, sa.ForeignKey('usuarios.id'))
    usuario: Mapped[Usuario] = orm.relationship('Usuario', lazy='joined')

    def __repr__(self) -> str:
        return f'<Tarefa: {self.nome}>'