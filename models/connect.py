import os

from sqlalchemy import create_engine, event, Engine
from sqlalchemy.orm import scoped_session, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = 'users.db'
engine = create_engine(f"sqlite:///{BASE_DIR}/{DB_NAME}", echo=True)

# https://docs.sqlalchemy.org/en/20/orm/session_basics.html#what-does-the-session-do
session = scoped_session(
    sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )
)

# 시작/커밋/롤백 블록 구성
# with Session(engine) as session:
#     session.begin()
#     try:
#         session.add(some_object)
#         session.add(some_other_object)
#     except:
#         session.rollback()
#         raise
#     else:
#         session.commit()


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
