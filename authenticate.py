import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import os
from dotenv import load_dotenv

#from routes import get_db



load_dotenv()

class AuthHandler():
    security = HTTPBearer()
    #pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.getenv("secrets")
    
    def encode_token(self, email):
        secret = os.getenv("secrets")
        algorithms = 'HS256'

        payload = {
            #'exp': datetime.datetime.now() + datetime.timedelta(days=120),
            #'iat': datetime.datetime.now(),
            'sub': email
    
        }
        return jwt.encode(
            payload,
            secret,
            algorithm=algorithms
        )

    def decode_token(self, token):
        try:
            #dectoken = Hash.decrypt(bytes(token, 'ascii')) 
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)

