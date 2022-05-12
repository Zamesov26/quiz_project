from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy.orm import relationship
import datetime
from dataclasses import dataclass


@dataclass
class Question(SqlAlchemyBase):
    __tablename__ = 'questions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    question = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('categories.id'))
    category = relationship("Category")

    def to_dict(self):
        date = self.created_date.strftime('%Y-%m-%dT%H:%M:%S.%f').rstrip('0') + 'Z'
        return {
                'id': self.id,
                'created_date': date,
                'question': self.question,
                'category_id': self.category_id,
                'category': self.category.title
                }
