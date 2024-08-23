import sqlalchemy as sa

from models.model_base import ModelBase

from datetime import datetime

class Usuario(ModelBase):
    __tablename__: str = 'usuarios'

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_cadastro: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    email: str = sa.Column(sa.String(45), unique=True, nullable=False)
    senha: str = sa.Column(sa.String(45), nullable=False)

    def __repr__(self) -> str:
        return f'<Usuário: {self.email}>'