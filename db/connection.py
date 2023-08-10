from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import get_settings


Base = declarative_base()
SessionLocal = None
Engine  = None

def create_database():
    global SessionLocal
    global Engine
    settings = get_settings()
    SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.postgresuser}:{settings.postgrespassword}@{settings.postgresurl}/{settings.postgresdb}'
    Engine = create_engine(SQLALCHEMY_DATABASE_URL) 

    #Create health function to detect whether the db is working or not

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
    
    if settings.migratedb:
        print("Running migration")
        Base.metadata.create_all(bind=Engine) 


def get_db_session():
    return SessionLocal()