import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
import psycopg2

SqlAlchemyBase = dec.declarative_base()

__factory = None

def global_init(base_dir):
    global __factory

    if __factory:
        return

    # conn_str = "postgresql+psycopg2://postgres:1111@db/testdb"

    engine = sa.create_engine(base_dir, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
