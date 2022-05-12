from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy.orm import relationship


class Category(SqlAlchemyBase):
    __tablename__ = 'categories'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    questions = relationship("Question", back_populates='category')
