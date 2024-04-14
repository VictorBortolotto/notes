from db import database
from utils import response

class UserService():
  def __init__(self):
    self.__db = database.Database()

  def create_user(self,newUser):
    values = (newUser['email'], newUser['password'])
    responseObj = {}
    resultSet = self.__db.insert("insert into users(email,password) values(%s, %s)", values)
    if resultSet['rowsAffected'] == 1:
      responseObj = response.Response(200,"Success", "User Created with Success", str(resultSet["lastId"]))
    else:
      responseObj = response.Response(500,"Error", "Error while insert user in database","")
      print(responseObj.response_to_json())
    
    return responseObj
  
  def update_user_password(self,data,id):
    values = (data['password'], id)
    rowsAffected = self.__db.update("update users set password = %s where id = %s", values)
    if rowsAffected == 1:
      responseObj = response.Response(200,"Success", "User Update with Success", "")
    elif rowsAffected == 0:
      responseObj = response.Response(404,"Info", "User Not Found", "")
    else:
      responseObj = response.Response(500,"Error", "Error While Update User in Database", "")

    return responseObj