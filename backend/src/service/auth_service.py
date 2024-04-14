from werkzeug.security import check_password_hash
import jwt
import datetime
import random
import string
from db import database
from utils import response
from model import auth

class AuthService():
  def __init__(self):
    self.__database = database.Database()
    self.__auth = auth.Auth()

  def authenticate(self, user):
    self.__auth.set_email(user['email'])
    self.__auth.set_pasword(user['password'])
    dbUser = self.__get_user_by_email()
    
    if dbUser == -1: return response.Response(500,"Error", "Erro to search user in database!", "{}")

    if not self.__check_user(dbUser): return response.Response(404,"Not found", "User not found", "{}")
    
    if not self.__check_password(dbUser['password']):
      return response.Response(401,"Unauthorized", "Wrong password!", "{}")
    else:
      self.__generate_token()
      return response.Response(200,"Authorized", "", self.__auth.get_token())

  def __check_user(self, user):
    return len(user) > 0
          
  def __check_password(self, passwordHash):
    return check_password_hash(passwordHash, self.__auth.get_password())
  
  def __get_user_by_email(self):
    return self.__database.select("select email, password from users where email like %s", self.__auth.get_email())
  
  def __generate_token(self):
    token = jwt.encode({ "email": self.__auth.get_email(), "expiresIn": datetime.datetime.now() + datetime.timedelta(hours=12) }, self.__generate_secret_key(), algorithms=["HS256"])
    self.__auth.set_token(token)
  
  def __generate_secret_key(self):
    random_text = string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(random_text) for i in range(12))