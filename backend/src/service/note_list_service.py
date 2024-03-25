from db import database
from utils import response

class NoteListService():
  def __init__(self):
    self.__db = database.Database()

  def create_note_list(self,note_list):
    values = (note_list['name'],note_list['id_user'])
    responseObj = {}
    resultSet = self.__db.insert("insert into note_list(name,id_user) values (%s,%s)",values)
    if resultSet['rowsAffected'] == 1:
      responseObj = response.Response(200,"Success", "Note List Created with Success", str(resultSet["lastId"]))
    else:
      responseObj = response.Response(500,"Error", "Error While Inserting Note List in Database", "")
    
    return responseObj

  def update_note_list_name(self,name,id):
    values = (name['name'],id)
    responseObj = {}
    rowsAffected = self.__db.update("update note_list set name = %s where id = %s",values)
    if rowsAffected == 1:
      responseObj = response.Response(200,"Success", "Note List Update With Success", "")
    elif rowsAffected == 0:
      responseObj = response.Response(404,"Info", "Note List Not Found", "")
    else:
      responseObj = response.Response(500,"Error", "Error While Updating Note List in Database", "") 

    return responseObj

  def delete_note_list(self,id):
    values = [id]
    rowsAffected = self.__db.delete("delete from note_list where id = %s",values)
    responseObj = {}
    if rowsAffected == 1:
      responseObj = response.Response(200,"Success", "Note List Deleted With Success", "")
    elif rowsAffected == 0:
      responseObj = response.Response(404,"Info", "Note List Not Found", "")
    else:
      responseObj = response.Response(500,"Error", "Error While Deleting Note List in Database", "") 

    return responseObj