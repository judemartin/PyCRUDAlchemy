import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from src.data.modelbase import SqlAlchemyBase

__factory = None


def global_init(db_conn_str: str):
    global __factory

    if __factory:
        return

    if not db_conn_str or not db_conn_str.strip():
        raise Exception("You must specify a connection string.")

    conn_str = db_conn_str.strip()
    print("Connecting to DB with {}".format(conn_str))

    # Adding check_same_thread = False after the recording. This can be an issue about
    # creating / owner thread when cleaning up sessions, etc. This is a sqlite restriction
    # that we probably don't care about in this example.
    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import src.data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
