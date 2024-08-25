import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped

from models.model_base import ModelBase
from models.usuario import Usuario

from datetime import datetime
from typing import List, Optional

# Cronograma pode ter vários usuários
usuario_cronograma = sa.Table(
    'usuario_cronograma',
    ModelBase.metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column('id_cronograma', sa.Integer, sa.ForeignKey('cronogramas.id')),
    sa.Column('id_usuario', sa.Integer, sa.ForeignKey('usuarios.id'))
)

class Cronograma(ModelBase):
    __tablename__: str = 'cronogramas'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_cadastro: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    nome: str = sa.Column(sa.String(45), nullable=False)
    tamanho: int = sa.Column(sa.Integer, nullable=False)

    # Usuário que vai instanciar o objeto cronograma
    id_usuario: int = sa.Column(sa.Integer, sa.ForeignKey('usuarios.id'))
    usuario: Mapped[Usuario] = orm.relationship('Usuario', lazy='joined')

    # Usuários que vão fazer parte do grupo do cronograma
    usuarios: Mapped[Optional[List[Usuario]]] = orm.relationship('Usuario', secondary=usuario_cronograma, backref='usuario', lazy='joined')

    def __repr__(self) -> str:
        return f'<Cronograma: {self.nome}>'