from sqlalchemy import create_engine,MetaData

from sqlalchemy.orm import sessionmaker
from app.engine.models.wmc_v3.config import settings
from sqlalchemy_utils import database_exists, create_database


#this file inits the database with tables and creates a session, which is used for db-connections
#productive
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

#test
#engine = create_engine(DATABASE_URI, pool_pre_ping=True)

if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine,autocommit=False, autoflush=False)
meta = MetaData()