from cryptography.fernet import Fernet
 
key = Fernet.generate_key()
fernet = Fernet(key)

 

class Hash():
    
    def encrypt(token:str):
        encMessage = fernet.encrypt(token.encode())
        return encMessage


    def decrypt(encToken):
        decMessage = fernet.decrypt(encToken).decode()
        return decMessage