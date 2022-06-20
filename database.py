from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker





engine = create_engine('mysql+pymysql://root:HarshSuvarna99@127.0.0.1:3306/applicant_info')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
meta = MetaData()
conn = engine.connect()
Base = declarative_base()



