from database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String


class UserInfo(Base):
    __tablename__='userinfo'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    company = Column(String(50))
    registered_on = Column(String(50))
    api_token = Column(String(300))
    counter = Column(Integer)
    counter_expiry = Column(String(50))


    