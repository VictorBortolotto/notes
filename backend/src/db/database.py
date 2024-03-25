import psycopg
import json 
from pathlib import Path

class Database():
  def __init__(self):
    self.__info = self.__load_database_configuration()
    self.__connection = self.__connect()

  def __load_database_configuration(self):
    root_folder = Path(__file__).parents[2]
    config = open(root_folder / 'resources\\database_config.json')
    info = json.load(config)
    return info

  def __connect(self):
    connection = psycopg.connect(
      dbname=self.__info['database'],
      host=self.__info['host'],
      user=self.__info['user'],
      password=self.__info['password'],
      port=self.__info['port']
    )
    return connection
  
  def __close_connection(self):
    if not self.__connection.closed: self.__connection.close()

  def __commit(self,):
    self.__connection.commit()

  def __create_cursor(self):
    return self.__connection.cursor()
  
  def __close_cursor(self,cursor):
    if not cursor.closed: cursor.close()

  
  def __fetch_select_lines(self,cursor):
    queryResult = cursor.fetchall()
    results = []
    for data in queryResult:
      print(data)
      results.append(data)

    return results

  def insert(self,sql,values):
    cursor = self.__create_cursor()
    resultSet = {
      "rowsAffected": 0,
      "lastId": 0
    }
    try:
      cursor.execute(sql,values)
      resultSet['rowsAffected'] = cursor.rowcount
      cursor.execute("select lastval()")
      resultSet['lastId'] = cursor.fetchone()[0]
      self.__commit()
    except (Exception, psycopg.DatabaseError) as error:
      print(error)
      self.__connection.rollback()
      self.__close_cursor(cursor)
      self.__close_connection()
      resultSet['rowsAffected'] = -1
      return resultSet

    self.__close_cursor(cursor)
    self.__close_connection()
    return resultSet

  def delete(self,sql,values):
    cursor = self.__create_cursor()
    rowsAffected = 0
    try:
      cursor.execute(sql,values)
      rowsAffected = cursor.rowcount
      self.__commit()
    except (Exception, psycopg.DatabaseError) as error:
      print(error)
      self.__connection.rollback()
      self.__close_cursor(cursor)
      self.__close_connection()
      return -1

    self.__close_cursor(cursor)
    self.__close_connection()
    return rowsAffected

  def update(self,sql,values):
    cursor = self.__create_cursor()
    rowsAffected = 0
    try:
      cursor.execute(sql,values)
      rowsAffected = cursor.rowcount
      self.__commit()
    except (Exception, psycopg.DatabaseError) as error:
      print(error)
      self.__connection.rollback()
      self.__close_cursor(cursor)
      self.__close_connection()
      return -1

    self.__close_cursor(cursor)
    self.__close_connection()
    return rowsAffected

  def select(self,sql):
    cursor = self.__create_cursor() 
    results = []
    try:
      cursor.execute(sql)
      results = self.__fetch_select_lines(cursor)
      print(results)
    except (Exception, psycopg.DatabaseError) as error:
      print(error)
      self.__close_cursor(cursor)
      self.__close_connection()
      return -1

    self.__close_cursor(cursor)
    self.__close_connection()
    return results

  def connection_test(self):
    connection = self.__connect()
    if self.__connection.closed == False:
      print('Database Connection is Open')
      self.__close_connection(connection)
