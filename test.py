email = 'harsh.suvarnagmail.com'
email = email.split('@')

#print(len(email))

counter=0
def cout_func():
    global counter
    counter+=1
    return counter

#print(cout_func())
#print(cout_func())

from cryptography.fernet import Fernet
 

 
key = Fernet.generate_key()

 
fernet = Fernet(key)





from datetime import date, timedelta

now = date.today()
next = '2022-06-21'
print(now)
nexs = now + timedelta(days=1)
print(nexs)

