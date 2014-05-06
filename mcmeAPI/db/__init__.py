import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

cur_dir = os.path.dirname(os.path.realpath(__file__)) 

engine = create_engine('sqlite:////'+cur_dir+'/users.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

def db_connect():
    from models import User#, Server
    init_db()
    return (db_session, User)