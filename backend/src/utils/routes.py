from enum import Enum

class Routes(Enum):
  USER = '/user'
  NEW_USER = USER + '/new-user'
  UPDATE_USER_PASSWORD = USER + '/<id>/new-password'
  NOTE_LIST = '/note-list'
  NEW_NOTE_LIST = NOTE_LIST + '/new'
  UPDATE_NOTE_LIST_NAME = NOTE_LIST + '/<id>/update-name'
  DELETE_NOTE_LIST = NOTE_LIST + '/<id>/delete'
  NOTE = '/note'
  NEW_NOTE = NOTE + '/new'
  UPDATE_NOTE_NAME = NOTE + '/<id>/update-name'
  UPDATE_NOTE_DESCRIPTION = NOTE + '/<id>/update-description'
  DELETE_NOTE = NOTE_LIST + "/<id_note_list>" + NOTE + '/<id_note>/delete'