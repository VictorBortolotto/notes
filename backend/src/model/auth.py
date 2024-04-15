import datetime
import random
import string
import jwt

class Auth(): 
  def __init__(self):
    self.__email = ''
    self.__password = ''

  def get_email(self):
    return self.__email
  
  def set_email(self, email):
    self.__email = email

  def get_password(self):
    return self.__password
  
  def set_pasword(self, pasword):
    self.__password = pasword

  def get_token(self):
    return self.__generate_token()
  
  def __generate_token(self):
    date = datetime.datetime.now() + datetime.timedelta(hours=12)
    token = jwt.encode({ "email": self.__email, "expiresIn":  str(date)}, self.__generate_secret_key())
    return token
  
  def __generate_secret_key(self):
    random_text = string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(random_text) for i in range(12))

  