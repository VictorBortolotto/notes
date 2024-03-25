from db import database

class NoteService():
  def __init__(self):
    self.__db = database.Database()
  
  def create_note(self,note):
    values = (note['name'],note['description'])
    self.__db.insert("insert into note(name,description) values(%s,%s)", values)