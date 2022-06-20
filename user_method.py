from fastapi import HTTPException
from models import UserInfo
import datetime
from authenticate import AuthHandler
from hashing import Hash
from datetime import date, timedelta, datetime


#tkn_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


def register_user(email, first_name, last_name, company, db):
    emails = email.split('@')
    if email==None or len(emails)==1:
        return 'Please enter a valid email ID'
    elif first_name==None:
        return 'Please enter your first name'
    elif last_name==None:
        return 'Please enter your last name'
    elif company==None:
        return 'Please enter Company name'
    
    
    else:
        email_q = db.query(UserInfo).filter(UserInfo.email==email).first()
        if email_q:
            return 'Email id already registered'

        else:
            token = AuthHandler.encode_token(first_name, email)
            
            user_q = UserInfo(email=email, first_name=first_name, last_name=last_name, company=company, api_token=token, counter=0, counter_expiry=date.today()+timedelta(days=1), registered_on=datetime.now().replace(microsecond=0))
            db.add(user_q)
            db.commit()
            db.refresh(user_q)

        
            return {'Message':'Registration Successful', 'Token':token}

def get_user_profiles(user_id, email, db, secure):
    user_q = db.query(UserInfo).filter(UserInfo.user_id==user_id, UserInfo.email==email).first()
    if user_q ==None:
        return 'Invalid User ID or unregistered Email ID'
    email_q = db.query(UserInfo.email, UserInfo.first_name, UserInfo.last_name).filter(UserInfo.email==email).first()
    #dectoken = Hash.decrypt(str(secure))
    if email_q==None:
        return 'Email id not registered'
    elif str(email_q[0]) == str(secure):
            fullname = email_q[1] +' '+ email_q[2]
            return {'Full Name': fullname, 'Email ID': email_q[0]}
    
    else:
        raise HTTPException(status_code=401, detail='Invalid token!')

    
def call_limit(user_id, output, db):
    
    if output=='Email id not registered':
        pass
    else:
    
        counter = db.query(UserInfo.counter).filter(UserInfo.user_id==user_id).first()
        count_q = db.query(UserInfo).filter(UserInfo.user_id==user_id).update({UserInfo.counter:int(counter[0])+1})
        db.commit()
        
        
    day_q = db.query(UserInfo.counter_expiry).filter(UserInfo.user_id==user_id).first()

    if str(datetime.now()) > str(day_q[0]):
            update_count = db.query(UserInfo).update({UserInfo.counter:0})
            db.commit()
            dat_q = db.query(UserInfo).update({UserInfo.counter_expiry:date.today()+timedelta(days=1)})
            db.commit()
    count_q = db.query(UserInfo.counter).filter(UserInfo.user_id==user_id).first()
    if int(count_q[0])>=11:
        
        return {'Message':'Call quota for the day is over'}
    else:
        return output