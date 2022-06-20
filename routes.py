from fastapi import APIRouter, Depends
from passlib.hash import bcrypt
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from authenticate import AuthHandler
from user_method import register_user, get_user_profiles, call_limit

user = APIRouter()

models.Base.metadata.create_all(engine)


auth_handler = AuthHandler()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.post('/register_user', tags=['Register'])
def user_signup(email:str=None, first_name:str=None, last_name:str=None, company:str=None, db:Session=Depends(get_db)):
    output = register_user(email, first_name, last_name, company, db)
    return output

@user.get('/user_profile/get', tags=['Get User'])
def get_user_profile(user_id:int=None, email:str=None, db:Session=Depends(get_db), secure=Depends(auth_handler.auth_wrapper)):
    
    output = get_user_profiles(user_id, email, db, secure)
    output = call_limit(user_id, output, db)
    return output


