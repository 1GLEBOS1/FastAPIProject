from db import Base
from sqlalchemy import Column, Integer, ForeignKey, Double

class Files(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    number_session = Column(Double, nullable=False)
